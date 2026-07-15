# SQL

This folder contains my SQL learning notes, hands-on practice, and solutions to SQL exercises.

SQL (Structured Query Language) is used to store, retrieve, manipulate, and manage data in relational databases.

It is one of the most important skills for data analysts, data scientists, and data engineers.

The topics are organized from SQL basics to advanced window functions using real datasets such as **Northwind**, **Drug Review**, **Insurance**, **Olympics**, and **IPL**.

---

# Folder Structure

## 30 - Database Fundamentals

- Databases
- DBMS vs RDBMS
- Tables, Rows, Columns
- Primary Key
- Foreign Key
- Relationships

---

## 31 - SQL DDL Commands

- CREATE
- ALTER
- DROP
- TRUNCATE
- RENAME

---

## 32 - SQL DML Commands

- SELECT
- INSERT
- UPDATE
- DELETE
- Filtering Records

---

## 33 - SQL Grouping & Sorting

- ORDER BY
- GROUP BY
- HAVING
- Aggregate Functions
  - COUNT()
  - SUM()
  - AVG()
  - MIN()
  - MAX()

---

## 34 - SQL Joins

- INNER JOIN
- LEFT JOIN
- RIGHT JOIN
- FULL JOIN
- CROSS JOIN
- SELF JOIN

Hands-on practice using multiple tables.

---

## 35 - SQL Subqueries

- Scalar Subqueries
- Multi-row Subqueries
- Correlated Subqueries
- Nested Queries
- Practical SQL Problems

---

## 36 - Window Functions

- OVER()
- PARTITION BY
- ORDER BY
- ROW_NUMBER()
- RANK()
- DENSE_RANK()
- Running Total
- Running Average
- Cumulative Sum
- Percentage of Total

---

## 37 - Advanced Window Functions

Applied window functions on real datasets.

Topics covered include:

- Ranking
- LAG()
- CUME_DIST()
- Running Average
- Cumulative Sum
- Percentage Change
- Year-over-Year Analysis
- Median Calculation
- Percentage of Total
- Advanced Analytical Queries

---

# Datasets Used

During practice, I used multiple datasets including:

- Northwind Database
- Drug Review Dataset
- Insurance Dataset
- Olympics Dataset
- IPL Ball-by-Ball Dataset

---

# Importing Large CSV Files into MySQL

For very large datasets, importing through **MySQL Workbench** can be slow or fail. Instead, I used **Pandas** with **SQLAlchemy** to load data directly into MySQL.

```python
import pandas as pd
from sqlalchemy import create_engine

# Read CSV file
df = pd.read_csv("your_dataset.csv")

# Connect to MySQL
engine = create_engine(
    "mysql+pymysql://username:password@localhost/database_name"
)

# Import data into MySQL
df.to_sql(
    name="table_name",
    con=engine,
    if_exists="replace",   # replace | append | fail
    index=False
)

print(f"Imported {len(df)} rows successfully.")
```

This approach is useful when working with datasets containing hundreds of thousands of rows.

---

# What I Learned

- Database fundamentals
- SQL query writing
- Data filtering and sorting
- Aggregate functions
- Joins
- Subqueries
- Window functions
- Analytical SQL queries
- Working with real-world datasets
- Importing large datasets into MySQL using Python

---

## Repository Context

This folder is part of my data science learning journey.

This section focuses on learning SQL concepts that are commonly used in data analysis and data-driven applications.

---

If you are learning SQL, feel free to explore the examples and practice the queries alongside the notes.