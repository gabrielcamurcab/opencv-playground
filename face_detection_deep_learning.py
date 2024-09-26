import cv2
from deepface import DeepFace

cap = cv2.VideoCapture(2)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    try:
        result = DeepFace.analyze(frame, actions=['gender', 'age', 'emotion'], enforce_detection=False)

        cv2.putText(frame, f"Genero: {result['gender']}", (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)
        cv2.putText(frame, f"Idade: {result['age']}", (50,100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)
        cv2.putText(frame, f"Emoção: {result['dominant_emotion']}", (50,150), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)

    except Exception as e:
        print(f"Erro: {str(e)}")

    cv2.imshow('Reconhecimento de faces', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows() 