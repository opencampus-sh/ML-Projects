import os
import sys
import time
import torch
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# Import local Modules

from yolo_opencv import get_prediction

from yolo_torch.darknet import Darknet
from utils.torch_utils import boxes_iou, nms, detect_objects, print_objects, load_class_names, plot_boxes


# Parameters
CONFIDENCE = 0.5
THRESHOLD_SCORE = 0.5
THRESHOLD_IOU = 0.4

# Model Configuration
CONFIG_PATH = 'configs/yolov4.cfg'
WEIGHT_PATH = 'weights/yolov4.weights'

# Miscellaneous
CUDA = False
WRITE_OUTPUT = False
SHOW_DISPLAY = True

# Input / Output 
INPUT = 'io/sample3.mp4' # 'io/sample.mp4' # 2 #(external-livecam))
OUTPUT = 'io/yolo_output.avi'

# Frameworks ( OpenCV(v3/v4) | PyTorch(v3) )
input_type = 'video' # | 'video' | 'live' [ 0 or 1 or 2]

# later function + yolov3 inference [ todo ] 
if input_type == 'image':

    # Read Dataset Labels
    labels_file = 'dataset/coco.names'
    
    # Model ( Pytorch )
    model = Darknet(CONFIG_PATH)
    model.load_weights(WEIGHT_PATH)
    model.print_network()

    class_names = load_class_names(labels_file)

    original_image = cv.imread(INPUT)
    original_image = cv.cvtColor(original_image, cv.COLOR_BGR2RGB)

    image = cv.resize(original_image, (model.width, model.height))

    # detect the objects
    boxes = detect_objects( model, image, THRESHOLD_IOU, THRESHOLD_SCORE )

    # plot the image with the bounding boxes and corresponding object class labels
    plot_boxes(original_image, boxes, class_names, plot_labels=True)

# later function / class
elif input_type == 'video' or input_type =='live':  
    
    with open('dataset/coco.names', "r", encoding="utf-8" ) as f:
        LABELS = f.read().strip().split("\n")

    # Random Labels Color
    COLOR = np.random.randint(0, 255, size=(len(LABELS),3), dtype='uint8')

    # BBOX , Class Overlay Info
    FONT_SCALE = 2
    THICKNESS = 2

    net = cv.dnn.readNetFromDarknet(CONFIG_PATH, WEIGHT_PATH)

    if CUDA: 
        net.setPreferableBackend(cv.dnn.DNN_BACKEND_CUDA)
        net.setPreferableTarget(cv.dnn.DNN_TARGET_CUDA)

    get_prediction.get_video_inference(
        net,
        INPUT,
        OUTPUT,
        CONFIDENCE,
        THRESHOLD_IOU,
        WRITE_OUTPUT,
        SHOW_DISPLAY,
        LABELS
    )

else:
    print('please provide a valid framework_name ')
