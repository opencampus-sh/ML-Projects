import React from 'react';

const PROJECT_FOLDER = 'https://github.com/opencampus-sh/ML-Projects/blob/main/src/data/nlp/code/';
const projects = [
  {
    title: 'Study Recommender System with GPT-3',
    imageUrl: 'img/nlp/StudyRecommendationGPT3Project.PNG',
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
    imageUrl: 'img/nlp/gpt-2.png',
    semester: 'WiSe 20/21',
    students: 'Steffen Brandt, Steffen Pohle, Atul Kumar Yadav, Jonas Peltner, Nicolas Steen, Philipp Seeler',
    description: (
      <>
      Can GPT-2 be fine-tuned to achieve GPT-3 like accuracies?
      The project fine-tuned different models and compared them on different tasks.
      </>
    ),
    project_link: 'https://github.com/steffen74/GPT-2',
  },
];

export default projects;
