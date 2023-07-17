---
title: "Pedal Prophets: Harnessing ML, Python, and SQL to Forecast Seoul's Bike Rentals"
date: 2023-07-16 00:00:00 -0700
image: /assets/images/bikecanva.png
categories: [Grad School Projects]
tags: [data analytics,sql,python,data science,machine learning]     # TAG names should always be lowercase
---

This data science project centered around predicting bike rental demand, a pivotal component of urban life, using a dataset sourced from Seoul, South Korea. Initially, during a class taught by Dr. David Quigley, I used Python as my primary tool for data cleaning and feature engineering.

Recently, after acquiring SQL skills, I decided to revisit the project. The goal was to identify hidden patterns and create accurate prediction models using both SQL for data querying and manipulation, and Python for data exploration, preprocessing, and feature engineering. Together with machine learning techniques, I was able to generate precise forecasts and gain a deeper understanding of the bike rental dynamics in Seoul.

This endeavor represents a fusion of my earlier work and new skills, leveraging the synergy of SQL and Python to improve data management efficiency and uncover more profound insights from the Seoul-based dataset, which could potentially shift our understanding of urban transportation dynamics.

## Dataset
This data was originally taken from Kaggle, available [here](https://www.kaggle.com/datasets/saurabhshahane/seoul-bike-sharing-demand-prediction). For this specific assignment, I was given a variation of this dataset. I was given [XTrain](https://github.com/ReidGlaze/Machine_Learning/blob/main/Homework%204/XTrain.csv), [yTrain](https://github.com/ReidGlaze/Machine_Learning/blob/main/Homework%204/yTrain.csv), and [XTest](https://github.com/ReidGlaze/Machine_Learning/blob/main/Homework%204/XTest.csv) csv files. yTest was not given. Instead, the predicted values were submitted to Kaggle and an accuracy score was returned. 

## Tools Used
* Azure Data Studio - This was used to write T-SQL scripts and to write Python in Jupyter Notebooks.
* Microsoft Azure Portal - This was used to host the Server and Database. It includes $200 of free credits for new users.
* Pyodbc Library - This was used to connect the server to Python and use the SQL queries inside of Jupyter.

## Unsuccessful Methods
* SQLite - This is great for using SQL and Python together. However, it does not allow you to format features as dates. It worked, but it would not have been a good example for this project.
* MYSQL - I had trouble using the import wizard. I prefer the one on Azure Data Studio.
* Hosting Locally on Azure Data Studio - I am able to host a server locally through Docker. However, I was unsuccessful when trying to connect it with myodbc. I have a newer Mac that uses an ARM processor, so this may have complicated things.

## The Query

If you look at the [XTrain](https://github.com/ReidGlaze/Machine_Learning/blob/main/Homework%204/XTrain.csv) data, you will see the data in the format that it was given. The date was given in the MM/DD/YYYY format. The following query was used to convert the column to the datetime format. The "103" key was used for this specific starting format. Furthermore, DATEPART was used to find out the specific day of the week and the month for each date. CASE was used to determine if that day was a weekend or not. These are all important features that can predict the number of bike rentals on a given day. Trivial features were excluded from the query.

![by origin](/assets/images/Xtrain_query.png){: width="700" }

The output of this query is shown below.

![by origin](/assets/images/Xtrain_query_output.png)

XTest can be queried in a similar fashion.

## Using a SQL Query in Jupyter Notebook
After the server was created in [MS Azure](https://portal.azure.com/), the following code was ran in Jupyter to connect the server. Of course, if you wish to replicate this, you will need to enter custom information about your server. Using MS Azure, this information can be found by clicking on your database and then clicking "connection strings" in the menu on the left.

![by origin](/assets/images/pyodbc.png){: width="700" }

Next, the output of queries were converted into pandas dataframes. The queries for XTrain, XTest, and yTrain are shown below. As you can see, there is some code used to filter out a warning. This warning suggested using SQLAlchemy. However, using pyodbc didn't cause any problems for me so I chose to ignore it.

![by origin](/assets/images/query_jupyter.png)

Printing Xtrain.head() in a new cell resulted in a dataframe that looked identical to the one queried earlier in SQL. This meant that my connection was succesful and I could move on to feature engineering and model building. How exciting!

![by origin](/assets/images/query_output.png)


