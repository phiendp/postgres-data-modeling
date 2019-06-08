# Data Modeling with Postgres

## Introduction
A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analytics team is particularly interested in understanding what songs users are listening to. Currently, they don't have an easy way to query their data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

They'd like a data engineer to create a Postgres database with tables designed to optimize queries on song play analysis, and bring you on the project. Your role is to create a database schema and ETL pipeline for this analysis. You'll be able to test your database and ETL pipeline by running queries given to you by the analytics team from Sparkify and compare your results with their expected results.


## Project Description
In this project, you'll apply what you've learned on data modeling with Postgres and build an ETL pipeline using Python. To complete the project, you will need to define fact and dimension tables for a star schema for a particular analytic focus, and write an ETL pipeline that transfers data from files in two local directories into these tables in Postgres using Python and SQL.

## Schema
### Fact Table
* songplays: records in log data associated with song plays.

### Dimensions Table
* users: users in the app.
* songs: songs in the music database.
* artists: artists in the music database.
* time: timestamps of records in songplays broken down into specific units.

<img width="1711" alt="Screen Shot 2019-06-08 at 11 05 41 AM" src="https://user-images.githubusercontent.com/2704142/59141818-ceb11400-89dd-11e9-9487-aa8cc1143686.png">

## How to run
1. Execute `create_tables.py` to create the table in the database.
2. Execute `etl.py` to process and load the data from our logs to the database.
3. Check the results via `test.ipynb`.
