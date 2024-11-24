# Hand-Gesture-Recognition-for-Barrier-Free-Kiosk

This is a fine-tuned hand gesture recognition model designed to classify numerical sign language gestures for barrier-free kiosks.

<img src="https://drive.google.com/uc?id=17s2qO8fjcgugYAGDBUMjvp1vRjYufQdP" alt="Hand Gesture Recognition Demo" width="350">

The model is highly effective, achieving an average confidence of 90%, an average inference time of 76.92 milliseconds, and a compact model size of 8.1 MB. It is specifically designed for resource-constrained environments, such as kiosks and other embedded systems, making it ideal for scenarios requiring high accuracy and fast inference speed within limited computing resources.

## Overview

<img src="https://drive.google.com/uc?id=1iBLdht_pAQ1tcWYiX-xX1QeEjkx7XxXD" alt="Model Overview">

Using Google's MediaPipe hand gesture recognition model, the model was trained and fine-tuned to recognize Korean Sign Language numbers.

## Installation
Clone this project:
```bash
git clone https://github.com/Godsihyeong/Hand-Gesture-Recognition-for-Barrier-Free-Kiosk.git
```

Using `pip` and `requirements.txt`:
```bash
pip install -r requirements.txt
```

Using `conda` and `environment.yaml`:
```bash
conda env craete -f environment.yaml
```

## Run Model with Webcam.py
You can run the fine-tuned model and test it using your laptop's webcam by executing the webcam.py script.
This script utilizes the fine-tuned hand gesture recognition model and displays the predictions in real time.

**Instructions:**
1. Ensure that your environment is set up and all dependencies are installed.
2. Run the following command in your terminal:
```
python webcam.py
```
3. The webcam feed will open, and the model's predictions for hand gestures will be displayed.

## License
This project is licensed under the Apache License 2.0. See the [LICENSE](LICENSE) file for details.
