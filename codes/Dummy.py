









path1 = r"E:\Python_Projeler\ComputerVisionProjects\Car_Eyes\dataset\BDD100K_YOLO\train\images"

path2 = r"E:\Python_Projeler\ComputerVisionProjects\Car_Eyes\dataset\BDD100K_YOLO\train\labels"

error = r"E:\Python_Projeler\ComputerVisionProjects\Car_Eyes\dataset\BDD100K_YOLO\train\errorcheck.txt"


import os

labels = os.listdir(path2)
i = 1
for image in os.listdir(path1):
    image_name = image.split('.')[-2]
    txt = image_name+".txt"
    if not txt in labels:
        try:
            os.remove(path1 + "\\" +image)
            print(f"Removed {image}     {i}/137")
            i = i + 1
        except Exception as e:
            print(f"There was an error deleting file:{image}     Error:{e}")