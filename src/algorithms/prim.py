import heapq

def prim(grafo):
    origem = next(iter(grafo))  # Começa do primeiro nó
    visitados = set([origem])
    arestas = [(peso, origem, destino) for destino, peso in grafo[origem]]
    heapq.heapify(arestas)
    resultado = []

    while arestas:
        peso, u, v = heapq.heappop(arestas)
        if v not in visitados:
            visitados.add(v)
            resultado.append((u, v, peso))
            for destino, custo in grafo[v]:
                if destino not in visitados:
                    heapq.heappush(arestas, (custo, v, destino))

    return resultado
