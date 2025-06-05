import streamlit as st
import folium
from streamlit_folium import st_folium
import networkx as nx

from utils.data_loader import carregar_pontos, carregar_arestas
from algoritmo.mst import prim

# Função pra formatar aresta (trata int e string tipo 'descarte_5')
def edge_id(u, v):
    u_str = str(u)
    v_str = str(v)
    return "-".join(sorted([u_str, v_str]))

# Carrega dados
pontos = carregar_pontos('data/pontos.csv')
arestas = carregar_arestas('data/arestas.csv')

coords = {p['id']: (p['lat'], p['lon']) for p in pontos}
nomes = {p['id']: p['nome'] for p in pontos}

if "entupidas" not in st.session_state:
    st.session_state["entupidas"] = set()
if "origem_fluxo" not in st.session_state:
    st.session_state["origem_fluxo"] = None
if "destino_fluxo" not in st.session_state:
    st.session_state["destino_fluxo"] = None
if "caminho_selecionado" not in st.session_state:
    st.session_state["caminho_selecionado"] = "normal"  # padrão: normal

def update_entupidas():
    st.session_state["entupidas"] = set(st.session_state.tubulacoes_entupidas_multiselect)

def update_origem():
    st.session_state["origem_fluxo"] = st.session_state.origem_select

def update_destino():
    st.session_state["destino_fluxo"] = st.session_state.destino_select

def update_caminho():
    st.session_state["caminho_selecionado"] = st.session_state.caminho_select

st.title("Rede de Tubulações com MST e Pontos de Descarte")

arestas_str = sorted({edge_id(o, d) for o, d, _ in arestas})

st.sidebar.header("Configurações")

entupidas = st.sidebar.multiselect(
    "Tubulações entupidas:",
    options=arestas_str,
    default=list(st.session_state["entupidas"]),
    key="tubulacoes_entupidas_multiselect",
    on_change=update_entupidas
)

pontos_ids = [p['id'] for p in pontos]

origem = st.sidebar.selectbox(
    "Origem do fluxo:",
    options=[None] + pontos_ids,
    format_func=lambda x: nomes.get(x, "") if x is not None else "Nenhum",
    index=pontos_ids.index(st.session_state["origem_fluxo"]) + 1 if st.session_state["origem_fluxo"] in pontos_ids else 0,
    key="origem_select",
    on_change=update_origem
)

destino = st.sidebar.selectbox(
    "Destino do fluxo:",
    options=[None] + pontos_ids,
    format_func=lambda x: nomes.get(x, "") if x is not None else "Nenhum",
    index=pontos_ids.index(st.session_state["destino_fluxo"]) + 1 if st.session_state["destino_fluxo"] in pontos_ids else 0,
    key="destino_select",
    on_change=update_destino
)

caminho_tipo = st.sidebar.radio(
    "Escolha o caminho para visualizar:",
    options=["normal", "alternativo"],
    index=0 if st.session_state["caminho_selecionado"] == "normal" else 1,
    key="caminho_select",
    on_change=update_caminho
)

def montar_grafo(arestas, entupidas_set, permitir_descarte=False):
    G = nx.Graph()
    for o, d, peso in arestas:
        edge = edge_id(o, d)
        if permitir_descarte:
            G.add_edge(o, d, weight=peso)
        else:
            if edge not in entupidas_set:
                G.add_edge(o, d, weight=peso)
    return G

# Grafo sem entupidos (para caminho normal)
G_normal = montar_grafo(arestas, set(), permitir_descarte=True)

# Grafo com entupidos removidos (para caminho alternativo)
G_alt = montar_grafo(arestas, st.session_state["entupidas"])

# Calcula caminhos
path_normal = []
path_alt = []
if origem is not None and destino is not None and origem != destino:
    try:
        path_normal = nx.shortest_path(G_normal, source=origem, target=destino, weight='weight')
    except nx.NetworkXNoPath:
        pass
    try:
        path_alt = nx.shortest_path(G_alt, source=origem, target=destino, weight='weight')
    except nx.NetworkXNoPath:
        pass

# Escolhe caminho pra mostrar baseado na seleção
if st.session_state["caminho_selecionado"] == "normal":
    path_exibir = path_normal
else:
    path_exibir = path_alt

# MST pra base do grafo filtrado
G_mst = montar_grafo(arestas, st.session_state["entupidas"])
mst_arestas = prim(pontos, list(G_mst.edges(data='weight')))
mst_edges_str = {edge_id(u, v) for u, v, _ in mst_arestas}

# Prepare set das arestas do caminho selecionado pra desenhar
path_edges_str = set()
for i in range(len(path_exibir) - 1):
    path_edges_str.add(edge_id(path_exibir[i], path_exibir[i+1]))

mapa = folium.Map(location=[-23.43, -45.08], zoom_start=13)

for p in pontos:
    cor = "gray"  # pontos normais cinza
    if p['id'] == origem:
        cor = "#5C4033"  # marrom - origem
    elif p['id'] == destino:
        cor = "#800080"  # roxo - destino
    elif any(f"descarte_{p['id']}" in edge for edge in mst_edges_str):
        cor = "#004225"  # verde escuro - descarte

    folium.CircleMarker(
        location=(p['lat'], p['lon']),
        radius=8,
        color=cor,
        fill=True,
        fill_color=cor,
        popup=f"{p['nome']} (ID: {p['id']})"
    ).add_to(mapa)

for o, d, peso in arestas:
    edge = edge_id(o, d)
    cor = "#C8A2C8"  # lilás tubulações normais
    peso_largura = max(1, 6 - peso)
    estilo = None
    if edge in st.session_state["entupidas"]:
        cor = "#FF0000"  # vermelho tubulações entupidas
        estilo = 'dash'
    if edge in path_edges_str:
        cor = "#800080"  # roxo caminho escolhido
        peso_largura = 8

    folium.PolyLine(
        locations=[coords[o], coords[d]],
        color=cor,
        weight=peso_largura,
        dash_array='5' if estilo == 'dash' else None,
        tooltip=f"Tubulação {nomes[o]}-{nomes[d]} (Peso: {peso})"
    ).add_to(mapa)

st_folium(mapa, width=700, height=500)

# Info usuário
if path_exibir:
    st.success(f"Caminho {st.session_state['caminho_selecionado']} encontrado: {' -> '.join(nomes[n] for n in path_exibir)}")
else:
    st.warning(f"Nenhum caminho {st.session_state['caminho_selecionado']} disponível entre origem e destino.")

# Debug
with st.expander("Debug info"):
    st.write("Tubulações entupidas:", st.session_state["entupidas"])
    st.write("Origem:", origem)
    st.write("Destino:", destino)
    st.write("Caminho normal:", path_normal)
    st.write("Caminho alternativo:", path_alt)
    st.write("MST arestas:", mst_arestas)
