## Data Analysis

### Exam Scores<br>
This dataset has the marks by students in various subjects (math, reading, writing) and also other data about the students such as their gender, ethnicity, and type of lunch. You can perform some analysis and get the average score per gender, find out whether a student passed/failed an exam, and more.

Dataset:  https://www.kaggle.com/datasets/spscientist/students-performance-in-exams

Tutorial: https://towardsdatascience.com/a-complete-yet-simple-guide-to-move-from-excel-to-python-d664e5683039

### Pokemon Dataset<br>
This dataset has stats of 721 pokemon. You’ll find their type, HP, attack, special attack, special defense, and speed. You can play with this data and do some analysis to, say, find the pokemon with the highest attack and defense.
If you’re new to Pandas, I highly recommend you learn the basics with this dataset by watching the tutorial below.

Dataset: https://www.kaggle.com/datasets/abcsds/pokemon

Tutorial: https://youtu.be/vmEHCJofslg

### Netflix movies and TV shows

This dataset has all the movies and TV shows available on Netflix as of mid-2021. There you can find data such as the title, director, rating, release year, and duration. There is missing data and some columns need some cleaning before working with them in a project.

Dataset: https://www.kaggle.com/datasets/shivamb/netflix-shows

Tutorial: https://towardsdatascience.com/a-straightforward-guide-to-cleaning-and-preparing-data-in-python-8c82f209ae33

## Data Visualization
You can use these datasets to create visualizations. To do so, you can use matplotlib, seaborn, and even pandas.

### FIFA 22 player dataset
This dataset contains football player data for the video game FIFA. Data such as date of birth, height, weight, and overall rating can be found here.
The coolest thing is that on the website, there isn’t only the players’ data for 2022, but from 2016 to 2022, so you can compare the evolution of ratings in each player using line plots and other visualizations.

Dataset: https://www.kaggle.com/datasets/stefanoleone992/fifa-22-complete-player-dataset

Tutorial: https://towardsdatascience.com/a-simple-guide-to-beautiful-visualizations-in-python-f564e6b9d392

### Population dataset (1955–2020)
This dataset contains the population every 5 years from 1955 to 2020 for most countries around the world. The dataset has 3 columns: country, year, and population. The data is good to make simple visualizations such as piecharts, bar plots, boxplots, and histograms.

Dataset: https://drive.google.com/file/d/1QpCcE4U8NIhznbqf0kdeO2ITKPEs9OSm/view

Tutorial: https://towardsdatascience.com/the-easiest-way-to-make-beautiful-interactive-visualizations-with-pandas-cdf6d5e91757

### The Simpsons / Avatar The Last Airbender

Why not have fun while learning how to make visualizations? There are free datasets of TV shows such as The Simpsons and Avatar The Last Airbender on Kaggle. There you’ll find all the episodes and scripts, so you can make visualizations to show who has the highest number of lines, who speaks to whom, make a wordcloud, and plot sentiment analysis.

Dataset: The Simpsons - https://github.com/areevesman/the-simpsons/tree/master/data<br>
Avatar - https://www.kaggle.com/datasets/ekrembayar/avatar-the-last-air-bender 

Tutorial: The Simpsons meets Data Visualization - https://medium.com/towards-data-science/the-simpsons-meets-data-visualization-ef8ef0819d13 <br>
Data Visualization in Python with Avatar The Last Airbender - https://towardsdatascience.com/avatar-meets-data-visualization-60631f86ba7d

## Automation 
Instead of repeating tasks like creating Excel reporting, you can automate them with Python.

### Supermarket sales
Most of us once in our life had to create an Excel report using a sales dataset. Why not automate it? This dataset contains historical sales of a supermarket company for 3 months of data. You can use this data to create a pivot table and barplot in Excel using Python behind scenes.

Dataset: https://www.kaggle.com/datasets/aungpyaeap/supermarket-sales<br>
Tutorial: https://towardsdatascience.com/a-simple-guide-to-automate-your-excel-reporting-with-python-9d35f143ef7

## Regression Analysis

### Boston House Prices
This is a popular dataset for making linear regression. The dataset contains information about houses in Boston such as the per capita crime rate by town, average number of rooms per dwelling, full-value property tax rate per $10,000, and more.

Dataset: <br>
from sklearn.datasets import load_boston<br>
boston_dataset = load_boston()<br>

Tutorial: https://towardsdatascience.com/a-simple-guide-to-linear-regression-using-python-7050e8c751c1

## Text Classification

If you’re into NLP (Natural language processing), you’ll love these datasets. To work with them you have to use libraries such as sklearn, NLTK, gensim, spaCy, etc

### IMDB Dataset — Sentiment Analysis
This dataset contains 50k movie reviews with their sentiment (positive/negative). This data is great for building a model that classifies whether a text is positive or negative. This is known as binary text classification.

Dataset: https://www.kaggle.com/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews

Tutorial: https://towardsdatascience.com/a-beginners-guide-to-text-classification-with-scikit-learn-632357e16f3a

### 60k Stack Overflow Questions with Quality Rating

This dataset contains 60k Stack Overflow questions from 2016 to 2020. There are 3 types of questions: HQ (high-quality posts without a single edit), LQ_EDIT (low-quality posts with a negative score, and multiple community edits), and LQ_CLOSE (Low-quality posts that were closed by the community without a single edit).
You can use this dataset to predict tags for a question. This is more challenging than the previous project since there are not only 2 but multiple options for a tag. In this case, you have to use a multilabel classification approach.

Dataset: https://www.kaggle.com/datasets/imoore/60k-stack-overflow-questions-with-quality-rate

Tutorial:https://github.com/hse-aml/natural-language-processing/blob/master/week1/week1-MultilabelClassification.ipynb

## Image Classification
Unlike the other datasets listed in this article, these contain mostly images that you can use to build a classification model. To do so, you have to use Tensor Flow, Open CV, etc.

### Rock Paper Scissors

If you like the rock paper scissors game, you won’t get bored with this dataset. This dataset contains 2892 images of different hands in rock/paper/scissors poses.
This is commonly used for image classification (as shown in the tutorial below), but you can use this dataset for other purposes.

Dataset: https://www.kaggle.com/datasets/sanikamal/rock-paper-scissors-dataset

Tutorial: https://medium.com/geekculture/rock-paper-scissors-image-classification-using-cnn-eefe4569b415

## Face Mask Detection

This dataset consists of 1,376 images. In 690 images people are wearing face masks, while in 686 images people are not wearing a mask.
You can use this dataset to build a model that detects whether a person is wearing a face mask. By the end of the project, you can pick up a face mask and use your computers’ camera to test it yourself.

Dataset: https://github.com/prajnasb/observations/tree/master/experiements

Tutorial: https://towardsdatascience.com/covid-19-face-mask-detection-using-tensorflow-and-opencv-702dd833515b

## Recommender System

Have you ever wondered how companies like Netflix and YouTube recommend movies and videos? You can use the dataset below to build your own recommender system and understand how this works.

### MovieLens 20M Dataset — Movie Recommendation
This dataset contains 20 million ratings and 465,000 tag applications applied to 27,000 movies by 138,000 users. Perfect for those who want to build their movie recommendation system from scratch.

Dataset: https://grouplens.org/datasets/movielens/

Tutorial: https://www.datacamp.com/community/tutorials/recommender-systems-python


Dataset: 
Tutorial:


Dataset: 
Tutorial: