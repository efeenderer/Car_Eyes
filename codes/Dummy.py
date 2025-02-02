

path1 = r"E:\Python_Projeler\ComputerVisionProjects\Car_Eyes\dataset\MainDataset\val\images"

path2 = r"E:\Python_Projeler\ComputerVisionProjects\Car_Eyes\dataset\MainDataset\val\labels"


import os
import cv2 as cv

counter = 0

labels = os.listdir(path2)

names = set()

for image in os.listdir(path1):
    image_txt_name = image.split(".")[-2] + ".txt"
    image_txt_path = os.path.join(path2,image_txt_name)
    image_path = os.path.join(path1,image)

    if not image_txt_name in labels:
        counter += 1
        with open(image_txt_path,'w'):
            pass
        print(image_txt_path)

        