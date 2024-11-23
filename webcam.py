import cv2
import time
import os

import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

model_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'optimal_gesture_recognizer.task')

# Create a GestureRecognizer object
base_options = python.BaseOptions(model_asset_path=model_path)
options = vision.GestureRecognizerOptions(base_options=base_options)
recognizer = vision.GestureRecognizer.create_from_options(options)

cap = cv2.VideoCapture(0)  # '0'은 기본 웹캠을 의미합니다.

if not cap.isOpened():
    print("웹캠을 열 수 없습니다.")
    exit()

gestureRecognized = False  # 제스처 인식 여부를 초기화
recognized_value = None    # 인식된 숫자 값을 저장할 변수

# Real-time gesture recognition loop
while True:
    ret, frame = cap.read()
    if not ret:
        print("프레임을 읽을 수 없습니다.")
        break

    # BGR to RGB 변환 (MediaPipe는 RGB 이미지를 요구함)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Perform gesture recognition on the frame
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)
    start_time = time.time()  # 추론 시작 시간 기록
    recognition_result = recognizer.recognize(mp_image)

    # 예측 결과가 존재하는 경우
    if recognition_result.gestures:
        # 가장 높은 확률의 제스처 가져오기
        top_gesture = recognition_result.gestures[0][0]
        gesture_label = top_gesture.category_name  # 예: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        confidence = top_gesture.score  # 예: 0.95

        # 숫자 제스처가 인식되었다면
        if gesture_label.isdigit():  # 제스처가 숫자인지 확인
            inference_time = time.time() - start_time  # 추론에 걸린 시간
            fps = 1 / inference_time if inference_time > 0 else 0
            cv2.putText(frame, f'FPS: {fps:.2f}', (10, 70), cv2.FONT_HERSHEY_TRIPLEX, 1, (0, 0, 0), 2, cv2.LINE_AA)
            gestureRecognized = True
            recognized_value = int(gesture_label)  # 숫자를 저장

        # 예측 결과를 화면에 출력
        cv2.putText(frame, f'Gesture: {gesture_label} ({confidence:.2f})',
                    (10, 30), cv2.FONT_HERSHEY_TRIPLEX, 1, (0, 0, 0), 2, cv2.LINE_AA)

        
        
    # 프레임 표시
    cv2.imshow('Gesture Recognition', frame)

    # 'q' 키를 누르면 루프 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 웹캠 및 창 닫기
cap.release()
cv2.destroyAllWindows()
