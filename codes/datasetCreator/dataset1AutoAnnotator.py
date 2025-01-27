import os
import shutil
import random
import numpy as np
import csv

def getFilePath():
    file_path = os.path.dirname(__file__)

    return file_path[0].upper() + file_path[1:]

def UpperPath(path): #Upper folder of the argument "path"
    upper_path = os.path.dirname(path)

    return upper_path[0].upper() + upper_path[1:]

__path__ = getFilePath()    #Directory of the current file

csv_path = os.path.join(UpperPath(UpperPath(__path__)), r"dataset\dataset1\train_solution_bounding_boxes.csv")

images_path = os.path.join(UpperPath(UpperPath(__path__)), r"dataset\dataset1\train\images")
labels_path = os.path.join(UpperPath(UpperPath(__path__)), r"dataset\dataset1\train\labels")


with open(csv_path,"r") as file:
    reader = csv.reader(file)
    i = 0
    for label in os.listdir(labels_path):
        label_path = os.path.join(labels_path,label)
        os.remove(label_path)
    for row in reader:
        if i < 1:
            i = i + 1 
            continue
        image_file = row[0]
        x1,y1,x2,y2 = (float(row[1])/676, float(row[2])/380, float(row[3])/676, float(row[4])/380,)
        
        #print(f"{image_file}")
        #print(f"{x1},{y1},{x2},{y2}")
        image_name = image_file.split(".")[-2]

        center_x = (x1+x2)/2
        center_y = (y1+y2)/2
        height = y2-y1
        width = x2-x1

        os.path.join(labels_path,f"{image_name}"+".txt")
        try:            
            with open(os.path.join(labels_path,f"{image_name}"+".txt"),"a+") as label:
                TEXT = f"0 {center_x} {center_y} {height} {width}\n"
                label.write(TEXT)
                print(f"File created {image_name}.txt")
        except Exception as e:
            print(f"There was an error creating the label file: {image_name}.txt Error:{e}")












