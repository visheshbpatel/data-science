# SQL Subqueries

## What is a Subquery?

A subquery is a query written inside another SQL query.

The inner query executes first and its result is used by the outer query.

Example:

```sql
SELECT *
FROM movies
WHERE score = (
    SELECT MAX(score)
    FROM movies
);
```

### Execution Flow

```sql
SELECT MAX(score)
FROM movies;
```

returns the highest movie rating.

The outer query then finds the movie having that rating.

---

## Types of Subqueries

### 1. Independent (Non-Correlated) Subquery

The inner query can execute independently of the outer query.

#### Types

* Scalar Subquery (1 Row, 1 Column)
* Row Subquery (Multiple Rows, 1 Column)
* Table Subquery (Multiple Rows, Multiple Columns)

### 2. Correlated Subquery

The inner query depends on the current row of the outer query and executes repeatedly for each row.

---

# Where Can Subqueries Be Used?

Subqueries can be used with:

* WHERE
* SELECT
* FROM
* HAVING
* INSERT
* UPDATE
* DELETE

---

# 1. Independent Subquery - Scalar Subquery

A scalar subquery returns exactly one value.

## 1.1 Find the Movie with Highest Profit

```sql
SELECT *
FROM movies
WHERE (gross - budget) = (
    SELECT MAX(gross - budget)
    FROM movies
);
```

Alternative:

```sql
SELECT *
FROM movies
ORDER BY (gross - budget) DESC
LIMIT 1;
```

### Which is Better?

For large datasets:

```sql
ORDER BY ... LIMIT 1
```

is generally faster because sorting and indexing can be optimized more efficiently.

---

## 1.2 Count Movies Having Rating Above Average Rating

```sql
SELECT COUNT(*)
FROM movies
WHERE score > (
    SELECT AVG(score)
    FROM movies
);
```

---

## 1.3 Highest Rated Movie of Year 2000

```sql
SELECT *
FROM movies
WHERE year = 2000
  AND score = (
        SELECT MAX(score)
        FROM movies
        WHERE year = 2000
  );
```

---

## 1.4 Highest Rated Movie Among Movies Having Votes Above Dataset Average

```sql
SELECT *
FROM movies
WHERE score = (
    SELECT MAX(score)
    FROM movies
    WHERE votes > (
        SELECT AVG(votes)
        FROM movies
    )
);
```

---

# 2. Independent Subquery - Row Subquery

A row subquery returns multiple rows but only one column.

## 2.1 Find All Users Who Never Ordered

```sql
SELECT *
FROM users
WHERE user_id NOT IN (
    SELECT DISTINCT user_id
    FROM orders
);
```

---

## 2.2 Find All Movies Made by Top 3 Directors (Based on Total Gross)

```sql
WITH top_directors AS (
    SELECT director
    FROM movies
    GROUP BY director
    ORDER BY SUM(gross) DESC
    LIMIT 3
)
SELECT *
FROM movies
WHERE director IN (
    SELECT *
    FROM top_directors
);
```

---

## 2.3 Find Movies of Actors Whose Average Rating is Greater Than 8.5

(Votes cutoff = 25000)

```sql
SELECT *
FROM movies
WHERE star IN (
    SELECT star
    FROM movies
    WHERE votes > 25000
    GROUP BY star
    HAVING AVG(score) > 8.5
);
```

---

# 3. Independent Subquery - Table Subquery

Returns multiple rows and multiple columns.

## 3.1 Most Profitable Movie of Each Year

```sql
SELECT *
FROM movies
WHERE (year, gross - budget) IN (
    SELECT year,
           MAX(gross - budget)
    FROM movies
    GROUP BY year
);
```

---

## 3.2 Highest Rated Movie of Each Genre

(Votes cutoff = 25000)

```sql
SELECT *
FROM movies
WHERE (genre, score) IN (
    SELECT genre,
           MAX(score)
    FROM movies
    WHERE votes > 25000
    GROUP BY genre
)
AND votes > 25000;
```

---

## 3.3 Highest Grossing Movies of Top 5 Actor-Director Combinations

