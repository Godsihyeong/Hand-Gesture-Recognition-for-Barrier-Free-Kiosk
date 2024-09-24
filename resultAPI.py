import os
import configparser

# import trained model

from recognize_gesture_api import recognize_gesture


# AI.ini 파일을 경로에서 불러와 읽습니다.
OUTPUT_FILE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'AI.ini')
output = configparser.ConfigParser()
ret = output.read(OUTPUT_FILE_PATH)


# 만약 실패하면 프로그램을 종료합니다.
if not ret:
    print(f"{OUTPUT_FILE_PATH} 파일이 존재하지 않거나, 읽을 수 없습니다.")
    exit(0)


# AI모델 로딩 작업을 수행합니다.
#
#
print('모델 로딩 완료')


# AI모델 로딩이 완료되면, AI.ini의 loaded 항목을 1로 변경합니다.
output.set('MODEL', 'loaded', '1')
with open(OUTPUT_FILE_PATH, 'w') as ini:
    output.write(ini)


# 메인 루프
# 연속적인 작업을 위해 루프를 작성합니다.
while True:

    # 루프 내에서 실시간으로 AI.ini를 확인합니다.
    ret = output.read(OUTPUT_FILE_PATH)
    if not ret:
        break

    # 명령어를 표준 입력으로 받아들입니다.
    print(f'작업을 선택해주세요')
    print('===================')
    print(f'1. face\n2. voice\n3. gesture\n4. eye')
    
    user_input = input()

    print(f'{user_input}을 선택하셨습니다.')
    
    # # 입력이 'face'라면, 얼굴 인식을 수행합니다.
    # if user_input == 'face' and output['FACE']['recognized'] == '0':
    #     # 얼굴 인식 수행
    #     #
    #     #
    #     if faceDetected:
    #         # 얼굴이 인식되었다면, AI.ini에 정보를 기록합니다.
    #         print("얼굴이 인식되었습니다.")
    #         output.set('FACE', 'recognized', '1')
    #         output.set('FACE', 'age', '20대')
    #         output.set('FACE', 'sex', 'female')
            
    #         with open(OUTPUT_FILE_PATH, 'w') as ini:
    #             output.write(ini)
    #     else:
    #         print('얼굴이 인식되지 않았습니다')

    # # 입력이 'voice'라면, 음성 인식을 수행합니다.
    # if user_input == 'voice' and output['VOICE']['recognized'] == '0':
    #     # 음성 인식 수행
    #     #
    #     #
    #     if voiceRecognized:
    #         # 음성이 인식되었다면, AI.ini에 정보를 기록합니다.
    #         print("음성이 인식되었습니다.")
            
    #         output.set('VOICE', 'recognized', '1')
    #         output.set('VOICE', 'value', '주민등록')
            
    #         with open(OUTPUT_FILE_PATH, 'w') as ini:
    #             output.write(ini)

    #     else:
    #         print("음성이 인식되지 않았습니다.")
            
    # 입력이 'gesture'라면, 제스쳐 인식을 수행합니다.            
    if user_input == 'gesture' and output['GESTURE']['recognized'] == '0':
        # 제스쳐 인식 수행
        #
        gestureRecognized = recognize_gesture()
        
        if gestureRecognized is not None:
            # 제스쳐가 인식되었다면, AI.ini에 정보를 기록합니다.
            print(f"제스쳐가 {gestureRecognized}가 인식되었습니다.")
            output.set('GESTURE', 'recognized', '1')
            output.set('GESTURE', 'value', str(gestureRecognized))
            
            with open(OUTPUT_FILE_PATH, 'w') as ini:
                output.write(ini)

        else:
            print('제스쳐가 인식되지 않았습니다.')

    # # 입력이 'eye'라면, 시선 추적을 수행합니다.  
    # if user_input == 'eye' and output['EYE']['recognized'] == '0':
    #     # 시선 추적 수행
    #     #
    #     #
    #     if eyeTracked:
    #         # 시선이 인식되었다면, AI.ini에 정보를 기록합니다.
    #         print("시선이 인식되었습니다.")
    #         output.set('EYE', 'recognized', '1')
    #         output.set('EYE', 'x', '374')
    #         output.set('EYE', 'y', '185')
            
    #         with open(OUTPUT_FILE_PATH, 'w') as ini:
    #             output.write(ini)
                
    #     else :
    #         print('시선이 인식되지 않았습니다.')

    # # 입력이 'quit'라면, 루프를 빠져 나갑니다.
    # if user_input == 'quit':
    #     break


print("프로그램이 종료되었습니다.")