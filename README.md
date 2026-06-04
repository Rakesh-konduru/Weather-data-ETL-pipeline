Weather Data Pipeline using Databricks
Overview

This project demonstrates the development of a data pipeline using Databricks to process and transform weather data into structured tables for analysis. The pipeline handles data ingestion, cleaning, transformation, and storage in an optimized format.

Technologies Used

Databricks
PySpark
SQL
Delta Lake

Workflow

The pipeline begins by loading raw weather data into the Databricks environment. The data is then cleaned by selecting relevant columns and handling missing or inconsistent values. Transformations are applied using PySpark and SQL to structure the data properly. The processed data is stored in multiple tables within the accuweather schema. The pipeline is scheduled to run automatically at regular intervals.

Output Tables

forecast_daily
forecast_hourly
historical_daily
historical_hourly

Features

Automated data pipeline using scheduled jobs
Efficient data processing using PySpark
Storage in Delta format for improved performance and reliability
Support for scalable and production-level data workflows

Data Storage

The processed data is stored in Delta tables within the Databricks environment. Delta Lake provides features such as ACID transactions, improved query performance, and support for data updates and versioning.

Use Case

This pipeline can be used to support analytics and reporting on weather data, including daily and hourly forecasts as well as historical trends.

Learning Outcome

Through this project, I gained hands-on experience in building data pipelines, performing data transformations using PySpark and SQL, and working with Delta Lake for efficient data storage and management.

