import numpy as np

def calculate_angle(v1, v2):
    # 두 벡터의 각도를 계산하는 함수
    v1 = np.array(v1)
    v2 = np.array(v2)
    cos_theta = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
    angle = np.arccos(cos_theta)
    return np.degrees(angle)

def recognize_number(landmark_list):
    # 각 손가락의 각도를 계산하여 손가락이 펴졌는지 구부러졌는지 판단
    
    thumb_finger_angle = calculate_angle(
        [landmark_list[3][1] - landmark_list[2][1], landmark_list[3][0] - landmark_list[2][0]],
        [landmark_list[2][1] - landmark_list[1][1], landmark_list[2][0] - landmark_list[1][0]]
    )
    
    # 각 손가락의 마디 벡터 계산
    index_finger_angle = calculate_angle(
        [landmark_list[8][1] - landmark_list[6][1], landmark_list[8][0] - landmark_list[6][0]],
        [landmark_list[5][1] - landmark_list[6][1], landmark_list[5][0] - landmark_list[6][0]]
    )
    
    middle_finger_angle = calculate_angle(
        [landmark_list[12][1] - landmark_list[10][1], landmark_list[12][0] - landmark_list[10][0]],
        [landmark_list[9][1] - landmark_list[10][1], landmark_list[9][0] - landmark_list[10][0]]
    )
    
    
    ring_finger_angle = calculate_angle(
        [landmark_list[16][1] - landmark_list[14][1], landmark_list[16][0] - landmark_list[14][0]],
        [landmark_list[13][1] - landmark_list[14][1], landmark_list[13][0] - landmark_list[14][0]]
    )
    
    
    pinky_finger_angle = calculate_angle(
        [landmark_list[20][1] - landmark_list[18][1], landmark_list[20][0] - landmark_list[18][0]],
        [landmark_list[17][1] - landmark_list[18][1], landmark_list[17][0] - landmark_list[18][0]]
    )
    
    
    thumb_open = thumb_finger_angle < 20
    index_open = index_finger_angle > 100
    middle_open = middle_finger_angle > 100
    ring_open = ring_finger_angle > 100
    pinky_open = pinky_finger_angle > 100
    
    
    # 약지, 새끼 손가락도 동일한 방식으로 처리 가능
    # 필요에 따라 각도를 조정

    # if not thumb_open and index_open and not middle_open and not ring_open and not pinky_open:
    #     return 1
    # elif not thumb_open and index_open and middle_open and not ring_open and not pinky_open:
    #     return 2
    # elif not thumb_open and index_open and middle_open and ring_open and not pinky_open:
    #     return 3
    # elif not thumb_open and index_open and middle_open and ring_open and pinky_open:
    #     return 4
    
    if not thumb_open:
        if index_open and not middle_open and not ring_open and not pinky_open:
            return 1
        elif index_open and middle_open and not ring_open and not pinky_open:
            return 2
        elif index_open and middle_open and ring_open and not pinky_open:
            return 3
        elif index_open and middle_open and ring_open and pinky_open:
            return 4
    
    elif thumb_open:
        if not index_open:
            if not middle_open and not ring_open and not pinky_open:
                return 5
            elif middle_open and ring_open and pinky_open:
                return 10
        elif index_open and not middle_open and not ring_open and not pinky_open:
            return 6
        elif index_open and middle_open and not ring_open and not pinky_open:
            return 7
        elif index_open and middle_open and ring_open and not pinky_open:
            return 8
        elif index_open and middle_open and ring_open and pinky_open:
            return 9
    
    return None
