import json
import os

def getFilePath():
    file_path = os.path.dirname(__file__)

    return file_path[0].upper() + file_path[1:]

def UpperPath(path): #Upper folder of the argument "path"
    upper_path = os.path.dirname(path)

    return upper_path[0].upper() + upper_path[1:]

__path__ = getFilePath()    #Directory of the current file

classes_in_BDD = set()


def bdd_to_yolo(json_path, label_path=None):
    
    with open(json_path) as f:
        data = json.load(f)

    

    if not os.path.exists(label_path):
        os.makedirs(label_path)
    
    map_classes = {'traffic light': 'traffic_light',  # There were many classes in BDD100K dataset. I had to classify them.
                   'traffic sign': 'traffic_sign',    # At the end of this code, I created a set that checks all the classes in the BDD100K labels. And then I matched them to my classes:
                                                      #                                                                               0-Traffic Light, 1-Traffic Sign, 2-Vehicle, 3-Person
                   'drivable area': 'road',
                   'lane':'road',

                   'bus':'vehicle',
                   'motor':'vehicle',
                   'train':'vehicle',
                   'car':'vehicle',
                   'bike':'vehicle',
                   'truck':'vehicle',
                   
                   'person':'person',
                   'rider':'person',
                   }
    
    class_ids = {'road':0,
                 'traffic_light':1,
                 'traffic_sign':2,
                 'vehicle':3,
                 'person':4}
    
    for index,item in enumerate(data):
        img_name = str(item['name'])
        txt_file = img_name.split(".")[-2] + ".txt"
        txt_path =  os.path.join(label_path,txt_file)
        if not os.path.exists(txt_path):
            os.path.join(label_path,txt_file)
        
        with open(txt_path, 'w+') as f:

            for label in item['labels']:

                classes_in_BDD.add(label['category'])

                category = label['category']

                if category in map_classes:

                    id = class_ids[map_classes[category]]

                    if 'box2d' in label:
                        x1, y1 = label['box2d']['x1'], label['box2d']['y1']
                        x2, y2 = label['box2d']['x2'], label['box2d']['y2']
                        
                        x_center = (x1 + x2) / (2 * 1280) # images in BDD100K are all 1280x720
                        y_center = (y1 + y2) / (2 * 720)
                        width = (x2 - x1) / 1280
                        height = (y2 - y1) / 720
                        TEXT = f"{id} {x_center} {y_center} {width} {height}"
                        

                    elif 'poly2d' in label:
                        vertices = label['poly2d'][0]['vertices']
                        TEXT = f"{id} "
                        for coordinates in vertices:
                            x, y = coordinates[0], coordinates[1]
                            #print(f"{x} {y} ")
                            x = x/1280
                            y = y/720
                            
                            TEXT = TEXT + f"{x} {y} "

                    f.write(TEXT+"\n")
        print(f"label {txt_file} is done.     {index}/{len(data)}")

    
json_path = r"E:\Python_Projeler\ComputerVisionProjects\Car_Eyes\dataset\BDD100K\bdd100k_labels_release\bdd100k\labels\bdd100k_labels_images_train.json"
labels_path = r"E:\Python_Projeler\ComputerVisionProjects\Car_Eyes\dataset\BDD100K_YOLO\train\labels"


bdd_to_yolo(json_path,labels_path)

for sinif in classes_in_BDD: #Here I check all the classes in BDD100K to match those with mines later.
    print(sinif)





