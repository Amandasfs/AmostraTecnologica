import csv
from src.models.point import Ponto

def load_points_from_csv(caminho):
    pontos = []
    with open(caminho, newline='', encoding='utf-8') as csvfile:
        leitor = csv.DictReader(csvfile)
        for linha in leitor:
            ponto = Ponto(
                id=int(linha['id']),
                tipo=linha['tipo'],
                x=float(linha['x']),
                y=float(linha['y']),
                populacao=int(linha['populacao']),
                sazonalidade=float(linha['sazonalidade']),
                contaminacao=float(linha['contaminacao']),
                tem_espaco = linha['tem_espaco'].strip().lower() == 'true'
            )
            pontos.append(ponto)
    return pontos
