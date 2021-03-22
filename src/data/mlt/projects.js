import React from 'react';

const PROJECT_FOLDER = 'https://github.com/opencampus-sh/ML-Projects/blob/main/src/data/mlt/code/';
const projects = [
  {
    title: 'Iceberg and Ship Detection in Radar Satellite Imagery',
    imageUrl: 'img/mlt/Ship_Iceberg_ClassificationProject.PNG',
    semester: 'WiSe 20/21',
    students: 'Eike Schütt, Yi-Jie',
    description: (
      <>
      This project is aimed at building an algorithm able to detector for SAR imagery which finds and classifies ships, icebergs or unidentified objects.
      </>
    ),
    project_link: PROJECT_FOLDER + 'Ship_Iceberg_Classification.ipynb',
  },
  {
    title: 'Classification of illustrations in historic monographies',
    imageUrl: 'img/mlt/Historic_illustrationProject.PNG',
    semester: 'WiSe 20/21',
    students: 'Irena Kampa',
    description: (
      <>
      Digitalizing old collections makes them available to a worldwide public.
      This project trains a CNN to identify illustrations in monographies from the 15th to the 18th century.
      </>
    ),
    project_link: PROJECT_FOLDER + 'Historic_illustration.ipynb',
  },
  {
    title: 'Writing System Recognition',
    imageUrl: 'img/mlt/ScriptRecongitionProject.PNG',
    semester: 'WiSe 20/21',
    students: 'Manpreet Singh, Adnan Nooruddin, Rahima Akter, Sebastian Koch',
    description: (
      <>
      Can we detect different language from an image?
      Here a classifier which is able to distinguish Latin, Chines, Kyrillic and Georgian!
      </>
    ),
    project_link: PROJECT_FOLDER + 'ScriptRecongition',
  },
  {
    title: 'Designing Airfoils',
    imageUrl: 'img/mlt/AirfoilsDesignProject.png',
    semester: 'WiSe 20/21',
    students: 'Nils Berns, Violetta Germann',
    description: (
      <>
      Airfoils usually are designed using complex differential equations.
      Can we feed a NN with a set of 2D outline of airfoil profiles and let it learn?
      </>
    ),
    project_link: PROJECT_FOLDER + 'AirfoilsDesign/AirfoilDesign_presentation_final.ipynb',
  },
  {
    title: 'Music genre classification task',
    imageUrl: 'img/mlt/MusicalGenreClassificationProject.PNG',
    semester: 'WiSe 20/21',
    students: 'Rakibuzzaman Mahmud, Sarker Miraz Mahfuz, Mohammad Wasif Islam',
    description: (
      <>
      Have ever had a discussion with your friends about the genre of a song?
      Here the solution: a neural network to automatically classify musical genre!
      </>
    ),
    project_link: PROJECT_FOLDER + 'MusicalGenreClassification',
  },
  {
    title: 'Network traffic prediction',
    imageUrl: 'img/mlt/NetworkTrafficPredictionProject.PNG',
    semester: 'WiSe 20/21',
    students: 'Mithra Gholami',
    description: (
      <>
      Internet traffic accounts for huge quantities of data, yet sometimes it's hard to make sense of them.
      This project aims at classifying network traffic using passive measurements of TCP connections.
      </>
    ),
    project_link: PROJECT_FOLDER + 'NetworkTrafficPrediction.ipynb',
  },
  {
    title: 'Predicting Bakery Turnover using AR-Net',
    imageUrl: 'img/mlt/Predict-Bakery-Turnover-using-AR-Net-mainProject.PNG',
    semester: 'WiSe 20/21',
    students: 'Ravish Kumar, Modeus Abdelnaby',
    description: (
      <>
      How accurately can we predict the bakery turnover?
      This group got an auto-regressive neural network on this task!
      </>
    ),
    project_link: PROJECT_FOLDER + 'Predict-Bakery-Turnover-using-AR-Net-main/Predicting_Bakery_Turnover_AR-Net_Modelling-HyperparameterSearch.ipynb',
  },
  {
    title: 'stock market news analysis by NLP',
    imageUrl: 'img/mlt/News4MarketPredictionProject.PNG',
    semester: 'WiSe 20/21',
    students: 'Andrej Ponomarenko, Monfrared Gharibi Foorogh',
    description: (
      <>
      Are daily news correlated with the stock market?
      Can we use them to predict the market behaviour?
      Here some interesting attempts!
      </>
    ),
    project_link: PROJECT_FOLDER + 'News4MarketPrediction.ipynb',
  },
  {
    title: 'Using containership positions (AIS) to predict export statistics',
    imageUrl: 'img/mlt/AIS_predictionProject.PNG',
    semester: 'WiSe 20/21',
    students: 'Jakob Stender, Steffen Gans',
    description: (
      <>
      The project worked on training a nueral network for the prediction of unilateral export statistics using Neuralnet and AIS-Containership data
      </>
    ),
    project_link: PROJECT_FOLDER + 'AIS_prediction',
  },
  {
    title: 'Voice Detection (Classify Human based on Voice)',
    imageUrl: 'img/mlt/voicedetection.jpg',
    semester: 'WiSe 20/21',
    students: 'Mutasim Fuad, Mithun Das, Rajib Chandra Das',
    description: (
      <>
      This group focused on voice detection and human classification based on the voice.
      </>
    ),
    project_link: PROJECT_FOLDER + 'VoiceDetection.ipynb',
  },

];

export default projects;
