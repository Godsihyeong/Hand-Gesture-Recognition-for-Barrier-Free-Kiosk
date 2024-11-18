import os
import shutil
import random

from tqdm import tqdm

import tensorflow as tf
assert tf.__version__.startswith('2')

from mediapipe_model_maker import gesture_recognizer

import matplotlib.pyplot as plt

num_dict = {'one':1, 'peace':2, 'three':3, 'four':4, 'dislike':5, 'thumb_index':6, 'three2':7, 'stop_inverted':9, 'ok':10, 'no_gesture':'none'}

for cls in list(num_dict.keys()):
    print(cls, ':', len(os.listdir(f'./dataset/{cls}')))


# os.mkdir('./dataset/data_1000/none')

# for i in range(1, 11):
#     os.mkdir(f'./dataset/data_1000/{i}')

print(list(num_dict.keys()))

print(num_dict)

categories = list(num_dict.keys())

for i in range(0, len(categories)):

    category = categories[i]

    sampled_images = random.sample(os.listdir(f'./dataset/{category}'), 1000)

    for img in tqdm(sampled_images, desc = 'Copying'):
        src_path = f'./dataset/{category}/{img}'
        dest_path = f'./dataset/data_1000/{num_dict[category]}'
        shutil.copy2(src_path, dest_path)
