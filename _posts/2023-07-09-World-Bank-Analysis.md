---
title: "SQL and International Development: Analyzing IDA World Bank Data"
date: 2023-07-09 00:00:00 -0700
categories: [DAA Bootcamp]
tags: [data analytics,sql]     # TAG names should always be lowercase
---

Welcome, data enthusiasts. In my third project with the DAA bootcamp, I will explore the complex landscape of **International Development Association (IDA) World Bank data** with **SQL**. The IDA, a critical arm of the World Bank Group, works tirelessly to combat poverty in the world's most vulnerable regions, allocating substantial funds for an array of projects each year.

Here are my **two key questions**:

* Over the **past decade**, which country has emerged as the **top beneficiary per capita** from the IDA's funds?
* Once we've identified this country, **how have these funds been allocated** within its boundaries?

By applying SQL to this data-rich context, I aim to shed light on both these questions. So, let's embark on this journey, using SQL as our compass to navigate the vast ocean of global development funding data.

## The Project

For this project, I will be using **Azure Data Studio** to run SQL. I start off by using the import wizard tool to import two tables into my database. I am using these two datasets:
* [IDA Statement Of Credits and Grants](https://finances.worldbank.org/Loans-and-Credits/IDA-Statement-Of-Credits-and-Grants-Historical-Dat/tdwh-3krx)
* [World Bank Population Data](https://data.worldbank.org/indicator/SP.POP.TOTL)