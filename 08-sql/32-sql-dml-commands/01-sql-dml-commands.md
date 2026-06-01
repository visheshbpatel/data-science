# SQL DML Commands Complete Notes

A structured reference for SQL DML commands with syntax, examples, and practice queries.

## 1. What is DML?

DML stands for **Data Manipulation Language**.

DML commands are used to **work with the data stored inside a table**.

Unlike DDL, which works on structure, DML works on actual records (rows).

Main DML Commands:

- INSERT
- SELECT
- UPDATE
- DELETE

---

## 2. INSERT Command

Used to add new data into a table.

## Syntax

```sql
INSERT INTO table_name(column1, column2, column3)
VALUES(value1, value2, value3);
```

---

## Example

Table: `smartphones`

| id | brand | model | price |
|---:|---|---|---:|
| 1 | Samsung | Galaxy S23 | 75000 |

```sql
INSERT INTO smartphones(id, brand, model, price)
VALUES(1, 'Samsung', 'Galaxy S23', 75000);
```

---

## 3. INSERT Variations

### Insert with selected columns

```sql
INSERT INTO smartphones(brand, price)
VALUES('Apple', 90000);
```

---

### Insert all columns

```sql
INSERT INTO smartphones
VALUES(2, 'Apple', 'iPhone 15', 90000);
```

---

### Insert multiple rows

```sql
INSERT INTO smartphones(brand, model, price)
VALUES
('Samsung','S23',75000),
('Apple','iPhone 15',90000),
('OnePlus','11R',42000);
```

---

## 4. Import Data in MySQL Workbench

Steps:

1. Open MySQL Workbench
2. Right click on schema
3. Select **Table Data Import Wizard**
4. Choose CSV file
5. Select destination table
6. Import

Useful when working with large datasets like smartphone dataset.

---

## 5. SELECT Command

Used to retrieve data.

### Select all

```sql
SELECT * FROM smartphones;
```

---

### Filter specific columns

```sql
SELECT brand, model, price
FROM smartphones;
```

---

## 6. Alias (Renaming Columns)

Alias is temporary column renaming.

## Syntax

```sql
SELECT price AS cost
FROM smartphones;
```

Example:

```sql
SELECT brand AS company_name
FROM smartphones;
```

---

## 7. Create Expression Using Columns

SQL allows calculations with columns.

Example:

```sql
SELECT brand,
       price,
       price * 0.18 AS gst_amount
FROM smartphones;
```

---

## 8. Constants in SELECT

We can also add constant values.

Example:

```sql
SELECT brand,
       'India' AS country
FROM smartphones;
```

---

## 9. DISTINCT

Used to get unique values.

---

### Unique values from one column

```sql
SELECT DISTINCT brand
FROM smartphones;
```

---

### Unique combinations

```sql
SELECT DISTINCT brand, processor_brand
FROM smartphones;
```

---

## 10. WHERE Clause

Used to filter rows.

---

## Find all Samsung phones

```sql
SELECT *
FROM smartphones
WHERE brand = 'Samsung';
```

---

## Phones with price > 50000

```sql
SELECT *
FROM smartphones
WHERE price > 50000;
```

---

## BETWEEN

Used for range filtering.

### Phones between 10000 and 20000

```sql
SELECT *
FROM smartphones
WHERE price BETWEEN 10000 AND 20000;
```

---

## Rating > 80 and price < 25000

```sql
SELECT *
FROM smartphones
WHERE rating > 80
AND price < 25000;
```

---

## Samsung phones with RAM > 8GB

```sql
SELECT *
FROM smartphones
WHERE brand='Samsung'
AND ram_capacity > 8;
```

---

## Samsung phones with Snapdragon processor

```sql
SELECT *
FROM smartphones
WHERE brand='Samsung'
AND processor_brand='Snapdragon';
```

---

## 11. Query Execution Order

SQL does not execute top to bottom.

Order:

1. FROM
2. WHERE
3. GROUP BY
4. HAVING
5. SELECT
6. ORDER BY
7. LIMIT

---

## Example

Find brands who sell phones with price > 50000

```sql
SELECT DISTINCT brand
FROM smartphones
WHERE price > 50000;
```

