# Machine Learning with Tensorflow Automated Essay Scoring submission

The project has been challenging and it was an interesting way to dive into NLP.


# Discussion of the results

We focused on one attribute from the study rating whether the mail written by the azubis was polite or impolite. Due to privacy reasons we cannot provide the data.

## Transfer Model BERT
Having a look into the data. For some sentences it is at the very least questionable if they are labeled correctly by the scorer. For some sentences model and human scorer have the same opinion, for others they are different and it is not always completely clear to us, why the data has been labelled Polite or Impolite by the scorer. Hence the accuracy of the model is also affected by the initial labelling.

It is though not easy to find a measurable baseline for the scores, as there is a rather large grey zone for polite and impolite answers. It is not fully clear, why the mail 118 is considered impolite by the scorer, while mail 391 and 416 are considered polite. There would be arguments for each mail in both directions. In this regard maybe the models can help to develop a standard that follows measurable rules and is not subject to human error.

## word2vec
Several problems might be implemented in this approach:

* maybe our dataset is to small to create our own embeddings
* maybe we made some major fails when creating embeddings or the model
* its definitely overfitting

## Primitive approaches
Primitive models like e.g. SVM performed suprisingly well on the data. It is not yet clear for us, why this is the case, but it should not be neglected to use such approaches when there is little data available.


There is absolutely no warranty for the provided code.
