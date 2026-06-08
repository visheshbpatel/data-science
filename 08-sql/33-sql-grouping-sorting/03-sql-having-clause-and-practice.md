# SQL HAVING Clause and Practice

## 1. What is HAVING Clause?

HAVING is used to filter groups after GROUP BY.

WHERE filters rows.

HAVING filters groups.

---

## 2. Why Do We Need HAVING?

Suppose we want:

- Brands with more than 20 phones
- Brands whose average rating is above 80
- Brands whose average price is greater than ₹50,000

These conditions depend on aggregate functions.

Aggregate functions cannot be used inside WHERE.

Therefore, SQL provides HAVING.

---

## 3. HAVING vs WHERE

| WHERE | HAVING |
|---------|---------|
| Filters rows | Filters groups |
| Executes before GROUP BY | Executes after GROUP BY |
| Cannot use aggregate functions | Can use aggregate functions |
| Works on individual records | Works on grouped records |

---

## 4. Query Execution Order

```text
FROM
WHERE
GROUP BY
HAVING
SELECT
ORDER BY
LIMIT
```

This execution order is extremely important.

---

## 5. Why Aggregate Functions Cannot Be Used in WHERE

Wrong:

```sql
SELECT brand_name,
AVG(price)
FROM smartphones
WHERE AVG(price) > 50000
GROUP BY brand_name;
```

Correct:

```sql
SELECT brand_name,
AVG(price)
FROM smartphones
GROUP BY brand_name
HAVING AVG(price) > 50000;
```

Reason:

AVG(price) is calculated after grouping.

WHERE executes before grouping.

---

# Smartphone Practice Problems

## Problem 1

### Find Average Rating of Brands Having More Than 20 Phones

```sql
SELECT brand_name,
COUNT(*) AS total_models,
AVG(rating) AS avg_rating
FROM smartphones
GROUP BY brand_name
HAVING COUNT(*) > 20
ORDER BY avg_rating DESC;
```


---

## Problem 2

### Find Top 3 Brands with Highest Average RAM

Conditions:

- Refresh Rate ≥ 90 Hz
- Fast Charging Available
- Brand should have at least 10 phones

```sql
SELECT brand_name,
AVG(ram_capacity) AS avg_ram
FROM smartphones
WHERE refresh_rate >= 90
AND fast_charging_available = 1
GROUP BY brand_name
HAVING COUNT(*) > 10
ORDER BY avg_ram DESC
LIMIT 3;
```


---

## Problem 3

### Average Price of Brands Having

- Average Rating > 70
- More Than 10 Phones
- Only 5G Phones

```sql
SELECT brand_name,
AVG(price) AS avg_price
FROM smartphones
WHERE has_5g='True'
GROUP BY brand_name
HAVING AVG(rating) > 70
AND COUNT(*) > 10;
```

---

# IPL Practice Problems

## Dataset

Table:

```text
ipl
```

Important Columns:

- batter
- batsman_run
- ID

---

## Problem 1

### Find Top 5 Run Scorers

```sql
SELECT batter,
SUM(batsman_run) AS runs
FROM ipl
GROUP BY batter
ORDER BY runs DESC
LIMIT 5;
```


---

## Problem 2

### Find 2nd Highest Six Hitter

```sql
SELECT batter,
COUNT(*) AS num_sixes
FROM ipl
WHERE batsman_run = 6
GROUP BY batter
ORDER BY num_sixes DESC
LIMIT 1,1;
```

### Explanation

- Filter only sixes
- Count sixes for each batter
- Sort descending
- Skip first row
- Return second row

---

## Problem 3

### Find Top Batsmen with Centuries

```sql
SELECT batter,
ID,
SUM(batsman_run) AS score
FROM ipl
GROUP BY batter, ID
HAVING score >= 100
ORDER BY batter ASC,
         score DESC;
```

### Why GROUP BY batter, ID?

A century is scored in a single innings.

If we group only by batter:

```sql
GROUP BY batter
```

SQL calculates career runs.

We need innings-wise scores.

Therefore:

```sql
GROUP BY batter, ID
```

creates separate groups for every batter in every match.

---

## Problem 4

### Top 5 Batsmen with Highest Strike Rate

Condition:

Minimum 1000 balls played.

### Strike Rate Formula

```text
Strike Rate =
(Runs / Balls Faced) × 100
```

### Query

```sql
SELECT batter,
SUM(batsman_run) AS runs,
COUNT(batsman_run) AS balls_faced,
ROUND(
(SUM(batsman_run)/COUNT(batsman_run))*100,
2
) AS SR
FROM ipl
GROUP BY batter
HAVING COUNT(batsman_run) > 1000
ORDER BY SR DESC
LIMIT 5;
```


---

## Common Mistakes

### Using Aggregate Functions in WHERE

Wrong:

```sql
WHERE AVG(price) > 50000
```

Correct:

```sql
HAVING AVG(price) > 50000
```

---

### Forgetting GROUP BY

Wrong:

```sql
SELECT brand_name,
AVG(price)
FROM smartphones;
```

Correct:

```sql
SELECT brand_name,
AVG(price)
FROM smartphones
GROUP BY brand_name;
```

---

### Using HAVING Instead of WHERE

Wrong:

```sql
HAVING price > 50000
```

Correct:

```sql
WHERE price > 50000
```

Use WHERE whenever filtering normal rows.

---

## Quick Revision

### WHERE

Filters rows.

### GROUP BY

Creates groups.

### HAVING

Filters groups.

---

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

---

### Important Functions

```sql
COUNT()
AVG()
SUM()
MIN()
MAX()
ROUND()
```

---

### Important Concepts

- HAVING Clause
- HAVING vs WHERE
- Aggregate Functions
- Query Execution Order
- Strike Rate Calculation
- Century Analysis
