# Create a Customer Segmentation Report for Arvato Financial Solutions

This is the capstone project for the Udactity's Data Science Nanodegree. 

We want to identify new customers for the company making use of Unsupervised and Supervised Machine Learning Techniques.

## Libraries
- Numpy
- Pandas
- Sklearn
- Matplotlib
- Seaborn
- Datetime
- Time

## Files
- Arvato Project Workbook (2).ipynb : jupyter notebook with all the analysis.
- clean_df4.py : python script with the funtion used to clean the data.

## Data

The data and outline of this project was provided by Arvato Financial Solutions, a Bertelsmann subsidiary.

The data includes 4 files:

- Demographics data for customers of a mail-order sales company in Germany.
- Demographics information for the general population of Germany.
- Demographics information for targets of a marketing campaign for the company - Train Set
- Demographics information for targets of a marketing campaign for the company - Test Set

## Steps, Summary and Conclusions

1. Data Wrangling

This step includes: Identify NaNs, Delete columns and rows with a high percentege of NaNs, convert object columns to numeric
columns via mapping or hot-encoding, fill the NaNs with the mode by column, delete high correlated columns, scale the data. 
All these steps (except the scaling) are done by the funtion clean_data4 in clean_data4.py

2. Customer Segmentation Report

In this step we use unsupervised learning to analyze attributes of established customers and the general population in order 
to create customer segments. This step includes: Principal Component Analysis to reduce the dimensionality, analysis of 
different amount of clusters to stablish the more convenient, clustering with k-means of the population and customers data. 

In this step we can conclude that clients are people with high income, high social status, low mobility and a neighborhood 
with houses of 1-2 families.

3. Supervised Learning Model

Build a supervised machine learning model that predicts whether or not each individual will respond to the campaign. This 
step includes: fit different classificator models to test their performance, choose one of them to look for the best 
parameters and improve the model. 

I choosed the GradientBoostingClassifier model because gives the best metric in a reasonable time. We use the roc_auc as 
metric due to high imbalance in the data. After looking for the best parameters of the model I reached a roc_auc of !!!!!!
for the train data.


4. Kaggle Competition
We make predictions on the campaign data as part of a Kaggle Competition. 

## Blog Post

All the steps are explained with more detail in !!!!!!!!!!!!



## Acknowledgements
Udacity and Arvato Financial Solutions for the idea and the data