```sql
WITH top_duos AS (
    SELECT star,
           director,
           MAX(gross)
    FROM movies
    GROUP BY star, director
    ORDER BY SUM(gross) DESC
    LIMIT 5
)
SELECT *
FROM movies
WHERE (star, director, gross) IN (
    SELECT *
    FROM top_duos
);
```

---

# 4. Correlated Subquery

A correlated subquery depends on values from the outer query.

The inner query executes once for every row processed by the outer query.

## 4.1 Movies Rated Higher Than Their Genre Average

```sql
SELECT *
FROM movies m1
WHERE score > (
    SELECT AVG(score)
    FROM movies m2
    WHERE m2.genre = m1.genre
);
```

---

## 4.2 Favorite Food of Each Customer

```sql
WITH fav_food AS (
    SELECT name,
           f_name,
           COUNT(*) AS frequency
    FROM users t1
    JOIN orders t2
        ON t1.user_id = t2.user_id
    JOIN order_details t3
        ON t2.order_id = t3.order_id
    JOIN food t4
        ON t3.f_id = t4.f_id
    GROUP BY t2.user_id, t3.f_id
)

SELECT *
FROM fav_food f1
WHERE frequency = (
    SELECT MAX(frequency)
    FROM fav_food f2
    WHERE f2.user_id = f1.user_id
);
```

---

# 5. Subquery with SELECT

## 5.1 Percentage of Votes for Each Movie

```sql
SELECT name,
       ROUND(
           (votes / (SELECT SUM(votes) FROM movies)) * 100,
           2
       ) AS votes_percentage
FROM movies;
```

---

## 5.2 Display Movie Score and Genre Average

```sql
SELECT name,
       genre,
       score,
       ROUND(
           (
               SELECT AVG(score)
               FROM movies m2
               WHERE m2.genre = m1.genre
           ),
           2
       ) AS genre_avg
FROM movies m1;
```

---

# 6. Subquery with FROM

## 6.1 Average Rating of Restaurants

```sql
SELECT r_name,
       avg_rating
FROM (
        SELECT r_id,
               ROUND(AVG(restaurant_rating), 2) AS avg_rating
        FROM orders
        GROUP BY r_id
     ) t1
JOIN restaurants t2
ON t1.r_id = t2.r_id;
```

---

# 7. Subquery with HAVING

## 7.1 Genres Having Average Score Greater Than Overall Average

```sql
SELECT genre,
       ROUND(AVG(score), 2)
FROM movies
GROUP BY genre
HAVING AVG(score) > (
    SELECT AVG(score)
    FROM movies
);
```

---

# 8. Subquery with INSERT

## Populate Loyal Users Table

```sql
INSERT INTO loyal_users (user_id, name)
SELECT t1.user_id,
       t2.name
FROM orders t1
JOIN users t2
ON t1.user_id = t2.user_id
GROUP BY t1.user_id, t2.name
HAVING COUNT(*) > 3;
```

---

# 9. Subquery with UPDATE

## Give 10% Reward Money Based on Order Value

```sql
UPDATE loyal_users lu
SET money = (
    SELECT SUM(amount) * 0.1
    FROM orders o
    WHERE o.user_id = lu.user_id
);
```

---

# 10. Subquery with DELETE

## Delete Users Who Never Ordered

```sql
DELETE FROM users
WHERE user_id IN (
    SELECT user_id
    FROM users
    WHERE user_id NOT IN (
        SELECT DISTINCT user_id
        FROM orders
    )
);
```

---

# Key Takeaways

* Subqueries are queries inside another query.
* Inner query executes before the outer query.
* Subqueries can return:

  * Single value (Scalar)
  * Multiple rows (Row Subquery)
  * Multiple rows and columns (Table Subquery)
* Correlated subqueries depend on the outer query.
* Subqueries can be used with:

  * WHERE
  * SELECT
  * FROM
  * HAVING
  * INSERT
  * UPDATE
  * DELETE
* Always consider performance; sometimes `JOIN`, `CTE`, or `ORDER BY ... LIMIT` can be faster than subqueries.
