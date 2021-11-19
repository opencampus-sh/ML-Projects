---
marp: true
theme: gaia
size: 4:2
_class: lead
paginate: true
backgroundColor: lightgray
backgroundImage: url('https://marp.app/assets/hero-background.jpg')
---

# **Object Detection with YOLO** 

[[Project-Repo](https://github.com/Mnpr/Open-Detector)]

---

# :bookmark_tabs: **Contents**

- Objective
- Dataset
- Architectures
- Inference and Results
- Demonstration
- Conclusion and Future works

---

#  Objective

To Compose/Implement :

- `YOLOv3` & `YOLOv4` algorithm on `MS COCO` dataset
- Object Detection on Images
- Object Detection on Videos | Live-Cam
- Evaluation Metrics ( to Futureworks )


---

# Dataset 

 

**Microsoft COCO( Common Objects in Context ) Dataset 2017**


- $80$ Common Object Classes
- Pre-trained Darknet weights and configs
  - YOLOV4 [[ Weights ]](https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v3_optimal/yolov4.weights), [[ Configs ]](https://raw.githubusercontent.com/AlexeyAB/darknet/master/cfg/yolov4.cfg)
  - YOLOV3 [[ Weights ]](https://pjreddie.com/media/files/yolov3.weights), [[ Configs ]](https://raw.githubusercontent.com/AlexeyAB/darknet/master/cfg/yolov3.cfg)
- MS COCO  [[ Labels ]](https://github.com/Mnpr/Open-Detector/blob/main/dataset/coco.names)


---

# Architectures

**Model Architecture, Tech Stack**

- YoloV3,  (PyTorch | OpenCV)
- Yolov4, (OpenCV)
  
With Pretrained Darknet Backbone.

---
![bg 95%](../assets/v3.jpeg)

---
![bg 90%](../assets/v4.jpeg)

---

# **Results**

![bg right:60% 90%](../assets/img_inference.png)

- Boundary Box
- Confidence Score
- Image Inference [Pytorch]
- Video & Live-Cam Inference [OpenCV]

---

# Demo:

![bg 70%](../assets/live_demo.png)

---

# Conclusion and Future works

>> Understanding and Implementation of Object Detection


*Future Works*
1. Evaluation Metrics for different model comparison
2. Run on  CUDA GPU Build
3. Other Yolo Variants with Sensors fusion for 3D object detection.
---

# :books: References

**YOLO Algorithms**

- [[V4 Apr 2020](https://arxiv.org/pdf/2004.10934v1.pdf)],[[V3 Apr 2018](https://arxiv.org/pdf/1804.02767v1.pdf)],[[V2 Dec 2016](https://arxiv.org/pdf/1612.08242v1.pdf)], & [[V1 May 2016](https://arxiv.org/pdf/1506.02640v5.pdf)]

**Darknet Reference**

- [[ Weights, Darknet Script, Configs ]](https://github.com/AlexeyAB/darknet)

**Misc.**

- Image Yolo Architectures [[ V3 ]](http://media5.datahacker.rs/2019/11/11-1024x423.jpg), [[ V4 ]](https://www.programmersought.com/article/55924478253/)




