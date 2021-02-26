import React from 'react';

const PROJECT_FOLDER = 'https://github.com/opencampus-sh/ML-Projects/blob/main/src/data/nlp/code/';
const projects = [
  {
    title: 'Study Recommender System with GPT-3',
    imageUrl: 'img/placeholder_NLP.png',
    semester: 'WiSe 20/21',
    students: 'Jan Peter Prigge, Jan Deller, Erwin Smith',
    description: (
      <>
      How can we choose the best study program for us when there are so many choices?
      Jan, Jan and Erwin built a system using state of the art technology to recommend you the best choice based on what you are looking for.
      </>
    ),
    project_link: PROJECT_FOLDER + '/StudyRecommendationGPT3/StudyRecommenderSystemwithGPT-3.pdf',
  },
  {
    title: 'Fine-tuning GPT-2',
    imageUrl: 'img/placeholder_NLP.png',
    semester: 'WiSe 20/21',
    students: 'Steffen Brandt, Steffen Pohle, Atul Kumar Yadav, Jonas Peltner, Nicolas Steen, Philipp Seeler',
    description: (
      <>
      description
      </>
    ),
    project_link: 'notyetavailable',
  },
];

export default projects;
