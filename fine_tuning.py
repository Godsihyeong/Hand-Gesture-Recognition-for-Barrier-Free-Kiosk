import os
import tensorflow as tf
assert tf.__version__.startswith('2')

from mediapipe_model_maker import gesture_recognizer

# fine_tuning
# fine_tuning
# fine_tuning

dataset_path = './dataset'
result_path = './result'

'''
[Explanation]
dataset_path directory : <dataset_path>/<label_name>/<img_name>
label_name : should include 'none' (1, 2, 3, 4, 5, 6, 7, 8, 9, 10 in this situation)
'''

data = gesture_recognizer.Dataset.from_folder(
    dirname=dataset_path,
    hparams=gesture_recognizer.HandDataPreprocessingParams()
)

# train test split

train_data, rest_data = data.split(0.8)
validation_data, test_data = rest_data.split(0.5)

# set parameters, options

hparams = gesture_recognizer.HParams(export_dir = result_path)
model_options = gesture_recognizer.ModelOptions(dropout_rate = 0.2)
options = gesture_recognizer.GestureRecognizerOptions(hparams=hparams, model_options=model_options)

'''
Args:
    <HParams>
        learning_rate, batch_size, epochs, shuffle, lr_decay
        steps_per_epoch : adjusting steps for each epoch
        gamma : Focal Loss parameter is made for solving imbalanced data problem
    <ModelOptions>
        dropout_rate : dropout ratio for each hidden layer
        layer_widths : customize hidden layer
            [128, 128, 128] -> make 3 hidden layer composing 128 neuron for each hidden layer

'''

# define model with parameters, options

model = gesture_recognizer.GestureRecognizer.create(
    train_data = train_data,
    validation_data = validation_data,
    options = options
)

# checking results

loss, acc = model.evaluate(test_data, batch_size = 1)
print(f'Test loss : {loss}, Test Accuracy : {acc}')

model.export_model()