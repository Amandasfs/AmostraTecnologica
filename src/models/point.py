from dataclasses import dataclass

@dataclass
class Ponto:
    id: int
    tipo: str
    x: float
    y: float
    populacao: int
    sazonalidade: float
    contaminacao: float
    tem_espaco: bool
