import cv2

# 1. 얼굴 검출 모델 불러오기
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# 2. 카메라 켜기 (0번은 기본 웹캠)
cap = cv2.VideoCapture(0)

while True:
    # 카메라에서 프레임 읽기
    ret, frame = cap.read()
    if not ret:
        break

    # 좌우 반전 (필요 없으면 삭제하세요)
    frame = cv2.flip(frame, 1)

    # 흑백 변환 (검출 속도 향상)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 얼굴 검출
    faces = face_cascade.detectMultiScale(gray, 1.1, 5, minSize=(30, 30))

    # 찾은 얼굴에 사각형 그리기
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, 'Face', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # 화면에 표시
    cv2.imshow('Real-time Face Detection', frame)

    # 'q' 키를 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 종료 처리
cap.release()
cv2.destroyAllWindows()