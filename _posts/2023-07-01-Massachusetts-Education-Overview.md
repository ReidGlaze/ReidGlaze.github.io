---
title: "Massachusetts Education Overview"
date: 2023-07-01 00:00:00 -0700
image: /assets/images/Massachusetts.png
categories: [DAA Bootcamp]
tags: [data analytics,tableau]     # TAG names should always be lowercase
---

Have you ever wondered what makes one school excel while another struggles? I looked into Massachusetts public schools' data, using the powerful visualization tool, Tableau, to answer this question. It allowed me to analyze and understand the complex patterns affecting educational performance. My insights are captured in an interactive dashboard, including a map of Massachusetts where each zip code is represented by a clickable region. Feel free to explore this dashboard by clicking on the image below to uncover the fascinating trends that affect this state's education system.


[![by origin](/assets/images/MassDashboard.png)](https://public.tableau.com/app/profile/reid.glaze/viz/Massachusetts_16880559956770/Dashboard?publish=yes)

## The Project

For this project, I will focus on trends in Massachusetts public schools using the ["Massachusetts Public Schools Data"](https://www.kaggle.com/datasets/ndalziel/massachusetts-public-schools-data) dataset from Kaggle. This dataset contains a range of information including student demographics, school performance, graduation rates, and college attendance statistics from 2017. The ultimate objective is to uncover patterns and discern which factors contribute most significantly to underperformance in Massachusetts educational institutions.

Some questions I will aim to answer:
* How does class size affect rates of college attendance?
* How does a school being economically disadvantaged affect college attendance?
* How does a school being economically disadvantaged affect graduation rates?
* How much do graduation rates vary from school to school?
* What kind of trends can be observed in primary education?

## Findings

The initial observation that grabbed my attention was an unexpected positive link between class size and college attendance rates. This was surprising, as I had always assumed smaller classes meant better outcomes. However, once a 4th degree polynomial regression line was applied to the scatter plot, the relationship was clear. Interestingly, this trend holds up until class sizes reach around 35 students. Although this needs more investigation due to limited data points for class sizes over 25, it's evident that classrooms with over 15 students perform significantly better than smaller ones.

The second finding was how economic disadvantage impacts college attendance. This was a less surprising but very significant trend. The percentage of college attendees among economically disadvantaged students varied greatly, ranging from as low as 10 percent to as high as 95 percent. Most high-performing outliers were charter schools, a fact revealed by Tableau's feature allowing for a closer look at individual data points. This significant difference in the impact of economic disadvantage on college attendance brings out the deep societal implications of these observations.
