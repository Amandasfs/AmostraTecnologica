💧 SaneApp – Sistema de Planejamento de Rotas para Saneamento
Este projeto tem como objetivo simular e planejar rotas de saneamento utilizando o algoritmo de Prim, com base em dados geográficos e sociais.

✅ O que foi feito até agora:
📁 Estrutura do Projeto: 
ESTRUTURAÇÃO DE PASTAS:

saneApp/
│
├── data/                     # Arquivos de entrada e saída de dados
│   ├── input.csv             # Dados de entrada (pontos, coordenadas, etc.)
│   └── output.csv            # Resultados (rotas, recomendações)
│
├── src/                      # Código-fonte principal
│   ├── __init__.py
│   ├── main.py               # Ponto de entrada do programa
│   │
│   ├── algorithms/           # Algoritmos de grafos
│   │   ├── __init__.py
│   │   └── prim.py           # Implementação do algoritmo de Prim
│   │
│   ├── analysis/             # Análises específicas (estresse, contaminação etc.)
│   │   ├── __init__.py
│   │   └── stress_analysis.py
│   │
│   ├── models/               # Classes de dados (dataclasses, enums, etc.)
│   │   ├── __init__.py
│   │   └── point.py          # Representa pontos: sede, estresse, postos
│   │
│   └── utils/                # Funções auxiliares
│       ├── __init__.py
│       └── data_loader.py    # Leitura e escrita de arquivos CSV
│
├── requirements.txt          # Bibliotecas usadas no projeto
├── README.md                 # Explicação do projeto (já fizemos)
└── .gitignore                # Ignorar arquivos temporários, __pycache__, etc.

🧠 Algoritmo de Prim: está sendo utilizado para calcular rotas mínimas entre os pontos com base nas coordenadas geográficas fornecidas.

📄 Leitura de Dados via CSV:

Um arquivo input.csv (temporário) contém os dados dos pontos da cidade, como:

Sede de tratamento

Pontos de estresse

Regiões com alta densidade populacional

Áreas com sazonalidade ou histórico de contaminação

Esses dados são interpretados por uma função chamada load_points_from_csv, localizada no módulo data_loader.py.

🧱 Classe de Ponto: foi criada uma classe que representa cada ponto do sistema, contendo atributos como nome, tipo, coordenadas e se possui espaço para expansão.

🔄 Próximos Passos:
Permitir que o usuário envie seus próprios arquivos CSV via interface.

Criar uma interface gráfica interativa, possivelmente com mapa (ex: Google Maps).

Implementar as decisões automáticas do sistema:

Se não há espaço: sugerir abertura de novas comportas.

Se há espaço: sugerir novos destinos para tratamento orgânico do esgoto.

