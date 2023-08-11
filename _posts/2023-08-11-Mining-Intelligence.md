---
title: "Mining Intelligence - Time-Based Analysis and Predictive Modeling"
date: 2023-08-11 00:00:00 -0700
image: 
categories: [DAA Bootcamp]
tags: [python, data analytics, sql, data science]     # TAG names should always be lowercase
---

#This page is currently under construction. Please check out my other projects or come back again later!
---

## Introduction

This report focuses on analyzing a dataset related to the mining process. The primary objectives are understanding patterns in the mining process over time and building a predictive model for `% Iron Concentrate` and `% Silica Concentrate`.

---

## Time-Based Data Analysis

### Data Loading and Preprocessing
The dataset was read from a CSV file, which contains various parameters of the mining process. Special emphasis was placed on the 'date' column, extracting features such as the hour of the day, day of the week, month, and a weekend indicator.

### Visualizations
Multiple visualizations were generated to understand the patterns in `% Silica` and `% Iron` concentrates based on different time granularities such as hour of the day and day of the week. The visuals provide insights into how the concentrations change over time.


---

## Predictive Modeling

### Data Preparation
Data was split into features (`X`) and targets (`y`), where the targets are `% Iron Concentrate` and `% Silica Concentrate`. An 80-20 split was used to separate the data into training and test sets.

### Model Selection and Training
A `RandomForestRegressor` was chosen to predict the two targets. The model was trained on the training data to capture patterns in the input features that influence the concentrations.

### Model Evaluation
The model's predictions on the test set were evaluated using the Mean Squared Error (MSE) and \( R^2 \) score for both targets. These metrics provide a quantitative measure of the model's accuracy and fit.

*(Note: Precise evaluation metrics are not provided in this summary, but they can be referenced from the notebook's execution results)*

---

## Conclusion
The analysis provides valuable insights into how `% Iron` and `% Silica` concentrations vary over time. The machine learning model offers a mechanism to predict these concentrations based on input features, which can be beneficial for process optimization in the mining industry.
