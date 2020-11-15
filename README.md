# Sentiment Analysis with IMDB Dataset 

![Status badge](https://img.shields.io/badge/Status-Archived-important)

**Natural Language Processing**

`Sentiment analysis` aims to determine the attitude of a speaker, writer, or other subject with respect to some topic or the overall contextual polarity or emotional reaction to a document, interaction, or event. The attitude may be a judgment or evaluation (see appraisal theory), affective state (that is to say, the emotional state of the author or speaker), or the intended emotional communication (that is to say, the emotional effect intended by the author or interlocutor).This is a basic form of Natural Language Processing (NLP) called Sentiment Analysis in which we will try and classify a movie review as either positive or negative. In this project, a sentiment classifier is built which evaluates the polarity of a piece of text being either positive or negative. This project is aims to perform sentiment analysis on IMDB dataset.

### Getting the Dataset

The "Large Movie Review Dataset" shall be used for this project. The dataset is compiled from a collection of 50,000 reviews from IMDB on the condition there are no more than 30 reviews per movie. The numbers of positive and negative reviews are equal. Negative reviews have scores less or equal than 4 out of 10 while a positive review have score greater or equal than 7 out of 10. Neutral reviews are not included. The 50,000 reviews are divided evenly into the training and test set. 
The Training Dataset used is stored in the zipped folder: aclImbdb.tar file. This can also be downloaded from: http://ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz. 

### Requirements

Code was tested with Python 3.8.3.
- `Dependencies/Packages`:
	- Keras 2.x
	- matplotlib
	- seaborn
	- numpy
	- pandas
	- scikit-learn
	- NLTK
	- nlpprepcrocess
	- Jupyter Notebook

You can install above packages by the following command:
`pip install [package-name] --user`

### Steps to follow

- Data preprocessing
	- Tokenization
	- Stopwords removal
	- Stemming/Lemmatization
- Unigram/bigram
- Tf-Idf Vecotization
- Reduce Dimension
- Feed to model
- Test model
- Measure Accuracy, F1 Score, Precision Recall

### Results

| Model | Accuracy | F1 Score | Precision | Recall |
| --- | --- | --- | --- | --- |
| MLP | 86.36 | - | - | - |
| Logistic Regression | 86.54 | - | - | - |
| SVM | 86.59 | - | - | - |