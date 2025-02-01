import os 
import shutil


sources = [r"E:\Python_Projeler\ComputerVisionProjects\Car_Eyes\dataset\Mapillary_YOLO",
           r"E:\Python_Projeler\ComputerVisionProjects\Car_Eyes\dataset\BDD100K_YOLO"]

directory = r"E:\Python_Projeler\ComputerVisionProjects\Car_Eyes\dataset\MainDataset"



def carrier(sources=sources,directory=directory):
    for s in sources:
        
        for folder in os.listdir(s):

            folder_path = os.path.join(s,folder)
            
            print(folder_path)
            try:
                shutil.move(folder_path,directory)
            except Exception as e:
                print(f"Error occured at {folder}        Error: {e}")


carrier()