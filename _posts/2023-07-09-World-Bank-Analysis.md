---
title: "SQL and International Development: Analyzing IDA World Bank Data"
date: 2023-07-09 00:00:00 -0700
image: /assets/images/worldbank.png
categories: [DAA Bootcamp]
tags: [data analytics,sql]     # TAG names should always be lowercase
---

Welcome, data enthusiasts. In my third project with the DAA boot camp, I explored the complex landscape of International Development Association (IDA) World Bank data with SQL. The IDA, a critical arm of the World Bank Group, works tirelessly to combat poverty in the world's most vulnerable regions, allocating substantial funds for an array of projects each year.

**Two key questions:**

1. Over the past decade, which country has emerged as the top beneficiary per capita from the IDA's funds?
2. How can the many projects supporting India in the past decade be categorized in simple terms?

By applying SQL to this data-rich context, I shed light on both these questions. So, let's embark on this journey, using SQL as our compass to navigate the vast ocean of global development funding data.

## The Project

For this project, Azure Data Studio was used to run SQL. Starting out with **question 1**, the import wizard tool was used to import two tables into the database. These two datasets were used:
* [IDA Statement Of Credits and Grants](https://finances.worldbank.org/Loans-and-Credits/IDA-Statement-Of-Credits-and-Grants-Historical-Dat/tdwh-3krx)
* [World Bank Population Data](https://data.worldbank.org/indicator/SP.POP.TOTL)

After importing these two tables, a CTE was created. A CTE works similarly to a subquery, but it is much easier to read. The CTE was used to extract principal disbursements that occurred exclusively in the past decade. Additionally, SUM was used along with GROUP BY to find the total amount of principal for each country within this time period.

Next, the CTE was combined with the population data using INNER JOIN. In addition to country and principal columns, a column was selected that represented the population data for each country from 2013. Additionally, a column was created that showcased the principal column divided by the 2013 population.

Finally, ORDER BY was used to sort the principal disbursements per capita in the last 10 years in descending order. Tuvalu received the most principal per capita in the past decade.
![Alt Text](/assets/images/fixed_query_1.png){: width="600" }
![Alt Text](/assets/images/fixed_query_2.png){: width="600" }

