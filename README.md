# Object detection with imageAI

Based on [imageAI](http://imageai.org/)

Import conda environment with

```
conda env create -f environment.yml
```

If you encounter any problems during install with wrapt try the following:
```
conda update --all
conda remove wrapt
pip install tensorflow
```

If you get an error during execution like 
```
ImportError: numpy.core._multiarray_umath failed to import
```
try the following:
```
pip install -U numpy
```


Download [YoloV3 Model](https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/yolo.h5)

```
wget https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/yolo.h5
```


## imageobjectdetection.py
Uses all ```*.jpg``` Files from the ```pictures``` directory and performes object detection on them. Saves the result in ```*_new.jpg``` in same folder

## videoobjectdetection.py
Uses Webcam to capture frames an then performs object detection. Shows result in a window.