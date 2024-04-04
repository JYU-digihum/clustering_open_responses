
# Clustering open responses in survey data

## Introduction

In this notebook we apply clustering to open responses in survey data with the help of Transformer modeling. The notebook is tailored to Finnish text data.

[FSD3360 Helsingin Sanomat Loneliness Survey 2014](https://services.fsd.tuni.fi/catalogue/FSD3360?tab=description&lang=en&study_language=en) from the Finnish Social Data Archive is used as an example. The dataset is available for research, teaching and study.

The data includes the following open-ended question: "Miltä yksinäisyys tuntuu? Yksinäisyyteen liittyy usein voimakkaita tunteita, jotka ovat erilaisia eri elämäntilanteissa. Jos haluat, voit kertoa yksinäisyyskokemuksiasi tässä."

In this notebook we
    1. install and import necessary libraries,
    2. preprocess loneliness data,
    3. perform principal component analysis (PCA) for feature reduction,
    4. use elbow or silhouette method for determining an appropriate amount of clusters,
    5. perform k-means clustering and visualize the results with t-distributed stochastic neighbor embedding (t-SNE),
    6. make wordclouds of clusters using lemmatized loneliness data.

The notebook can also be copied from [Colab](https://colab.research.google.com/drive/1v8UpvuwO_qoHG9upb3CrMzEMvZdgagvM) (File -> Save a copy in Drive).

## Running the example code

### Colab

1. Download the dataset from here: [FSD3360 Helsingin Sanomat Loneliness Survey 2014](https://services.fsd.tuni.fi/catalogue/FSD3360?tab=description&lang=en&study_language=en). Alternatively, use your own dataset (csv file).
2. Load the dataset, the script for lemmatization (lemmatization.py) and list of stopwords (for example from [here](https://github.com/stopwords-iso/stopwords-fi)).

### Locally

Pre-requisites:
- python 3.7 (tested with 3.7.9)
- torch 1.7.1
- transformers 4.16.2
- sentence_transformers 2.3.1
- kneed 0.8.5
- kaleido 0.2.1

How to get started
1. Install [Turku Neural Parser](https://turkunlp.org/Turku-neural-parser-pipeline/) to your computer.
2. Install [Jupyter notebook](https://jupyter.org/install).
3. Run the notebook by starting jupyter on the command line:
```{cmd}
jupyter notebook
```
4. Download the dataset from here: [FSD3360 Helsingin Sanomat Loneliness Survey 2014](https://services.fsd.tuni.fi/catalogue/FSD3360?tab=description&lang=en&study_language=en). Alternatively, use your own dataset (csv file).

## Acknowledgements

This repository has been produced as part of the infrastructure project [FIN-CLARIAH ](https://www.jyu.fi/en/projects/fin-clariah).

Reference:
```
Toivanen, I., Lampi, A., Sihto, T., Oinas, T. & Taipale, S. (2024). Vanhustyöntekijöiden teknologiaan liittämät tunteet – avovastausten analysoiminen tekoälypohjaisen klusteroinnin keinoin. In press.
```
