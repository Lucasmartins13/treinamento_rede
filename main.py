import cv2
import numpy as np
from ultralytics import YOLO

# Função para calcular a distância entre dois pontos
def calcular_distancia(p1, p2):
    return np.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

# Carregar modelo YOLOv8 treinado
model = YOLO("best (3).pt")  

# Abrir o vídeo
video_path = "cut_vid.mp4"  
cap = cv2.VideoCapture(video_path)

# Reduzir tamanho do frame 
scale_percent = 50  

# Configurar saída de vídeo (opcional)
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.mp4', fourcc, cap.get(cv2.CAP_PROP_FPS), (640, 640))




frame_count = 0
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print ('not ret')
        break


    # Redimensionar frame
    # frame = cv2.resize(frame, (0, 0), fx=scale_percent/100, fy=scale_percent/100)
    frame = cv2.resize(frame, (640,640))
    # Fazer inferência
    results = model(frame)

    # Dicionários para armazenar keypoints do gancho e do caminhão
    keypoints_gancho = None
    keypoints_caminhao = None

    for result in results:
        if result.keypoints is not None:
            keypoints = result.keypoints.xy.cpu().numpy()  # Obtém os keypoints

            for i, kps in enumerate(keypoints):
                if len(kps) >= 2:
                    # Ordenar os keypoints corretamente (esquerdo = menor X, direito = maior X)
                    p1, p2 = sorted([tuple(map(int, kps[0])), tuple(map(int, kps[1]))], key=lambda p: p[0])

                    if result.names[int(result.boxes.cls[i])] == "gancho":
                        keypoints_gancho = (p1, p2)  # (esquerdo, direito)

                    elif result.names[int(result.boxes.cls[i])] == "caminhao":
                        keypoints_caminhao = (p1, p2)  # (esquerdo, direito)

    # Se ambos foram detectados, desenha as conexões corretas
    if keypoints_gancho and keypoints_caminhao:
        yellow = (0, 255, 255)

        # Conectar corretamente os keypoints
        cv2.line(frame, keypoints_gancho[0], keypoints_caminhao[0], yellow, 2)  # Esquerdo com esquerdo
        cv2.line(frame, keypoints_gancho[1], keypoints_caminhao[1], yellow, 2)  # Direito com direito

        # Desenha os pontos 
        for point in keypoints_gancho + keypoints_caminhao:
            cv2.circle(frame, point, 5, yellow, -1)

        # Calcular e mostrar a distância entre os keypoints
        distancia_esquerdo = calcular_distancia(keypoints_gancho[0], keypoints_caminhao[0])
        distancia_direito = calcular_distancia(keypoints_gancho[1], keypoints_caminhao[1])

        # Exibir distâncias na tela 
        cv2.putText(frame, f"Dist. Esquerdo: {distancia_esquerdo:.2f} px", 
                    (keypoints_gancho[0][0], keypoints_gancho[0][1] - 10), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)  # Vermelho

        cv2.putText(frame, f"Dist. Direito: {distancia_direito:.2f} px", 
                    (keypoints_gancho[1][0], keypoints_gancho[1][1] - 10), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)  # Vermelho

    # Exibir frame com keypoints (agora menor)
    cv2.imshow("Detecção de Keypoints", frame)

    # Salvar no vídeo de saída
    out.write(frame)

    # Pressione 'q' para sair
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar recursos
cap.release()
out.release()
cv2.destroyAllWindows()
