# Research Report
# Nucleus segmentation via artificial neural network
 
 Dear reader,
 
 please use this GitHub repository to get access to our research project “NUciSeg - U-Net Optimierung für die Segmentierung von Zellkernkonglomeraten” which was realized within the course “Machine Learning für die Medizin” by opencampus sh. 
 
 In order to use the provided notebooks, please download the master branch (https://github.com/REDortmund/Nucleus) or use this data bundle. In the next step you need to upload the whole folder into your personal Google Drive account. From there you can execute the notebooks via Google Colab.

 Herein we provide two notebooks: NUciSeg_Final.ipynb will help you to understand the data-structure and gives insights into our working-process, where we evaluated different models and training-approaches. The conclusions we draw from this notebook led us to the design of our final model, which we present together with the according results in the notebook Final_Model.ipynb

# Project description
 In the context of microscopy cell imaging analyses, the identification of a cell nuclei is often described as a critical step. Recent developments in Deep Learning have optimized this operation compared to previous rule-based algorithms.   

 A common machine learning based method for solving such a task is called "image segmentation". This approach is characterized by learning the relationships between the searched categories and the corresponding pixel values in the context of a supervised learning. To implement such a procedure, annotated images in the form of segmentation masks are typically required. In this project we segment cell nuclei cluster and separate them from each other. 

 The dataset we used in this project is based on nuclei pictures which were coloured with DAPI and the outer borders from overlapping cell nuclei clusters were marked. For solving the segmentation task we will use a U-Net based architecture and a pretrained ResNet.

##Github repository
 In order to demonstrate image segmentation methods in the context of microscopy cell images our project uses a dataset from Kaggle (URL: https://www.kaggle.com/gnovis/nucleus). The dataset will also be available in the corresponding GitHub repository of this project. Your supervisor will give you the access to this repository. Please load from there all your files into to your personal Google Drive to use this notebook properly.

> **Context**\
 The dataset was created in the context of a master thesis for solving microscope image segmentation by means of machine learning methods. Further information regards this document can find here: https://github.com/gnovis/nucleus.

> **Content**\
 The dataset consists of cell nuclei clusters with marked borders (incomplete) and cluster border masks. The data were used to train NN to predict full cell borders to separate cells from each other. 

> **Acknowledgements**\
 Microscope images of cell nuclei used for dataset creation was obtained from Martin Mistrik research group from Institute of Molecular and Translational Medicine (IMTM).



# Content of NUciSeg_Final.ipynb

 In this notebook different architectures of convolutional neural networks will be presented and discussed to solve the given image segmentation problem. In this context different approaches were implemented to handle the input data for these CNNs. Furthermore, different loss functions and metrices will be discussed within the research scope.

 The whole data set and all the trained models are available in different ZIP file in our GitHub repository. After uploading these files into a virtual machine of Google Colad you can use the provided code chunks to just load the weights instead of executing the training for each model.


## Chapter 1 - Exploratory Data Analysis

## Chapter 2 - Zero Padded Images 
- **First initial Model**

- **U-Net**
  - **Adjustment of the Metric and the Loss**

- **ResNet50 - transfer learning**


## Chapter 3 - Handling of the Input Data 

- **Adjustment of the Ground Truth**

- **Image Generator**

Next to this document we provide a separate Notebook which offers you a compact script to execute our recommended model within a suitable setting.   


# Content of Final_Model.ipynb

 This notebook is representing the final model for our research project in the field of Nucleus Segmentation. 

 For further illustrations of each code chunck please take a closer look into our detailed project documentary in the notebook "NUciSeg Final.ipy".

# Outlook for further projects...

 We were able to create a model that is able to fulfill the task of image segmentation with the underlying dataset. However there is always room for improvement...

- Try and adjust our model on other data or maybe the adjusted mask-pictures: The images we trained our model on are already edited and pre-processed... Since the borders of the nuclei have already been marked, our model might depend very much on this markings. Especially when we trained our models for fewer epochs we saw that it relied heavily on these markings, since it tried to predict some lines whenever there were some deepenings, indentation or irregularities in the shape of the pre-drawn boundaries of the nuclei. This might also relate to the poor quality of the dataset. We observed that for several pictures, the segementation-lines of the ground-truth pictures were drawn quite straight, without accounting for the actual round shape of the nuclei. Therefore this could be a source confusion in the training-process for our model... Maybe the model would perform better on datasets with betterprepared mask-pictures. You could also try to train the model on the "raw" images without any markings. For example we edited our mask-pictures to exclude the outer boundary-lines... you could follow a similar approach for the training-images see how well the model can be trained when no lines are given at all. This would also yield more realistic data for such a segmentation task on microscopic images.

- Play with the hyper-parameters: In this project we focused mainly on finding an appropriate metric and the right loss-function. However there are still parameters that can be optimized - Play around with different optimizers, learning-rates, batch-sizes and so on... Additionally maybe trying to combine different loss-functions can improve the training-process?

- The performance of the transfer learning could be increased by adding more convolutional layers in at the end of the upsampling model, so the number of featurmaps can be decreased in more steps not like now from 170 to 1.

- Using less layers from the ResNet50, because it could help to have more general features with than more spatial information then features with high information but less spatial information. The information in the features increases with the deeped of the neural network.

- Chance the input in the ResNet50 from the copy of the same channel to zero padded channels. Or try too use the data pipeline from the ResNet50 or other approaches

- Use another pretrained model from keras or from a paper