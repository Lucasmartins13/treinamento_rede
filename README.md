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
### O código é dividido nas seguintes partes:

### 1. Importação de bibliotecas

. Importa OpenCV, NumPy e a biblioteca Ultralytics para o YOLOv8.

### 2. Definição de funções

. calcular_distancia(p1, p2): Calcula a distância entre dois pontos no plano.

### 3. Carregamento do modelo YOLOv8

. O modelo best (3).pt é carregado para detecção.

### 4.Inicialização do processamento de vídeo

. O vídeo cut_vid.mp4 é aberto com OpenCV.

. As configurações de tamanho do frame e saída (output.mp4) são definidas.

### 5. Loop principal (processamento frame a frame)

. Lê e redimensiona cada frame.

. Faz inferência com YOLOv8.

. Extrai keypoints do gancho e do caminhão.

. Conecta os pontos detectados e calcula as distâncias.

. Exibe e salva o frame processado.

### 6. Finalização

. Libera os recursos de vídeo e fecha as janelas.
## Controles
. O programa exibe o vídeo processado em tempo real.

. Para encerrar a execução, pressione q no teclado.

. O vídeo processado será salvo automaticamente na pasta videos/output.mp4.

## Autor
. Projeto desenvolvido por Lucas Martins.
