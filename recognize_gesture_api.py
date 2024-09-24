from install_packages import install_package

install_package('mediapipe')

install_package('opencv-python')

import cv2
import mediapipe as mp
import time  # 시간 추적을 위한 모듈

from classify_number import recognize_number

def recognize_gesture():
    mp_hands = mp.solutions.hands
    mp_drawing = mp.solutions.drawing_utils

    cap = cv2.VideoCapture(0)

    detected_number = None  # 마지막으로 감지된 숫자
    detection_start_time = None  # 감지가 시작된 시간

    with mp_hands.Hands(
        max_num_hands=1,  # 최대 감지할 손의 개수
        min_detection_confidence=0.7,  # 감지 신뢰도
        min_tracking_confidence=0.7  # 추적 신뢰도
    ) as hands:
        
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                print("카메라에서 영상을 가져올 수 없습니다.")
                break

            # BGR을 RGB로 변환
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # 손을 감지
            result = hands.process(frame_rgb)

            # 결과에서 손의 랜드마크가 감지되었는지 확인
            if result.multi_hand_landmarks:
                
                for hand_landmarks in result.multi_hand_landmarks:
                    # 랜드마크를 그려줌
                    mp_drawing.draw_landmarks(
                        frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                    
                    # 손가락 랜드마크를 이용해 각도를 계산하거나 특정 제스처 인식
                    landmarks = hand_landmarks.landmark
                    # 각 랜드마크의 x, y 좌표를 리스트로 저장
                    landmark_list = [(lm.x, lm.y) for lm in landmarks]
                    # 특정 제스처를 인식하는 코드 작성 가능
                    number = recognize_number(landmark_list)
                    
                    if number is not None:
                        if number == detected_number:
                            # 같은 숫자가 이미 감지되었으면 시간을 체크
                            elapsed_time = time.time() - detection_start_time
                            if elapsed_time >= 3:  # 3초 이상 같은 값이면
                                print(f'Number {number} detected for 3 seconds.')
                                cv2.putText(frame, f'Number : {number}', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
                                cap.release()
                                cv2.destroyAllWindows()
                                return number  # 숫자를 반환하고 종료
                        else:
                            # 숫자가 바뀌면 다시 시간 초기화
                            detected_number = number
                            detection_start_time = time.time()  # 새로운 숫자가 감지된 시간 저장

                        # 화면에 현재 감지된 숫자를 출력
                        cv2.putText(frame, f'Number : {number}', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
                    else:
                        # 숫자가 감지되지 않으면 초기화
                        detected_number = None
                        detection_start_time = None
            
            # 결과를 화면에 표시
            cv2.imshow('Hand Gesture Recognition', frame)
            
            # 'Esc' 키를 누르면 종료
            if cv2.waitKey(5) & 0xFF == 27:
                break

    cap.release()
    cv2.destroyAllWindows()
