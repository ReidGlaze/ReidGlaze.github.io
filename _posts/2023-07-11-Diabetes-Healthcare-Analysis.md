---
title: "Data Driven Diabetics: An SQL Approach to Healthcare Analysis"
date: 2023-07-11 00:00:00 -0700
image: 
categories: [DAA Bootcamp]
tags: [data analytics,sql]     # TAG names should always be lowercase
---

Efficiency and patient turnover are key aspects of hospital management, and one crucial indicator of these is the length of stay (LOS) for each hospital visit. LOS can be influenced by a range of variables, from patient demographics to the complexity of their medical condition. Gaining a deep understanding of these factors can lead to strategies that enhance hospital efficiency and improve patient care.

In this article, we harness the power of Structured Query Language (SQL) to delve into healthcare data and examine the different variables influencing hospital LOS. Our objective is to offer valuable insights that can assist healthcare professionals and policymakers in making data-driven decisions to enhance hospital operations. Join us as we navigate through this dataset to explore what truly impacts the duration of patients' hospital stays.

## The Project

### Query 1
The healthcare data analysis team lead is keen to explore the distribution of the length of hospital stays measured in days. They are particularly interested in determining whether the majority of patients have a length of stay less than 7 days. It's crucial for the hospital to confirm that any patients with stays exceeding this duration are indeed in need of acute care.

Although SQL isn't traditionally associated with data visualization, an innovative approach has been implemented for some initial exploratory data analysis. This method exploits SQL's calculation functions and uses rudimentary histogram bars for data visualization. In other words, the heavy lifting of number crunching is done by SQL, and basic text characters are utilized to visually represent the data.

![by origin](/assets/images/time_in_hospital_1.png)
![by origin](/assets/images/time_in_hospital_2.png)

### Query 2
The hospital's new Director seeks to understand which medical specialties are performing the highest average number of procedures. They're interested in a comprehensive list of specialties, each with their average procedure count. The Director requested specialties with an average procedure count exceeding 2.5 and a total procedure count surpassing 50.

To meet this requirement, an additional column was added to display the AVG number of procedures per specialty, grouped accordingly with the GROUP BY function. Furthermore, the ORDER BY function was used to sort these groups in descending order by average number of procedures. However, some specialties showed rounded averages, potentially due to low patient counts. Thus, the data was cleaned up using the ROUND function for a more legible decimal format. A COUNT function was applied, adding a column that highlighted the number of patients treated by each specialty.

To ensure the Director's focus remains on significant data, specialties with less than 50 patients were filtered out. This was achieved using the HAVING function, which effectively filters on aggregated rather than individual rows, ensuring only specialties treating more than 50 patients were included in the final list.

![by origin](/assets/images/surgery_specialty_1.png)
![by origin](/assets/images/surgery_specialty_2.png)


### Query 3



### Query 4
The head of the hospital is interested in investigating the correlation between the quantity of laboratory procedures and the duration of patient hospital stays. They are particularly curious to determine if there's a trend indicating that patients who undergo numerous lab procedures also have extended hospital stays. For the purpose of this investigation, patients are classified into three groups based on the number of lab procedures they undergo: those with few procedures (0-25), those with an average number of procedures (25-55), and those undergoing many procedures (55+).

The CASE WHEN function was used to split the data into these three groups for study. To make sure everything was working correctly, a check was done before grouping the data further. This was done by looking at the average stay in the hospital and the number of lab procedures, as shown in the next part of the report.

![by origin](/assets/images/time_spent_procedures_1.png)
![by origin](/assets/images/time_spent_procedures_2.png)