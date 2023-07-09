---
title: "SQL and International Development: Analyzing IDA World Bank Data"
date: 2023-07-09 00:00:00 -0700
categories: [DAA Bootcamp]
tags: [data analytics,sql]     # TAG names should always be lowercase
---

Welcome, data enthusiasts. In my third project with the DAA bootcamp, I explored the complex landscape of **International Development Association (IDA)** World Bank data with **SQL**. The IDA, a critical arm of the **World Bank Group**, works tirelessly to combat poverty in the world's most vulnerable regions, allocating substantial funds for an array of projects each year.

Here are my **two key questions**:

1. Over the **past decade**, which country has emerged as the **top beneficiary per capita** from the IDA's funds?
2. Which country has recieved the most IDA overall in the past 10 years. **How have these funds been allocated** within its boundaries?

By applying **SQL** to this data-rich context, I shed light on both these questions. So, let's embark on this journey, using SQL as our compass to navigate the vast ocean of global development funding data.

## The Project

For this project, I used **Azure Data Studio** to run **SQL**. I started off by using the import wizard tool to import two tables into my database. I used these two datasets:
* [IDA Statement Of Credits and Grants](https://finances.worldbank.org/Loans-and-Credits/IDA-Statement-Of-Credits-and-Grants-Historical-Dat/tdwh-3krx)
* [World Bank Population Data](https://data.worldbank.org/indicator/SP.POP.TOTL)

After importing these two tables, I wrote querys to **extract important information** that I would use from each of these tables and created two **new, simpler tables**.
![Alt Text](/assets/images/carbon1.png){: width="600" }
*Creates a new table with country names and total principal issued in the past decade*
![Alt Text](/assets/images/carbon2.png){: width="400" }
*Creates a new table with country names (column1) and 2013 population data (column58)*
Next, I **combined** both of these tables into one table with INNER JOIN, so that the rows would match where the **country names matched**.

![Alt Text](/assets/images/carbon3.png){: width="500" }
*Creates a new table, combining the two simple tables where country names match*
Afterwards, I used the new table to **sort** the countries by **Principal per capita**.

![Alt Text](/assets/images/carbon4.png){: width="400" }
*Sorts countries by Principal per capita*
![Alt Text](/assets/images/principalpercapita.png){: width="500" }
*Zimbabwe as highest Principal per capita in the past decadee*
This table shows the "World" as number 1 and "South Asia" as number 2. Not only are these not countries, but the information is innacurate. This is because the population data includes countries that are not funded by the IDA. For this reason, **Zimbabwe** is the winner.

Moving on to question 2, I sorted the "country_principal" table I created earlier to find the country that recieved the most principal from the IDA in the past decade: Bangladesh
![Alt Text](/assets/images/carbon5.png){: width="400" }
*Sort countries by principal recieved in the past decade*
![Alt Text](/assets/images/principaltotal.png){: width="500" }
*Bangladesh recieved the most funding in the past decade*
