# Projeto de Tracking de Keypoints com YOLOv8
## Descrição
Este projeto utiliza visão computacional para detectar e rastrear keypoints em um vídeo. O objetivo é identificar pontos-chave em um gancho e em um caminhão, conectando corretamente os pontos correspondentes entre os dois objetos. Para isso, foi utilizado o modelo YOLOv8 treinado com keypoints no Kaggle e inferência feita em Python usando OpenCV.
## Funcionalidades
. Detecção de keypoints em um vídeo.

. Conexão automática dos keypoints esquerdos e direitos entre os objetos detectados.
 
. Cálculo da distância entre os pontos conectados.

. Geração de um vídeo de saída com os keypoints e conexões destacadas.

## Tecnologias Utilizadas
. Python

. OpenCV

. YOLOv8 (Ultralytics)

. Roboflow (para anotação e gerenciamento de dataset)

. Kaggle (para treinamento do modelo)
## Como Usar
### Primeiramente, certifique-se de ter instalado:
. Python 3.8+

. OpenCV

. NumPy

. Ultralytics YOLOv8
### Preparação:
. Tenha o modelo YOLOv8 treinado salvo como best (3).pt.

. Coloque o vídeo a ser processado na mesma pasta do código e nomeie-o como cut_vid.mp4.

## Rode o script Python main.py normalmente.

## Saída do Programa
Se o modelo detectar corretamente os keypoints, a saída do vídeo mostrará:

. Os pontos detectados no gancho e no caminhão.

. As conexões entre os pontos esquerdos e direitos destacadas em amarelo.

. A exibição das distâncias calculadas entre os pontos conectados.

. Um vídeo de saída salvo na pasta videos/output.mp4.
## Estrutura do Código
|-- dataset/                # Dataset gerado pelo Roboflow

|-- models/                 # Modelos treinados

|   |-- best.pt             # Modelo treinado

|-- videos/                 # Vídeos de entrada e saída

|   |-- cut_vid.mp4         # Vídeo de entrada

|   |-- output.mp4          # Vídeo com tracking e conexões

|-- main.py                 # Código principal de inferência


|-- README.md               # Documentação do projeto
## Controles
O programa exibe o vídeo processado em tempo real.
Para encerrar a execução, pressione q no teclado.
O vídeo processado será salvo automaticamente na pasta videos/output.mp4.
## Requisitos do Sistema
Python 3.8 ou superior
GPU NVIDIA compatível com CUDA (opcional, mas recomendado para melhor desempenho)
Dependências listadas no arquivo requirements.txt
## Autor
Projeto desenvolvido por Lucas Martins.
