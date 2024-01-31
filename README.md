# YouTube-Data-Analysis-END-TO-END-DATA-ENGINEERING-PROJECT


## **The requirement for (our simulated) customer:**
1. Launching new data driven campaign
2. Main advertising channel: YouTube
3. Initial Questions to answer:
- a) how to categorise videos, based on their comments and statistics ?
- b) what factors affect how popular a YouTube video will be ?


## **Why YouTube?**
 Top three most-visited websites(monthly)
 - Google: 92.5 billion
 - YouTube: 34.6 billion
 - Facebook: 25.5 billion

 ## **Things covered in this project but not limited to:**
 - to build a data lake from scratch in amazon s3 (joining semi-structured and structured data).
 - Lake House architecture design (Best practices ---> cost and performance).
 - Data Lake vs Data Warehouse
 - Data Lake design in layers, partitioned for cost-performance (eg- landing,cleansed as SSOT, reporting for BI users , WORM Model/ Write Once Read Many).
 - AWS Data Catalogue.
 - ETL in AWS Glue Spark Jobs , Amazon SageMaker jupyter Notebooks.
 - AWS SNS for alerting , AWS IAM for security mgmt.
 - SQL using AWS Athena and Spark SQL (i.e imapact of querying the optimized data layers).
 - Ingest changes incrementally and schema evolution
 - BI dashboards in AMAZON QuickSight.


## Overview
 This project aims to securely manage, streamline, and perform analysis on the structured and semi-structured YouTube videos data based on the video categories and the trending metrics.

## Project Goals

1. Data Ingestion — Build a mechanism to ingest data from different sources
2. ETL System — We are getting data in raw format, transforming this data into the proper format
3. Data lake — We will be getting data from multiple sources so we need centralized repo to store them
4. Scalability — As the size of our data increases, we need to make sure our system scales with it
5. Cloud — We can’t process vast amounts of data on our local computer so we need to use the cloud, in this case, we will use AWS
6. Reporting — Build a dashboard to get answers to the question we asked earlier

## Services we will be using:
1. Amazon S3: Amazon S3 is an object storage service that provides manufacturing scalability, data availability, security, and performance.
2. AWS IAM: This is nothing but identity and access management which enables us to manage access to AWS services and resources securely.
3. QuickSight: Amazon QuickSight is a scalable, serverless, embeddable, machine learning-powered business intelligence (BI) service built for the cloud.
4. AWS Glue: A serverless data integration service that makes it easy to discover, prepare, and combine data for analytics, machine learning, and application development.
5. AWS Lambda: Lambda is a computing service that allows programmers to run code without creating or managing servers.
6. AWS Athena: Athena is an interactive query service for S3 in which there is no need to load data it stays in S3.

 ## Dataset Used
 This Kaggle dataset contains statistics (CSV files) on daily popular YouTube videos over the course of many months. There are up to 200 trending videos published every day for many locations. The data for each region is in its own file. The video title, channel title, publication time, tags, views, likes and dislikes, description, and comment count are among the items included in the data. A category_id field, which differs by area, is also included in the JSON file linked to the region.

https://www.kaggle.com/datasets/datasnaek/youtube-new

## Architecture Diagram
![architecture](https://github.com/AKA-RONY/YouTube-Data-Engineering-Project/assets/67736824/bd86be18-543e-4647-9a90-4410e5ff988f)

