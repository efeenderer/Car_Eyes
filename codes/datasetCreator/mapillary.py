import os
import shutil


def getFilePath():
    file_path = os.path.dirname(__file__)

    return file_path[0].upper() + file_path[1:]

def UpperPath(path): #Upper folder of the argument "path"
    upper_path = os.path.dirname(path)

    return upper_path[0].upper() + upper_path[1:]

__path__ = getFilePath()    #Directory of the current file


s_path = r"E:\Python_Projeler\ComputerVisionProjects\Car_Eyes\dataset\BDD100K\bdd100k\images\100k\val"
d_path = r"E:\Python_Projeler\ComputerVisionProjects\Car_Eyes\dataset\BDD100K_YOLO\val\images"


i = 0
for images in os.listdir(s_path):
    if images[-3:] == "jpg" or images[-3:] == "png" :
        try:
            s = s_path + "\\" +images 
            shutil.move(s,d_path)
            print(f"{images} is moved")
        except Exception as e:
            print(f"{images} couldn't have been moved   Error:{e}")
    else:
        for image in  os.listdir(s_path + "\\"+images):
            try:
                s = s_path + "\\"+ images + "\\" +image
                shutil.move(s,d_path)
                print(f"{images}\\{image} is moved")
            except:
                print(f"{image} couldn't have been moved   Error:{e}")