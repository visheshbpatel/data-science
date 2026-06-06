# SQL Sorting Data

## 1. What is Sorting?

Sorting means arranging records in a specific order based on one or more columns.

In SQL, sorting is performed using the `ORDER BY` clause.

Common use cases:

- Most expensive phones
- Highest rated products
- Top scoring players
- Latest transactions

---

## 2. ORDER BY Clause

### Syntax

```sql
SELECT column_names
FROM table_name
ORDER BY column_name;
```

### Ascending Order (ASC)

```sql
SELECT model, price
FROM smartphones
ORDER BY price ASC;
```

Smallest values appear first.

### Descending Order (DESC)

```sql
SELECT model, price
FROM smartphones
ORDER BY price DESC;
```

Largest values appear first.

---

## 3. LIMIT Clause

LIMIT restricts the number of rows returned.

### Syntax

```sql
SELECT *
FROM smartphones
LIMIT 5;
```

Returns only 5 rows.

### LIMIT with OFFSET

```sql
LIMIT offset, count
```

Example:

```sql
LIMIT 1,1;
```

Skip the first row and return the next row.

---

## 4. Query Execution Order

For sorting queries:

```text
FROM
WHERE
SELECT
ORDER BY
LIMIT
```

SQL does not execute from top to bottom.

---

## 5. Aliases and Calculated Columns

### Alias

Alias gives a temporary name to a column.

```sql
SELECT model,
       price AS phone_price
FROM smartphones;
```

### Calculated Column

```sql
SELECT model,
       num_front_cameras + num_rear_cameras AS total_cameras
FROM smartphones;
```

The result is calculated during query execution.

---

## Practice Problems

### Problem 1: Top 5 Samsung phones with biggest screen size

```sql
SELECT *
FROM smartphones
WHERE brand_name='samsung'
ORDER BY screen_size DESC
LIMIT 5;
```

### Problem 2: Sort by total cameras

```sql
SELECT model,
num_front_cameras + num_rear_cameras AS total_cameras
FROM smartphones
ORDER BY total_cameras DESC;
```

### Problem 3: Sort by PPI

```sql
SELECT model,
ROUND(SQRT(resolution_width*resolution_width +
resolution_height*resolution_height)/screen_size) AS ppi
FROM smartphones
ORDER BY ppi DESC;
```

### Problem 4: 2nd Largest Battery

```sql
SELECT model,battery_capacity
FROM smartphones
ORDER BY battery_capacity DESC
LIMIT 1,1;
```

### Problem 5: Worst Rated Apple Phone

```sql
SELECT model,rating
FROM smartphones
WHERE brand_name='apple'
ORDER BY rating ASC
LIMIT 1;
```

### Problem 6: Sort by Brand then Rating

```sql
SELECT model,rating
FROM smartphones
ORDER BY brand_name ASC,rating DESC;
```

### Problem 7: Sort by Brand then Price

```sql
SELECT *
FROM smartphones
ORDER BY brand_name ASC,price ASC;
```
