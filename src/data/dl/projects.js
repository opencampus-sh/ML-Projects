import React from 'react';

const PROJECT_FOLDER = 'https://github.com/opencampus-sh/ML-Projects/blob/main/src/data/dl/code/';
const projects = [
  {
    title: 'Face Mask Recognition',
    imageUrl: 'img/placeholder_DL.png',
    semester: 'WiSe 20/21',
    students: 'Adnan Nooruddin, Ravish Kumar, Christoph Eberz, Bennet Möller',
    description: (
      <>
      This project develops a detection system which tells from a picture whether the person is wearing a mask or not.
      </>
    ),
    project_link: PROJECT_FOLDER + 'FaceMaskRecognition',
  },
  {
    title: 'Painting Classification',
    imageUrl: 'img/placeholder_DL.png',
    semester: 'WiSe 20/21',
    students: 'John Jay Kimani, Nils Berns',
    description: (
      <>
      Which artist painted this painting? Nils and John tried to answer this question using neural networks with different approaches, discover more in their presentation.
      </>
    ),
    project_link: PROJECT_FOLDER + 'PaintingClassification',
  },
  {
    title: 'Bike Sharing Prediction (SprottenFlotte)',
    imageUrl: 'img/placeholder_DL.png',
    semester: 'WiSe 20/21',
    students: 'Andrej Ponomarenko, Daniel Michells',
    description: (
      <>
      Analyzing the SprottenFlotte data from Kiel, can we predict where will the next bike be borrowed? <i><b>Note</b>: the data for this project is private and cannot be shared, only the results.</i>
      </>
    ),
    project_link: PROJECT_FOLDER + 'BikeSharingPrediction',
  },
  {
    title: 'Windfinder Predictions',
    imageUrl: 'img/placeholder_DL.png',
    semester: 'WiSe 20/21',
    students: 'Lennart Petersen',
    description: (
      <>
      Predicting the best spot for surfing is a hard task, yet Lennart gave it a great shot and developed a model to predict it with 86% of accuracy. <i><b>Note</b>: the data for this project is private and cannot be shared, only the results.</i>
      </>
    ),
    project_link: PROJECT_FOLDER + 'windfinderNN.ipynb',
  },
  {
    title: 'Image Segmentation',
    imageUrl: 'img/placeholder_DL.png',
    semester: 'WiSe 20/21',
    students: 'Yi-Jie Yang, Sebastian Koch, Erwin Smith, Suman Singha',
    description: (
      <>
      Segmentation is used to separate an object from the background.
      Using a U-Net the group was able to do some interesting work on a Kaggle Challenge.
      </>
    ),
    project_link: PROJECT_FOLDER + 'ImageSegmentation',
  },
  {
    title: 'COVID-19 Detection on X-Ray Image',
    imageUrl: 'img/placeholder_DL.png',
    semester: 'WiSe 20/21',
    students: 'Mithun Das, Mohammad Wasif Islam, Rakibuzzaman Mahmud, Sarker Miraz Mahfuz',
    description: (
      <>
      Can we detect COVID from an X-Ray image of the lungs?
      It turns out we can, or better, a software can do that for us.
      This project achieved an accuracy of 0.9896 on this task!
      </>
    ),
    project_link: PROJECT_FOLDER + 'COVID-19-Xray-Image-Classification',
  },
  {
    title: 'Disease Classification on Medical XRay Images',
    imageUrl: 'img/placeholder_DL.png',
    semester: 'WiSe 20/21',
    students: 'Sudesh Acharya',
    description: (
      <>
      Can a neural network distinguish different types of diseases just by looking at a single X-Ray image of the lungs?
      The project shows promising results in this direction.
      </>
    ),
    project_link: PROJECT_FOLDER + 'DiseaseClassificationXRay',
  },
];

export default projects;
