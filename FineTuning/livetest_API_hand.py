import os
import configparser

# AI.ini 파일을 경로에서 불러와 읽습니다.
OUTPUT_FILE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'AI.ini')
output = configparser.ConfigParser()
ret = output.read(OUTPUT_FILE_PATH)

# 만약 실패하면 프로그램을 종료합니다.
if not ret:
    print(f"{OUTPUT_FILE_PATH} 파일이 존재하지 않거나, 읽을 수 없습니다.")
    exit(0)

# =============== <Hand Gesture Recognition> ===============
import cv2
import time

import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

model_path = './gesture_recognizer.task'

# Create a GestureRecognizer object
base_options = python.BaseOptions(model_asset_path=model_path)
options = vision.GestureRecognizerOptions(base_options=base_options)
recognizer = vision.GestureRecognizer.create_from_options(options)
# =============== <Hand Gesture Recognition> ===============

print('모델 로딩 완료')

# AI모델 로딩이 완료되면, AI.ini의 loaded 항목을 1로 변경합니다.
output.set('MODEL', 'loaded', '1')
with open(OUTPUT_FILE_PATH, 'w') as ini:
    output.write(ini)

while True:
    ret = output.read(OUTPUT_FILE_PATH)
    if not ret:
        break
    user_input = input()
    
    # 입력이 'gesture'라면, 제스쳐 인식을 수행합니다.            
    if user_input == 'gesture' and output['GESTURE']['recognized'] == '0':
        # 제스처 인식 수행
        cap = cv2.VideoCapture(0)  # '0'은 기본 웹캠을 의미합니다.

        if not cap.isOpened():
            print("웹캠을 열 수 없습니다.")
            exit()

        print("캠이 작동 중입니다.")  # 캠 시작 문구 출력

        gestureRecognized = False  # 제스처 인식 여부를 초기화
        recognized_value = None    # 인식된 숫자 값을 저장할 변수
        stable_start_time = None   # 숫자가 안정적으로 유지되기 시작한 시간

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
            recognition_result = recognizer.recognize(mp_image)

            # 예측 결과가 존재하는 경우
            if recognition_result.gestures:
                # 가장 높은 확률의 제스처 가져오기
                top_gesture = recognition_result.gestures[0][0]
                gesture_label = top_gesture.category_name  # 예: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

                # 숫자 제스처가 인식되었다면
                if gesture_label.isdigit():  # 제스처가 숫자인지 확인
                    current_value = int(gesture_label)

                    if current_value == recognized_value:
                        # 동일한 숫자가 유지되고 있는 경우
                        if stable_start_time is None:
                            stable_start_time = time.time()  # 유지 시간 측정 시작
                        elif time.time() - stable_start_time >= 3:  # 3초 유지되었는지 확인
                            gestureRecognized = True
                            print(f"숫자 {current_value}가 3초 동안 유지되었습니다.")
                            break
                    else:
                        # 숫자가 바뀌었을 경우 초기화
                        recognized_value = current_value
                        stable_start_time = time.time()

        # 웹캠 종료
        cap.release()

        if gestureRecognized:
            # 제스처가 인식되었다면, AI.ini에 정보를 기록합니다.
            output.set('GESTURE', 'recognized', '1')
            output.set('GESTURE', 'value', str(recognized_value))  # 인식된 숫자 값 기록

            with open(OUTPUT_FILE_PATH, 'w') as ini:
                output.write(ini)
            print("인식된 숫자가 AI.ini에 기록되었습니다.")
        else:
            print('제스처가 인식되지 않았습니다.')
    