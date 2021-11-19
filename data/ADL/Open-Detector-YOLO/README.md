This repository contains Projectwork :arrow_down: undertaken for the partial fulfillment of Advanced Deep Learning Module ( SS2021 ) and ETCS Creditpoints @OpenCampus.sh.

# Open-Detector

**Objective :** Object Detection with YOLO[v3/v4], using OpenCV and PyTorch

## :beginner: Index

1. Datasets

2. Implementation

3. References

## :diamond_shape_with_a_dot_inside: 1. Dataset

- MSCOCO 2017 Dataset [[ Pretrained YOLO with Darknet Backend ](https://github.com/AlexeyAB/darknet)]

## :computer: 2. Implementaition

**Status /Progress**

- [x] Implementation-OpenCV ( Video/Cam ) [CPU]
    - [x] YOLOv3 pre-trained inference on video/webcam
    - [x] YOLOv4 pre-trained inference on video/webcam
- [x] Implementation PyTorch ( images ) [GPU]
- [x] Modularization
- [x] Final Presentation

## :bookmark_tabs: 3. References

- [1. ] YOLO Versions : [[Scaled-v4 Feb 2021](https://arxiv.org/pdf/2011.08036.pdf)], [[V4 Apr 2020](https://arxiv.org/pdf/2004.10934v1.pdf)], [[V3 Apr 2018](https://arxiv.org/pdf/1804.02767v1.pdf)], [[V2 Dec 2016](https://arxiv.org/pdf/1612.08242v1.pdf)], & [[V1 May 2016](https://arxiv.org/pdf/1506.02640v5.pdf)]
- [2. ] AlexeyAB/Darknet [[ Weights and Configs]](https://github.com/AlexeyAB/darknet)


***
**Reproduction Instructions:**
- Download and put yolov3 and v4 weights and configs inside `./Open-Detector/`
  - `configs/`
    - `yolov3.cfg`
    - `yolov4.cfg`
  - `weights`
    - `yolov3.weights`
    - `yolov4.weights`
- Sample video under `./io/sample.jpg` | `./io/sample.mp4` | [0,1,2, etc. for `live_cam`]
- Install dependencies `pip install -r requirements.txt`
- Run `python main.py` providing `input_type` = 'image' | 'video' | 'live'
***
