# Code Repository for "[Identifying Radical Social Media Posts using Machine Learning](https://www.researchgate.net/publication/333853105)"

Radicalization (like cyberterrorism) is one of the major concerns to all governments and law enforcement agencies to provide safety and security to their citizens. A lot of radical groups, extremists and insurgent organizations use social media platforms such as Facebook, Twitter, Reddit, YouTube etc. to post their ideology and propagate their message to their followers. Manual detection of these posts is nearly an impossible task. We propose an automated system for extracting data from Twitter employing investigative data mining technique using the hashtags used in the posts. The system preprocesses the data to clean it by tokenizing, stemming and lemmatization. Data is classified as radical or non­radical using supervised machine learning classification techniques (Naive Bayes, SVM, AdaBoost and Random Forest) with varying parameters. The idea is to classify posts by identifying the linguistic structure, their stylometry and detecting a time based pattern.

+ Dataset Link: https://github.com/prabhakar267/radicalization-TT-dataset
+ Paper Link: https://www.researchgate.net/publication/333853105

## Citing Work
```
@preprint{prabhakarRadicalPaper2017,
author = {Gupta, Prabhakar and Varshney, Pulkit and P S Bhatia, M},
year = {2017},
month = {06},
pages = {},
title = {Identifying Radical Social Media Posts using Machine Learning},
doi = {10.13140/RG.2.2.15311.53926}
}
```

## Running Code
Requires Python2.7 to run locally. See [instructions](https://www.python.org/downloads) to setup Python2.7.
+ Clone the project from source
```shell
git clone https://github.com/prabhakar267/radical-social-media-post-classification && cd radical-social-media-post-classification
```
+ Setup virtual environment
```shell
pip install virtualenv
virtualenv venv --python=python2.7
source venv/bin/activate
```
+ Install all dependencies
```shell
pip install -r requirements.txt
```
+ Run each script
