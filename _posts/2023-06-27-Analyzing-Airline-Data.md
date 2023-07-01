---
title: "Analyzing Airline Data"
date: 2023-06-27 00:00:00 -0700
image: https://media.licdn.com/dms/image/D5612AQGtS1pwY3xayw/article-cover_image-shrink_423_752/0/1687703011811?e=1693440000&v=beta&t=TDTAy-U5nitAYHm1g1pJqKlENluQI8nz_0Wd1mwDMCI
categories: [Grad School Projects]
tags: [data mining,flight data,data analytics,data science,machine learning,python]     # TAG names should always be lowercase
---


Flight cancellations and delays have significant implications for passengers and the airline industry, making it crucial to minimize these disruptions. They negatively impact customer satisfaction and can lead to financial losses for airlines. In 2022, the airline industry reported net losses of $6.9 billion. Minimizing disruptions enhances efficiency, protects the industry's reputation, and restores confidence among travelers.

## The Project

Big Thank you to Rohit Kharat and Mukund Kharat, whom I worked on this project with!
Our goal was to analyze a data from Jan 2022 to April 2022 and extract meaningful information from this data. For this project, we analyzed over 2 million flights. We set out to answer the following questions:
1. Which airports should be focused more on infrastructure development to mitigate the frequency and severity of delays?
2. What are the relationships between airline carriers and flight delays/cancellations?
3. What are the most common reasons for flight delays based on airports?
4. What are the relationships between days in a week or times in a day when there are a lot of cancellations and delays?

Additionally, we built a prediction model that could be used to calculate the arrival delay for a flight based on the other attributes. The customers and the airport authorities could directly use this. We also built several classification models to predict the reason for cancellations of flights based on the attributes provided by the dataset. For more information about the classification and prediction models, please see the full write-up at the bottom of the page.

## What we Learned

Some Interesting points that we took away from this project:
* Delays are most likely to occur at Atlanta, Dallas-Fort Worth, and Denver airports. They are most likely to occur in Texas, California, and Florida. Southwest Airlines has the most delays by a large margin.
* Frontier, JetBlue, and Allegiant airlines had the most delays over 30 minutes when analyzed as a percentage of total airline flights.
* The most common reason for a delayed flight was a Carrier Delay. This information varied depending on the airline.
* Cancellations are far more likely to happen between 4 and 5 am when compared to any other time in the day.
* Cancellations are more likely to occur between Wednesday and Saturday.
* Long delays are more likely to occur later in the day (after 3pm) or very early in the morning (before 4am).

## Tools Used

We used the "Airline Reporting Carrier On-Time Performance Dataset" by IBM. This entire dataset includes data on 194 million flights. We considered data from January 2022 to April 2022, using approximately 2 million samples, and analyzed delays and cancellations of these flights. During data pre-processing, we only extracted feature information that would be useful for answering our questions.
We used these libraries python:
* Numpy and Pandas for handling data
* Scipy and Scikit-Learn for statistics
* Matplotlib for visualization
* Keras and Tensorflow for machine learning

## The Data