---

## 12. IN and NOT IN

---

## IN

```sql
SELECT *
FROM smartphones
WHERE brand IN ('Samsung','Apple','OnePlus');
```

---

## NOT IN

```sql
SELECT *
FROM smartphones
WHERE brand NOT IN ('Samsung','Apple');
```

---

## 13. UPDATE

Used to modify existing records.

---

## Syntax

```sql
UPDATE smartphones
SET price = 79999
WHERE brand='Samsung';
```

---

## Example

```sql
UPDATE smartphones
SET rating = 85
WHERE model='Galaxy S23';
```

---

## 14. DELETE

Used to remove records.

---

## Syntax

```sql
DELETE FROM smartphones
WHERE condition;
```

---

## Delete all phones with price > 200000

```sql
DELETE FROM smartphones
WHERE price > 200000;
```

---

## 15. Types of SQL Functions

Two main types:

- Aggregate Functions
- Scalar Functions

---

### 16. Aggregate Functions

Work on multiple rows and return single value.

---

## MAX()

Find maximum value.

```sql
SELECT MAX(price)
FROM smartphones;
```

---

## MIN()

```sql
SELECT MIN(price)
FROM smartphones;
```

---

## Minimum and Maximum price

```sql
SELECT MIN(price), MAX(price)
FROM smartphones;
```

---

## Price of costliest Samsung phone

```sql
SELECT MAX(price)
FROM smartphones
WHERE brand='Samsung';
```

---

## AVG()

Average value.

Average rating of Apple phones:

```sql
SELECT AVG(rating)
FROM smartphones
WHERE brand='Apple';
```

---

## SUM()

```sql
SELECT SUM(price)
FROM smartphones;
```

---

## COUNT()

Number of OnePlus phones:

```sql
SELECT COUNT(*)
FROM smartphones
WHERE brand='OnePlus';
```

---

## COUNT(DISTINCT)

Number of brands:

```sql
SELECT COUNT(DISTINCT brand)
FROM smartphones;
```

---

## STD()

Standard deviation of screen sizes

```sql
SELECT STD(screen_size)
FROM smartphones;
```

---

## VARIANCE()

Variance of Xiaomi phone prices

```sql
SELECT VARIANCE(price)
FROM smartphones
WHERE brand='Xiaomi';
```

---

### 17. Scalar Functions

Works on individual values.

---

## ABS()

Absolute value.

```sql
SELECT ABS(-45);
```

Output:

```text
45
```

---

## ROUND()

Round to decimal places.

Round ppi to 1 decimal place:

```sql
SELECT ROUND(ppi_density,1)
FROM smartphones;
```

---

## CEIL()

Rounds upward.

```sql
SELECT CEIL(4.1);
```

Output:

```text
5
```

```sql
SELECT CEIL(4.9);
```

Output:

```text
5
```

---

## FLOOR()

Rounds downward.

```sql
SELECT FLOOR(4.9);
```

Output:

```text
4
```

```sql
SELECT FLOOR(4.1);
```

Output:

```text
4
```

---

## 18. Practice Queries

---

## Average battery and rear camera for phones price >= 100000

```sql
SELECT AVG(battery_capacity),
       AVG(primary_camera_rear)
FROM smartphones
WHERE price >= 100000;
```

---

## Average internal memory with refresh rate >= 120 and front camera >= 20MP

```sql
SELECT AVG(internal_memory)
FROM smartphones
WHERE refresh_rate >= 120
AND front_camera_resolution >= 20;
```

---

## Number of smartphones with 5G capability

```sql
SELECT COUNT(*)
FROM smartphones
WHERE has_5g = 1;
```

---

## Quick Revision Summary

## DML Commands

```sql
INSERT
SELECT
UPDATE
DELETE
```

---

## Filtering

```sql
WHERE
BETWEEN
IN
NOT IN
DISTINCT
```

---

## Aggregate Functions

```sql
MAX()
MIN()
AVG()
SUM()
COUNT()
COUNT(DISTINCT)
STD()
VARIANCE()
```

---

## Scalar Functions

```sql
ABS()
ROUND()
CEIL()
FLOOR()
```
