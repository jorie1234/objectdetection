from imageai.Detection import ObjectDetection
import os
import glob

execution_path = os.getcwd()

detector = ObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath( os.path.join(execution_path , "yolo.h5"))
detector.loadModel()


files = glob.glob("pictures/*[0-9].jpg")

for f in files:
    newFile=os.path.join(execution_path , f.replace(".jpg", "_new.jpg"))
    print("File: ", f)
    
    if os.path.isfile(newFile)==True:
        continue
    detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path , f), output_image_path=newFile, minimum_percentage_probability=30)

    for eachObject in detections:
        print(eachObject["name"] , " : ", eachObject["percentage_probability"], " : ", eachObject["box_points"] )
        print("--------------------------------")
