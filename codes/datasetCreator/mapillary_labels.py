import json
import os


def getFilePath():
    file_path = os.path.dirname(__file__)

    return file_path[0].upper() + file_path[1:]

def UpperPath(path): #Upper folder of the argument "path"
    upper_path = os.path.dirname(path)

    return upper_path[0].upper() + upper_path[1:]

__path__ = getFilePath()    #Directory of the current file


polygons_path = (r"E:\Python_Projeler\ComputerVisionProjects\Car_Eyes\dataset\Mapillary\val\v2.0\polygons",
                 r"E:\Python_Projeler\ComputerVisionProjects\Car_Eyes\dataset\Mapillary\train\v2.0\polygons")

labels_path = (r"E:\Python_Projeler\ComputerVisionProjects\Car_Eyes\dataset\Mapillary_YOLO\val\labels",
               r"E:\Python_Projeler\ComputerVisionProjects\Car_Eyes\dataset\Mapillary_YOLO\train\labels")

images_path = (r"E:\Python_Projeler\ComputerVisionProjects\Car_Eyes\dataset\Mapillary_YOLO\val\images",
               r"E:\Python_Projeler\ComputerVisionProjects\Car_Eyes\dataset\Mapillary_YOLO\train\images")

#           all_classes = set()             I used this part to check every classes in mapillary dataset.




class_ids = {'road':0,
             'traffic_light':1,
             'traffic_sign':2,
             'vehicle':3,
             'person':4}

map_classes = {                                 # After checking everything on the mapillary dataset, I used ChatGPT to match all these. I really didn't want to lose time on matching these.
                                                # After a while (5 mins) I realised that I could've written a code that does this job too. traffic-light, traffic-sign ... THEY'RE ALREADY WRITTEN IN THE CLASS NAMES XD
    'construction--flat--road': 'road',
    'construction--flat--service-lane': 'road',
    'construction--flat--driveway': 'road',
    'construction--flat--parking': 'road',
    'construction--flat--parking-aisle': 'road',
   
    'object--traffic-light--general-upright': 'traffic_light',
    'object--traffic-light--general-horizontal': 'traffic_light',
    'object--traffic-light--general-single': 'traffic_light',
    'object--traffic-light--pedestrians': 'traffic_light',
    'object--traffic-light--cyclists': 'traffic_light',
    'object--traffic-light--other': 'traffic_light',
    
    'object--traffic-sign--front': 'traffic_sign',
    'object--traffic-sign--back': 'traffic_sign',
    'object--traffic-sign--temporary-front': 'traffic_sign',
    'object--traffic-sign--temporary-back': 'traffic_sign',
    'object--traffic-sign--direction-front': 'traffic_sign',
    'object--traffic-sign--direction-back': 'traffic_sign',
    'object--traffic-sign--information-parking': 'traffic_sign',
    'object--traffic-sign--information': 'traffic_sign',
   
    'object--vehicle--car': 'vehicle',
    'object--vehicle--bus': 'vehicle',
    'object--vehicle--truck': 'vehicle',
    'object--vehicle--motorcycle': 'vehicle',
    'object--vehicle--bicycle': 'vehicle',
    'object--vehicle--trailer': 'vehicle',
    'object--vehicle--other-vehicle': 'vehicle',
    'object--vehicle--caravan': 'vehicle',
    'object--vehicle--vehicle-group': 'vehicle',
    'object--vehicle--wheeled-slow': 'vehicle',
    'object--vehicle--on-rails': 'vehicle',
  
    'human--person--individual': 'person',
    'human--person--person-group': 'person',
    'human--rider--bicyclist': 'person',
    'human--rider--motorcyclist': 'person',
    'human--rider--other-rider': 'person',
}
 
def mapillary_to_yolo(polygons=polygons_path,labels=labels_path):

    for label_path,json_path in zip(labels_path,polygons_path):

        files = os.listdir(json_path)
        length = len(files)

        for index,polygon_file in enumerate(files):

            file_name = polygon_file.split('.')[-2]
            polygon_path = os.path.join(json_path, polygon_file)

            TXT_path = os.path.join(label_path, file_name+".txt")

            with open(polygon_path) as f:
                data = json.load(f)
            
            #print()
            height = data['height']
            width = data['width']
            TEXT = ""
            try:
                for item in data['objects']:
                    if item['label'] in map_classes:
                        
                        id = class_ids[map_classes[item['label']]]

                        line = f"{id} "

                        for coordinates in item['polygon']:
                            x = coordinates[0]/width
                            y = coordinates[1]/height
                            line += f"{x} {y} "

                        TEXT += line + "\n"

                        
                with open(TXT_path,'a+') as f:
                    f.write(TEXT)
                    
                print(f"{file_name}.txt is created {index + 1}/{length} ")
            except Exception as e:
                print(f"An error occured creating {file_name}.txt   Error: {e}")
        
def check_files(labels=labels_path,images=images_path):
    
    for label_path,image_path in zip(labels,images):
        for index,image in enumerate(os.listdir(image_path)):
            image_name = image.split('.')[-2]
            txt = image_name+".txt"
            
            if not txt in os.listdir(label_path):
                try:
                    with open(label_path+"\\"+txt):
                        pass
                    print(f"File {txt} is created at {label_path}\\{txt}")
                except Exception as e:
                    print(f"File couldn't have been created      Error: {e}")

mapillary_to_yolo()
check_files()






