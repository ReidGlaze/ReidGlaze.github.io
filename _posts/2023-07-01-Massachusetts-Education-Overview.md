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

![by origin](/assets/images/ClassSize.png)

A key trend visible in the data is the variation in graduation rates among Massachusetts high schools. Despite Massachusetts being renowned for its high-quality public education, the schools with the lowest 10 graduation rates all sit below 20 percent. By interacting with the bar graph on the Tableau dashboard, you'll notice that most of these underperforming schools serve a high proportion of economically disadvantaged students. In stark contrast, the top 10 schools, all boasting a flawless graduation rate of 100 percent, serve far fewer students from disadvantaged backgrounds. This clear divergence shines a light on the educational disparities that exist even within one of the nation's leading public school systems.

![by origin](/assets/images/BottomTop.png)

Let's focus on one particular measure that underscores an area for potential enhancement in Massachusetts public schools. The rise of tech jobs and their promise of social mobility underscore the importance of early education, particularly in areas like mathematics. These formative years lay the groundwork for lifelong learning habits. For this analysis, I'll concentrate on 4th grade math MCAS scores. The visuals below spotlight school districts falling below the 50th percentile, as marked by the dividing line. If you interact with these schools on the Tableau dashboard, you can see the proportion of economically disadvantaged students in these districts. It's a revealing glance into how economic disparities can intersect with academic performance, even from a young age.
