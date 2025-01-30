import os
import shutil

def getFilePath():
    file_path = os.path.dirname(__file__)

    return file_path[0].upper() + file_path[1:]

def UpperPath(path): #Upper folder of the argument "path"
    upper_path = os.path.dirname(path)

    return upper_path[0].upper() + upper_path[1:]

__path__ = getFilePath()    #Directory of the current file


##Important Paths

tt100k_path = os.path.join(UpperPath(UpperPath(__path__)), r"dataset\tt100k_2021")
tt100k_train = os.path.join(tt100k_path,"train")
tt100k_test = os.path.join(tt100k_path,"test")



tt100k_annotations =  os.path.join(tt100k_path, "annotations_all.json")


if not os.path.exists(UpperPath(UpperPath(__path__))+r"\dataset\tt100k_2021_YOLO\train\images"):
    os.makedirs(UpperPath(UpperPath(__path__))+r"\dataset\tt100k_2021_YOLO\train\images")
if not os.path.exists(UpperPath(UpperPath(__path__))+r"\dataset\tt100k_2021_YOLO\val\images"):
    os.makedirs(UpperPath(UpperPath(__path__))+r"\dataset\tt100k_2021_YOLO\val\images")

for img_train in os.listdir(tt100k_train):

    d_train = os.path.join(UpperPath(UpperPath(__path__)),r"dataset\tt100k_2021_YOLO\train\images")

    s_train = os.path.join(tt100k_path,"train",img_train)

    try:
        if not os.path.exists(d_train + f"\\{img_train}"):
            shutil.move(s_train,d_train)
            print(f"{img_train} has been moved to {d_train}")
        else:
            print("Image has already been moved")
    except Exception as e:
        print(f"Error during moving {img_train} Error: {e}")

for img_test in os.listdir(tt100k_test):

    d_test = os.path.join(UpperPath(UpperPath(__path__)),r"dataset\tt100k_2021_YOLO\val\images")

    s_test = os.path.join(tt100k_path,"test",img_test)  

    try:
        if not os.path.exists(d_test + f"\\{img_test}"):
            shutil.move(s_test,d_test)
            print(f"{img_test} has been moved to {d_test}")
        else:
            print("Image has already been moved")
    except Exception as e:
        print(f"Error during moving {img_test} Error: {e}")
    







