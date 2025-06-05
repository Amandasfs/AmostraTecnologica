import networkx as nx
from algoritmo.grafo import criar_grafo_com_descarte

def prim(pontos, arestas):
    """
    Recebe:
      - pontos: lista de dicts com 'id' e 'tem_espaco' (bool)
      - arestas: lista de (origem, destino, peso)
    
    Cria grafo com descarte, calcula MST e retorna lista de arestas do MST:
    [(u, v, peso), ...]
    """

    G = criar_grafo_com_descarte(pontos, arestas)
    mst = nx.minimum_spanning_tree(G, weight='weight')

    mst_list = []
    for u, v, attr in mst.edges(data=True):
        peso = attr['weight']
        mst_list.append((u, v, peso))

    return mst_list
