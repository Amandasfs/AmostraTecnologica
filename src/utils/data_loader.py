import csv
import os

def carregar_pontos(caminho_arquivo):
    caminho_completo = os.path.join(os.path.dirname(__file__), '..', caminho_arquivo)
    caminho_completo = os.path.abspath(caminho_completo)
    pontos = []
    with open(caminho_completo, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            pontos.append({
                'id': int(row['id']),
                'nome': row['nome'],
                'tem_espaco': row['tem_espaco'].lower() == 'true',
                'lat': float(row['lat']),
                'lon': float(row['lon']),
            })
    return pontos

def carregar_arestas(caminho_arquivo):
    caminho_completo = os.path.join(os.path.dirname(__file__), '..', caminho_arquivo)
    caminho_completo = os.path.abspath(caminho_completo)
    arestas = []
    with open(caminho_completo, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            arestas.append((
                int(row['origem']),
                int(row['destino']),
                float(row['peso']),
            ))
    return arestas
