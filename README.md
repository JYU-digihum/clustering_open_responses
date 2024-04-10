
# Clustering open responses in survey data

## Introduction

In this notebook we apply clustering to open-ended responses in survey data using Transformer modeling. The notebook is tailored to Finnish textual data.

[FSD3360 Helsingin Sanomat Loneliness Survey 2014](https://services.fsd.tuni.fi/catalogue/FSD3360?tab=description&lang=en&study_language=en) from the Finnish Social Data Archive is used as an example. The dataset is available for research, teaching and study.

The data includes the following open-ended question: "Miltä yksinäisyys tuntuu? Yksinäisyyteen liittyy usein voimakkaita tunteita, jotka ovat erilaisia eri elämäntilanteissa. Jos haluat, voit kertoa yksinäisyyskokemuksiasi tässä." (trans. "How does loneliness feel? Loneliness is often associated with strong emotions, which vary across different life situations. If you want, you can share your experiences of loneliness here.") 

In this notebook we will show how to:

    1. install and import necessary libraries,
    2. preprocess loneliness data,
    3. perform principal component analysis (PCA) for feature reduction,
    4. use elbow or silhouette method to determine an appropriate number of clusters,
    5. perform k-means clustering and visualize the results with t-distributed stochastic neighbor embedding (t-SNE),
    6. create wordclouds of clusters using lemmatized loneliness data.

The notebook can also be copied from [Colab](https://colab.research.google.com/drive/1v8UpvuwO_qoHG9upb3CrMzEMvZdgagvM) (File -> Save a copy in Drive).

## Running the example code

### Colab

1. Download the dataset from here: [FSD3360 Helsingin Sanomat Loneliness Survey 2014](https://services.fsd.tuni.fi/catalogue/FSD3360?tab=description&lang=en&study_language=en). Alternatively, you can use your own dataset (csv file).
2. Load the dataset and the list of stopwords (e.g., from [here](https://github.com/stopwords-iso/stopwords-fi)) to local memory in Colab (from the upper left column choose the last icon "Files" -> "Open"). 

### Locally

Pre-requisites:
- python 3.7
- jupyter notebook
 
Tested with the following versions of packages:
- python 3.7.9
- torch 1.7.1
- transformers 4.16.2
- sentence_transformers 2.3.1
- kneed 0.8.5
- kaleido 0.2.1

How to get started
1. Install [Turku Neural Parser](https://turkunlp.org/Turku-neural-parser-pipeline/) on your computer. 
2. Install [Jupyter Notebook](https://jupyter.org/install).
3. Clone the repository on the command line:
```{cmd}
git clone https://github.com/JYU-digihum/clustering_open_responses.git
```
Alternatively, you can download the repository as a zip file (in the repository click Code -> Download ZIP).

4. Run the notebook by starting Jupyter on the command line:
```{cmd}
jupyter notebook
```
5. Download the dataset from here: [FSD3360 Helsingin Sanomat Loneliness Survey 2014](https://services.fsd.tuni.fi/catalogue/FSD3360?tab=description&lang=en&study_language=en). Alternatively, you can use your own dataset (csv file). Also, download the list of stopwords (e.g., from [here](https://github.com/stopwords-iso/stopwords-fi)), and place these two files under the same directory as the notebook.

## TODO

- re-check libraries and their versions needed to run the code locally 
- input data in other format than csv (txt, tsv etc.)
- improve usability: create a zip file of all outputs, command line versions etc.
- having [Trankit](https://github.com/nlp-uoregon/trankit) as an alternative library to lemmatization (will provide you almost as good performance in lemmatization as Turku Neural Parser for Finnish text)

## Acknowledgements

This repository has been produced as part of the [FIN-CLARIAH ](https://www.jyu.fi/en/projects/fin-clariah) infrastructure project.

Reference:
```
Toivanen, I., Lampi, A., Sihto, T., Oinas, T. & Taipale, S. (2024). Vanhustyöntekijöiden teknologiaan liittämät tunteet – avovastausten analysoiminen tekoälypohjaisen klusteroinnin keinoin. Sosiaalilääketieteellinen aikakauslehti. In press.
```


