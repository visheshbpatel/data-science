# SQL Grouping Data

## 1. What is GROUP BY?

GROUP BY is used to divide rows into groups based on a column value.

Instead of calculating a result for the entire table, SQL calculates a result for each group.

Example:

Without GROUP BY:

```sql
SELECT AVG(price)
FROM smartphones;
```

Returns one average price for the entire table.

With GROUP BY:

```sql
SELECT brand_name,
       AVG(price)
FROM smartphones
GROUP BY brand_name;
```

Returns one average price for each brand.

---

## 2. Why Do We Need GROUP BY?

GROUP BY is used when we want to answer questions like:

- Average price of each brand
- Number of phones per brand
- Maximum rating per brand
- Average battery capacity per brand

Without GROUP BY, these analyses are not possible.

---

## 3. Aggregate Functions

Aggregate functions operate on multiple rows and return a single result.

### COUNT()

Counts rows.

```sql
SELECT COUNT(*)
FROM smartphones;
```

---

### AVG()

Returns average value.

```sql
SELECT AVG(price)
FROM smartphones;
```

---

### SUM()

Returns total value.

```sql
SELECT SUM(price)
FROM smartphones;
```

---

### MIN()

Returns smallest value.

```sql
SELECT MIN(price)
FROM smartphones;
```

---

### MAX()

Returns largest value.

```sql
SELECT MAX(price)
FROM smartphones;
```

---

## 4. Rules of GROUP BY

When using GROUP BY:

Every selected column must either:

1. Be present in GROUP BY
2. Be used inside an aggregate function

Correct:

```sql
SELECT brand_name,
       AVG(price)
FROM smartphones
GROUP BY brand_name;
```

Incorrect:

```sql
SELECT model,
       brand_name,
       AVG(price)
FROM smartphones
GROUP BY brand_name;
```

---

## 5. Multiple Column GROUP BY

SQL can create groups using more than one column.

```sql
SELECT brand_name,
       processor_brand,
       COUNT(*)
FROM smartphones
GROUP BY brand_name,
         processor_brand;
```

Here SQL creates groups for every unique combination of:

- brand_name
- processor_brand

---

## 6. Query Execution Order

```text
FROM
WHERE
GROUP BY
HAVING
SELECT
ORDER BY
LIMIT
```

Understanding execution order is very important for GROUP BY queries.

---

# Practice Problems

## Problem 1

### Brand Wise Statistics

Find:

- Number of phones
- Average price
- Maximum rating
- Average screen size
- Average battery capacity

```sql
SELECT brand_name,
COUNT(*) AS num_phones,
ROUND(AVG(price)) AS avg_price,
MAX(rating) AS max_rating,
ROUND(AVG(screen_size),2) AS avg_screen_size,
ROUND(AVG(battery_capacity),2) AS avg_battery_capacity
FROM smartphones
GROUP BY brand_name
ORDER BY num_phones DESC;
```


---

## Problem 2

### Group Phones Based on NFC Availability

```sql
SELECT has_nfc,
AVG(price) AS avg_price,
AVG(rating) AS avg_rating
FROM smartphones
GROUP BY has_nfc;
```

---

## Problem 3

### Group Phones Based on Extended Memory Availability

```sql
SELECT extended_memory_available,
AVG(price) AS avg_price
FROM smartphones
GROUP BY extended_memory_available;
```

---

## Problem 4

### Group by Brand and Processor

```sql
SELECT brand_name,
processor_brand,
COUNT(*) AS num_models,
AVG(primary_camera_rear) AS avg_camera_resolution
FROM smartphones
GROUP BY brand_name,
         processor_brand;
```

---

## Problem 5

### Top 5 Most Costly Phone Brands

```sql
SELECT brand_name,
ROUND(AVG(price)) AS avg_price
FROM smartphones
GROUP BY brand_name
ORDER BY avg_price DESC
LIMIT 5;
```

---

## Problem 6

### Brand with Smallest Average Screen Size

```sql
SELECT brand_name,
ROUND(AVG(screen_size),2) AS avg_screen_size
FROM smartphones
GROUP BY brand_name
ORDER BY avg_screen_size ASC
LIMIT 1;
```

### Note

This finds the brand with the smallest average screen size.

---

## Problem 7

### Average Price of 5G Phones vs Non‑5G Phones

```sql
SELECT has_5g,
AVG(price) AS avg_price
FROM smartphones
GROUP BY has_5g;
```

---

## Problem 8

### Brand with Highest Number of NFC and IR Blaster Phones

```sql
SELECT brand_name,
COUNT(*) AS total_models
FROM smartphones
WHERE has_nfc='True'
AND has_ir_blaster='True'
GROUP BY brand_name
ORDER BY total_models DESC
LIMIT 1;
```

---

## Problem 9

### Samsung 5G Phones: NFC vs Non‑NFC Price Analysis

```sql
SELECT has_nfc,
AVG(price) AS avg_price
FROM smartphones
WHERE brand_name='samsung'
AND has_5g='True'
GROUP BY has_nfc;
```

### Why GROUP BY has_nfc?

We want separate average prices for:

- NFC Phones
- Non‑NFC Phones

---

## Problem 10

### Costliest Phone

```sql
SELECT model,
       price
FROM smartphones
ORDER BY price DESC
LIMIT 1;
```

---

### Using GROUP BY Without Purpose

GROUP BY should only be used when aggregation is needed.

---

## Quick Revision

### Aggregate Functions

```sql
COUNT()
AVG()
SUM()
MIN()
MAX()
```

### GROUP BY Rules

- Every selected column must be grouped
- Or aggregated

### Execution Order

```text
FROM
WHERE
GROUP BY
HAVING
SELECT
ORDER BY
LIMIT
```

### Important Concepts

- GROUP BY
- Aggregate Functions
- Multiple Column GROUP BY
- Query Execution Order
- Data Aggregation
