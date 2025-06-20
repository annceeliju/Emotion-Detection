import cv2
from deepface import DeepFace
# Load video from webcam
cap = cv2.VideoCapture(0)
while True:
    ret, frame1 = cap.read()
    frame=cv2.flip(frame1,1)
    # Analyze emotion
    results = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)

    # Display emotion on frame
    emotion = results[0]['dominant_emotion']
    cv2.putText(frame, f'Emotion: {emotion}', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (85, 85, 85), 2)

    cv2.imshow("Emotion Recognition", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
