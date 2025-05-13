import math

def identificar_estresse(pontos):
    grafo = {}
    for origem in pontos:
        grafo[origem.id] = []
        for destino in pontos:
            if origem.id != destino.id:
                distancia = math.dist((origem.x, origem.y), (destino.x, destino.y))
                grafo[origem.id].append((destino.id, distancia))
    return grafo
