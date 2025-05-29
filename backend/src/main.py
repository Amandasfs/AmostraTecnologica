from flask import Flask, request, jsonify, send_file
from werkzeug.utils import secure_filename
import os
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from src.utils.data_loader import load_points_from_csv
from src.algorithms.prim import prim
from src.analysis.stress_analysis import identificar_estresse

app = Flask(__name__, static_folder='static')
UPLOAD_FOLDER = 'data/'
VIDEO_OUTPUT_PATH = 'static/animacao.mp4'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs('static', exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload_csv():
    if 'file' not in request.files:
        return jsonify({'error': 'Nenhum arquivo enviado'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'Nome de arquivo inválido'}), 400

    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], 'input.csv')
    file.save(file_path)

    try:
        # Carrega lista de pontos com base no CSV formatado
        pontos = load_points_from_csv(file_path)

        # Gera grafo baseado nos pontos e identifica arestas
        grafo_dict = identificar_estresse(pontos)

        # Aplica algoritmo de Prim
        arvore_geradora = prim(grafo_dict)

        # Gera vídeo de animação com a rede e a MST
        gerar_animacao_grafo(grafo_dict, arvore_geradora, VIDEO_OUTPUT_PATH)

        # Prepara resposta com as rotas
        rotas = [
            {'origem': origem, 'destino': destino, 'peso': peso}
            for origem, destino, peso in arvore_geradora
        ]
        return jsonify({'rotas': rotas}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@app.route('/video')
def serve_video():
    try:
        caminho_absoluto = os.path.abspath(VIDEO_OUTPUT_PATH)
        print("Enviando arquivo:", caminho_absoluto)
        return send_file(caminho_absoluto, mimetype='video/mp4')
    except FileNotFoundError:
        return jsonify({'error': 'Vídeo não encontrado'}), 404


def gerar_animacao_grafo(grafo_dict, mst, output_path):
    G = nx.Graph()
    for origem in grafo_dict:
        for destino, peso in grafo_dict[origem]:
            G.add_edge(str(origem), str(destino), weight=round(peso, 2))

    pos = nx.spring_layout(G, seed=42)
    fig, ax = plt.subplots(figsize=(10, 6))

    def draw_step1():
        ax.clear()
        nx.draw(G, pos, with_labels=True, node_color='lightgray',
                edge_color='gray', node_size=1000, font_size=10)
        ax.set_title('Rede de esgoto completa')

    def draw_step2():
        ax.clear()
        G_tmp = G.copy()
        edge_to_remove = list(G_tmp.edges())[0]  # Simula entupimento qualquer
        G_tmp.remove_edge(*edge_to_remove)
        nx.draw(G_tmp, pos, with_labels=True, node_color='orange',
                edge_color='gray', node_size=1000, font_size=10)
        ax.set_title(f'⚠️ Entupimento em {edge_to_remove[0]} → {edge_to_remove[1]}')

    def draw_step3():
        ax.clear()
        mst_graph = nx.Graph()
        for origem, destino, peso in mst:
            mst_graph.add_edge(str(origem), str(destino), weight=round(peso, 2))
        nx.draw(mst_graph, pos, with_labels=True, node_color='salmon',
                edge_color='black', node_size=1000, font_size=10)
        edge_labels = nx.get_edge_attributes(mst_graph, 'weight')
        nx.draw_networkx_edge_labels(mst_graph, pos, edge_labels=edge_labels)
        ax.set_title(" Rota otimizada após entupimento (Prim)")

    steps = [draw_step1, draw_step2, draw_step3]

    def update(i):
        steps[i]()

    ani = animation.FuncAnimation(fig, update, frames=len(steps), repeat=False, interval=2000)

    ani.save(output_path, writer='ffmpeg', fps=1)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
