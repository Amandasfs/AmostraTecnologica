from src.utils.data_loader import load_points_from_csv
from src.algorithms.prim import prim
from src.analysis.stress_analysis import identificar_estresse

def main():
    pontos = load_points_from_csv("data/input.csv")
    grafo = identificar_estresse(pontos)
    arvore_geradora = prim(grafo)
    
    print("Rotas recomendadas (Prim):")
    for origem, destino, peso in arvore_geradora:
        print(f"{origem} -> {destino} | custo: {peso}")

if __name__ == "__main__":
    main()
