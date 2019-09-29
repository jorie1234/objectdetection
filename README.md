# Object detection with imageAI

Based on [imageAI](http://imageai.org/)

Import conda environment with

```conda env create -f environment.yml```

Download [YoloV3 Model](https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/yolo.h5)



## imageobjectdetection.py
Uses all ```*.jpg``` Files from the ```pictures``` directory and performes object detection on them. Saves the result in ```*_new.jpg``` in same folder

## videoobjectdetection.py
Uses Webcam to capture frames an then performs object detection. Shows result in a window.