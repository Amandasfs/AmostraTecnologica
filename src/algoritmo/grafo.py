import networkx as nx

def criar_grafo_com_descarte(pontos, arestas):
    """
    pontos: lista de dicts com ao menos:
      - id (int)
      - tem_espaco (bool)
    arestas: lista de tuplas (id_origem, id_destino, peso)

    Retorna grafo NetworkX com:
      - nós de pontos originais
      - nós extras "descarte_X" para pontos com 'tem_espaco' True
      - arestas entre pontos originais
      - arestas peso 1 entre ponto e seu nó descarte (se tem_espaco)
    """

    G = nx.Graph()

    # Adiciona nós dos pontos
    for p in pontos:
        G.add_node(p['id'], tem_espaco=p.get('tem_espaco', False))

    # Adiciona nós descarte e conecta com peso 1
    for p in pontos:
        if p.get('tem_espaco', False):
            descarte_node = f"descarte_{p['id']}"
            G.add_node(descarte_node, tipo='descarte')
            G.add_edge(p['id'], descarte_node, weight=1)

    # Adiciona arestas normais com peso informado
    for u, v, peso in arestas:
        G.add_edge(u, v, weight=peso)

    return G
