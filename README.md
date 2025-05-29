# 💧 SaneApp – Fase 3: Versão Final

Este projeto simula e analisa uma rede de esgoto utilizando grafos e algoritmos de otimização. A fase 3 introduz a geração de animações demonstrando o comportamento da rede frente a falhas e sua otimização com algoritmo de Prim.

## ✅ Funcionalidades

- 📁 Upload de arquivos CSV contendo os pontos da rede
- 🔄 Identificação automática de estresse na rede com base nos dados
- 🌐 Construção de grafo da rede de esgoto
- 🧠 Aplicação do algoritmo de Prim para otimização das conexões
- 🎥 Geração de animação (`animacao.mp4`) com três etapas:
  1. Exibição da rede completa
  2. Simulação de falha (entupimento)
  3. Exibição da rota otimizada com Prim

## 🛠️ Tecnologias usadas

- Python 3.12
- Flask
- NetworkX
- Matplotlib (com `matplotlib.animation`)
- FFmpeg (para exportação do vídeo)
- HTML + JS (frontend básico se houver)

## ▶️ Como rodar

1. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

2. Execute o backend:
    ```bash
    python -m src.main
    ```

3. Acesse via navegador ou ferramenta como Postman:
    - POST `/upload` → Envie o arquivo CSV
    - GET `/video` → Baixe/veja o vídeo gerado

## 📂 Estrutura do Projeto

saneApp/
├── backend/
│ ├── data/
│ ├── static/
│ │ └── animacao.mp4
│ ├── src/
│ │ ├── main.py
│ │ ├── utils/
│ │ │ └── data_loader.py
│ │ ├── algorithms/
│ │ │ └── prim.py
│ │ └── analysis/
│ │ └── stress_analysis.py

## 📌 Observações

- Certifique-se de ter o FFmpeg instalado e acessível no terminal (`ffmpeg -version`).
- O vídeo é gerado automaticamente no diretório `static/` após cada upload.

---

## 👨‍💻 Autor

- Amanda e Matheus 

