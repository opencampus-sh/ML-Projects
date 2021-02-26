# Overview
This respository is used as the final project for the course "Deep Learning" on [opencampus](https://edu.opencampus.sh/) in the Winter semester 2020/21.

**Topic**: Image Segmentation<br>
**Details**: This project managed to finish the task of image segmentation of the Kaggle Challenge, [Carvana Image Masking Challenge](https://www.kaggle.com/c/carvana-image-masking-challenge/overview).
The idea came from the interests of knowing how to segment the object from the image.
The datasets from the Carvana Image Masking Challenge is based on high quality car photos and the backgrounds of the images usually contain similar colors as cars.<br>
**Goals**: Work through the challenge and get to understand how image segmentation works, to know what are the state-or-art methods using for image segmentation, and to fine tune the image segmentation method with the knowledge we have learned from the course.<br>
**Dream**: This project initially planned to finish the [Cloud Segmentation challenge on Kaggle](https://www.kaggle.com/sorour/95cloud-cloud-segmentation-on-satellite-images/version/1), but with the time limitation and busy schedules...

# Background Knowledge for Image Segmentation
* [Introduction to Image Segmentation](https://www.analyticsvidhya.com/blog/2019/04/introduction-image-segmentation-techniques-python/)
* [The Image Segmentation Tutorial on Colab](https://www.tensorflow.org/tutorials/images/segmentation)

# Possible datasets for image segmentation
1. Some challenges on Kaggle:
    - [38-Cloud: Cloud Segmentation in Satellite Images](https://www.kaggle.com/sorour/38cloud-cloud-segmentation-in-satellite-images)
    - [95-Cloud: Cloud Segmentation on Satellite Images](https://www.kaggle.com/sorour/95cloud-cloud-segmentation-on-satellite-images/version/1)
    - [Ships in Satellite Imagery](https://www.kaggle.com/rhammell/ships-in-satellite-imagery)
    - [Understanding Clouds from Satellite Images](https://www.kaggle.com/c/understanding_cloud_organization)
    - [Carvana Image Masking Challenge](https://www.kaggle.com/c/carvana-image-masking-challenge/overview)
2. The [GitHub Repository](https://github.com/chrieke/awesome-satellite-imagery-datasets) collecting some satellite imagery datasets:
3. [Image Segmentation tutorial](https://www.tensorflow.org/tutorials/images/segmentation) with [Oxford-IIIT Pet Dataset](https://www.robots.ox.ac.uk/%7Evgg/data/pets/)
4. Open Images 2019 - [Instance Segmentation](https://www.kaggle.com/c/open-images-2019-instance-segmentation/data)
5. [Segmentation evaluation database](http://www.wisdom.weizmann.ac.il/~vision/Seg_Evaluation_DB/index.html)
6. [A Large-scale Dataset for Instance Segmentation in Aerial Images](https://captain-whu.github.io/iSAID/dataset.html)

## Link the shared Google drive for dataset we used
- Google Drive: right click the shared folder and click on "Add a shortcut to Drive" to make sure you can easily reach the folder
- Instruction for loading data in Google drive to Google Colab
```
from google.colab import drive
drive.mount('/content/drive')
%cd /content/drive/MyDrive/DL_project/kaggle/data/
```

# Possible Algorithms
* U-Net
    - [Origin paper for U-Net](https://arxiv.org/abs/1505.04597)
    - [Introduction about U-Net](https://neurohive.io/en/popular-networks/u-net/)
* FractalNet
    - [Background Paper about FractalNet](https://arxiv.org/pdf/1605.07648.pdf)
    - [A Repository for FractalNet implementation in Keras](https://github.com/snf/keras-fractalnet/blob/master/src/fractalnet.py)
* Others:
  [A repository for Deep Segmentation with several CNNs for semantic segmentation (U-Net, SegNet, ResNet, FractalNet) using Keras](https://github.com/danielelic/deep-segmentation/blob/master/train_fractal_unet.py)

# Notes for some possible further applications
* [Optical flow](https://nanonets.com/blog/optical-flow/)
* [Using Machine Learning to “Nowcast” Precipitation in High Resolution](https://ai.googleblog.com/2020/01/using-machine-learning-to-nowcast.html)
* [A Neural Weather Model for Eight-Hour Precipitation Forecasting](https://ai.googleblog.com/2020/03/a-neural-weather-model-for-eight-hour.html)


# Notebooks
* Examples to work from: [DL_Images.ipynb](https://github.com/yej117/Cloud_Segmentation_Deep_Learning/blob/main/DL_Images.ipynb)
* Final Notebook: [Image_segmentation.ipynb](https://github.com/yej117/Image_Segmentation_Deep_Learning/blob/main/Image_segmentation.ipynb)

# Overview of the timeline for this project
**14th Dec. - 4th Jan.**: project choice, dataset pre-processing, maybe first simple model and objective <br>
**4th Jan.**: Peer review session, each group present their status to another group <br>
**4th Jan. - 25th Jan.**: Architecture, fine-tuning, preparation presentation <br>

## Before Peer Review on 4th Jan.
Main task:
Find an **_intermediate target_**. It sounds a bit too hard to reach the target of cloud segmentation in six weeks.
So before the peer review, we should _choose the dataset_ and _have objectives_.

1. Look into different training datasets
2. Try to train them with some exist networks (for example, revising the [Image Segmentation tutorial](https://www.tensorflow.org/tutorials/images/segmentation) to train the dataset you find)
3. List down your findings:
    - Datasets: What you find? How it works with the networks that you used? Any interesting notebooks you find? What might be the challenging part?
    - Possible networks: What kind of application the networks mostly used for? What are their architecture? Any explanation for them? (And feel free to upload the program you wrote, it would be nice for the other to test)
    - Any useful documents you think it might help our project
4. Have another discussion before 4th Jan.

## Before meeting with Luca on 18th Dec. 16:30
- All: Look into the [Image Segmentation tutorial](https://www.tensorflow.org/tutorials/images/segmentation) with [Oxford-IIIT Pet Dataset](https://www.robots.ox.ac.uk/~vgg/data/pets/)
- EJ: Check how to link Colab with GitHub repository
     * add file from github: simply click the [link](http://colab.research.google.com/github), check the buttom "Private Repositories einschließen", and select this repository
     * push the file to github: file > Save a copy in Github
- Sebastian: Meeting tools
- Suman: Look into the dataset from Kaggle and give a brief summary
- Erwin: Work through the dataset from Kaggle and the possible applications


# Requirements of the final project
Date: 18th Jan. 2021
Time: 10 minutes for presentation + 5 minutes for a round of questions

Presentation structure:
- [x] Group: who are inside the group
- [x] Project: short description of the project and the motivation behind
- [x] Tools (optional)
- [x] Architecture
- [x] Story (optional): attempts, failures, successes
- [x] Results
- [ ] Baselines - how to measure the performance? is it good enough?? compare to??
- [ ] Missing (optional) - is there something you missed to improve in the project?
- [ ] Future work (optional) - how to improve

* Sharing (optional) on the opencampus gitbook: Code, Data and Presentation
