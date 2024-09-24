import subprocess
import sys

# Mediapipe 라이브러리가 설치되어 있는지 확인
def install_package(package):
    try:
        __import__(package)
    except ImportError:
        print(f"{package} 라이브러리가 설치되어 있지 않습니다. 설치를 시작합니다...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        print('설치완료')