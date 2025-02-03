import threading
import queue
import cv2
import numpy as np
import time as t
from ultralytics import YOLO
import mss
import os
import torch 



def getFilePath():
    file_path = os.path.dirname(__file__)

    return file_path[0].upper() + file_path[1:]

def UpperPath(path):
    upper_path = os.path.dirname(path)

    return upper_path[0].upper() + upper_path[1:]

__path__ = getFilePath()



def detection(sct,monitor):
    try:
        screenshot = np.array(sct.grab(monitor))
        frame = np.array(screenshot)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        results = eyes(frame)
        result = results[0].plot(font_size=5)
        return cv2.cvtColor(result, cv2.COLOR_RGB2BGR)

    except Exception as e:
        print(f"Error in detection: {e}")
        return None



def processImage():
    sct = mss.mss()
    monitor = {"top": 100, "left": 100, "width": 1000, "height": 600}

    while True:
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        try:
            detect = detection(sct, monitor)
            return detect

        except Exception as e:
            print(f"Error in main loop: {e}")

def display_window():
    cv2.namedWindow("Car Eyes", cv2.WINDOW_NORMAL)
    blank_image = np.zeros((480, 640, 3), np.uint8)
    while True:
        frame = processImage()
        cv2.imshow("Car Eyes", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cv2.destroyAllWindows()

if __name__ == "__main__":
    if torch.cuda.is_available():
        eyes = YOLO(r"E:\Python_Projeler\ComputerVisionProjects\runs\detect\train\weights\best.pt").to('cuda')
    else:
        eyes = YOLO(r"E:\Python_Projeler\ComputerVisionProjects\runs\detect\train\weights\best.pt")
    
    display_window()



cv2.destroyAllWindows()
del eyes