Delay Incidents by Origin:
![by origin](https://media.licdn.com/dms/image/D5612AQFa9m5AfMNe-w/article-inline_image-shrink_1500_2232/0/1687706132667?e=1693440000&v=beta&t=6lK-tn7f6Oo0GnaxtVXkyV_RUgs8rzlsGKekyjUUvdA)
Delay Incidents by State:
![by state](https://media.licdn.com/dms/image/D5612AQEwZQwS321bew/article-inline_image-shrink_1500_2232/0/1687706161439?e=1693440000&v=beta&t=b8NDKjAJ1Qiv7WwPH9A0sv1RirBsu2utGOY0EVAxFGA)
Delay Incidents by Airline:
![by origin](https://media.licdn.com/dms/image/D5612AQGtdO1lmY-jGw/article-inline_image-shrink_1500_2232/0/1687706208704?e=1693440000&v=beta&t=IpUMGh2YklC9OSe7j8DCys-TZBztPgbd2gpcVBCw0G8)
Short Delays by Airline:
![short delays by airline](https://media.licdn.com/dms/image/D5612AQGkQ-2zo55baw/article-inline_image-shrink_1500_2232/0/1687706287918?e=1693440000&v=beta&t=KSUiSIzv2dnlvAVE1QE7Xw5o8upuVEnTYkYZuQUX_aA)
Medium Delays by Airline:
![medium delays by airline](https://media.licdn.com/dms/image/D5612AQF8JXUkpD3lTw/article-inline_image-shrink_1500_2232/0/1687706359058?e=1693440000&v=beta&t=Fpi0BkYe7EtibRTvlJdFJ1RbCLGy21soo5I_b02mCSM)
Long delays by Airline:
![long delays by airline](https://media.licdn.com/dms/image/D5612AQHg6QwOVR-HRA/article-inline_image-shrink_1500_2232/0/1687706381786?e=1693440000&v=beta&t=p5iG16TU3b9gb4NSfPOqDN87JQ9muD6BuZOv5fqtdtY)
Common Reasons for Delays:
![common reasons for delays](https://media.licdn.com/dms/image/D5612AQE3JTdfWxRffw/article-inline_image-shrink_1500_2232/0/1687706426472?e=1693440000&v=beta&t=0rz_YIfz2m3l4IaIfyUbgbGXvrPJT0eyKIpp-mdq-2A)
Common Reasons for Delays for different airlines:
![Common reasons for delays for different airlines](https://media.licdn.com/dms/image/D5612AQEBWrjfz7skMg/article-inline_image-shrink_1500_2232/0/1687706490431?e=1693440000&v=beta&t=s2SIOXPkAP_17C_bLknmBpUfLpV8hJrkoDaq0BedPOs)
Probability of Cancellation by the hour:
![prob of cancellation by hour](https://media.licdn.com/dms/image/D5612AQGRXAYBNiwqEw/article-inline_image-shrink_1500_2232/0/1687706539728?e=1693440000&v=beta&t=xaj6yNzQg5IJ8EtmBIyA6It3KAFMBHyoTjwOTxohihY)
Probability of short, medium, and long delays based on hour of the day"
![prob of short, medium, long delays by hour](https://media.licdn.com/dms/image/D5612AQF9avxJOw3QWQ/article-inline_image-shrink_1000_1488/0/1687706608585?e=1693440000&v=beta&t=CrJLBGvQsObO0GrzZynMAk1QvsGd4PBXpO3r7rp0HBQ)
Probability of Cancellation based off day of the week:
![prob cancellation based off day of week](https://media.licdn.com/dms/image/D5612AQGs2ecZaaoyhg/article-inline_image-shrink_1500_2232/0/1687706654161?e=1693440000&v=beta&t=rfvDDo8uZapB1RokM_LnzZzM5Oh1kMQG1CZlBPasm68)
Decision Tree Classifier for cancellation of flights:
![Decision tree classifier](https://media.licdn.com/dms/image/D5612AQF7Zi08LH9MlA/article-inline_image-shrink_1500_2232/0/1687707223937?e=1693440000&v=beta&t=h6lGurb27pJzz5uO2iEwPnsuTWyJwhN3IeDjH6XpO2c)

## Summary

For our first question, we found out which airports we should focus on infrastructure development concerning carrier and aircraft delays. This information will help us to mitigate the frequency and severity of delays for passengers. The solution for the second question was found by which airlines have the most percentage of their flights delayed during departure and arrival based on different delay times. For the third question, we found the most common reasons for delays in flights based on origin airports, origin state, and airlines. The analysis was done to find the top 10 candidates which cause the delay in flights, so that information will help make informed decisions about which airlines and airports should be preferred. For our last question, we determined which times are optimal for consumers to purchase a flight to minimize the probability of delays.
We tried to build two types of prediction models. The first one was a Multiple Linear Regression model and the second one was a Neural Network. We concluded that the neural network was much better at predicting flight delays and the predicted values were much closer to the actual values. These predictions could be further improved with additional data and a more complex model. Neural networks did the best task in prediction of flight delays with mean absolute difference value of 14.7.
Multi-classification models were built to classify or predict the reason for cancellations. The models which we built for this task were decision tree, random forest, AdaBoost classifier, extra trees classifier, gradient boosting classifier, XGBoost, Naive Bayes, and logistic regression. Among these models, we got the highest classification metrics values for the random forest classifier, followed by the extra trees classifier. We got highest classification metrics (accuracy, precision, recall, F1 score) of 0.84 from random forest classifier.

## Application

Our project can help with a lot of real-world applications. Our findings related to the delay in flights because of airports will help the airports with poor performance improve their services. Having good performance would also help these airports in terms of business as the airlines and the passengers would prefer more to travel via these airports.
The results where we see the airline carrier performance in terms of delays will force the poor performing airlines to improve their services otherwise it would have a big impact on their business. These results also help the passengers to select better and more reliable flights.
We have also done an analysis of the reasons for delays at each airport which again would help the airport authorities to see what could be done to have better flight operations.
Our detailed analysis of delays based on the day of the week or time in a day would be more helpful to the customers when they are booking flights, as they can update their travel plans while considering the possibility of delays.
The classification model will serve the purpose of providing the reason for the cancellation of a flight to the airport authorities. This information can be shared by the authorities with the customer and can make an informed decision about the flight. This will also help in diverting a flight to a safer airport based on weather, national security, or any other issues. This knowledge will lead to help the airport as well as airline authorities to prevent losses incurred due to the cancellation of flights. Also, the customer will be provided with prior updates on the flight status.
The prediction model although not extremely efficient, gives decent predictions about the delays. Our experiments show how neural networks can be used in a more efficient way to make a very efficient and reliable delay predictor which could be eventually incorporated into airports’ and airlines’ websites and mobile applications. This would make it very helpful for the customers to chart out their travel plans with consideration of flight delays.

## [Link to Video Demonstration](https://drive.google.com/file/d/1tFNXBeGWgvO279kmX0j8H3mXri9UwV8C/view?usp=sharing)

## [Link to Our Final Project Paper](https://drive.google.com/file/d/1-1LUKGP2DKAdC8t3_b0wWjrclRyfEODE/view?usp=sharing)

## [Link to Github](https://github.com/ReidGlaze/DM-Project/blob/main/09_MiningForAirlinesOnTimeDataset_Part5.ipynb)