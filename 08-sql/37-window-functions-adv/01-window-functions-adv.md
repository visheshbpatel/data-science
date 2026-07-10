# SQL Window Functions - Part 2

> Comprehensive notes covering advanced applications of SQL Window Functions.

## Overview

This document summarizes practical uses of SQL Window Functions beyond basic ranking. Window functions perform calculations across a set of related rows while returning one result for every row.

Unlike `GROUP BY`, window functions **do not collapse rows**.

---

# Topics Covered

1. Ranking
2. Cumulative Sum
3. Cumulative Average
4. Running Average
5. Percent of Total
6. Percent Change
7. Percentiles & Quantiles
8. Segmentation using NTILE()
9. Cumulative Distribution
10. PARTITION BY Multiple Columns

---

# 1. Ranking

## Concept

Ranking assigns a position to rows based on an ordering.

Common ranking functions:

- ROW_NUMBER()
- RANK()
- DENSE_RANK()

In this example, `DENSE_RANK()` is used to find the Top 5 batters from every IPL team.


## Problem Statement
Find the **Top 5 highest run scorers from each IPL team** based on the total runs scored.

```sql
USE sql_cx;

SELECT *
FROM (
    SELECT
        BattingTeam,
        batter,
        SUM(batsman_run) AS total_runs,
        DENSE_RANK() OVER(
            PARTITION BY BattingTeam
            ORDER BY SUM(batsman_run) DESC
        ) AS rank_within_team
    FROM ipl
    GROUP BY BattingTeam,batter
) t
WHERE rank_within_team < 6
ORDER BY BattingTeam,rank_within_team;
```

### Key Takeaways

- PARTITION BY creates independent rankings.
- DENSE_RANK() doesn't skip rank numbers.
- Useful for Top-N analysis.

---

# 2. Cumulative Sum

## Concept

A cumulative sum calculates the running total by including the current row and every previous row.

Formula:

Current Row + All Previous Rows

## Problem Statement
Calculate Virat Kohli's cumulative career runs after every IPL match and display the totals after Match-50, Match-100, and Match-200.

```sql
USE sql_cx;

SELECT *
FROM(
SELECT
CONCAT('Match-',CAST(ROW_NUMBER() OVER(ORDER BY ID) AS CHAR)) AS match_no,
SUM(batsman_run) AS runs_scored,
SUM(SUM(batsman_run)) OVER(
ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
) AS career_runs
FROM ipl
WHERE batter='V kohli'
GROUP BY ID
)t
WHERE match_no='Match-50'
OR match_no='Match-100'
OR match_no='Match-200';
```

### Key Takeaways

- Running totals
- Financial reports
- Career statistics
- Sales dashboards

---

# 3. Cumulative Average

## Concept

Computes the average including every previous row.

## Problem Statement
Calculate Virat Kohli's cumulative batting average after every IPL match.

```sql
USE sql_cx;

SELECT
CONCAT('Match-',CAST(ROW_NUMBER() OVER(ORDER BY ID) AS CHAR)) AS match_no,
SUM(batsman_run) AS runs_scored,
SUM(SUM(batsman_run)) OVER w AS career_runs,
ROUND(
AVG(SUM(batsman_run)) OVER w,
2
) AS career_runs_avg
FROM ipl
WHERE batter='V kohli'
GROUP BY ID
WINDOW w AS(
ORDER BY ID
ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
);
```

### Key Takeaways

- Tracks long-term performance.
- WINDOW clause avoids repetition.

---

# 4. Running Average

## Concept

Running (Moving) Average calculates the average over a fixed-size sliding window.

## Problem Statement
Calculate Virat Kohli's rolling average over the last 10 IPL matches.

```sql
USE sql_cx;

SELECT
CONCAT('Match-',CAST(ROW_NUMBER() OVER(ORDER BY ID) AS CHAR)) AS match_no,
SUM(batsman_run) AS runs_scored,
SUM(SUM(batsman_run)) OVER w AS career_runs,
ROUND(AVG(SUM(batsman_run)) OVER w,2) AS career_runs_avg,
ROUND(
AVG(SUM(batsman_run))
OVER(
ROWS BETWEEN 9 PRECEDING AND CURRENT ROW
),2) AS rolling_avg
FROM ipl
WHERE batter='V kohli'
GROUP BY ID
WINDOW w AS(
ORDER BY ID
ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
);
```

### Key Takeaways

- Smooths noisy data.
- Highlights recent trends.
- Window size controls sensitivity.

---

# 5. Percent of Total

## Concept

Shows contribution of each value to the total.

## Problem Statement
Find the percentage contribution of each food item to Restaurant 1's total revenue.

```sql
USE zomato;

SELECT
f_name,
(total_value/SUM(total_value) OVER())*100 AS percent_of_total
FROM(
SELECT
f_id,
SUM(amount) AS total_value
FROM orders t1
JOIN order_details t2
ON t1.order_id=t2.order_id
WHERE r_id=1
GROUP BY f_id
)t
JOIN food t3
ON t.f_id=t3.f_id
ORDER BY percent_of_total DESC;
```

---

# 6. Percent Change

## Concept

Measures increase or decrease compared to previous values.

### Problem Statement 1
Calculate the quarter-over-quarter percentage change in YouTube views.

### Problem Statement 2
Calculate the week-over-week percentage change in YouTube views.

```sql
SELECT
YEAR(Date),
QUARTER(Date),
SUM(views) AS views,
(
(
SUM(views)-LAG(SUM(views))
OVER(ORDER BY YEAR(Date),QUARTER(Date))
)
/
LAG(SUM(views))
OVER(ORDER BY YEAR(Date),QUARTER(Date))
)*100 AS Percent_change
FROM youtube_views
GROUP BY YEAR(Date),QUARTER(Date);
```

Weekly example

```sql
SELECT *,
((Views-LAG(Views,7) OVER(ORDER BY Date))
/
LAG(Views,7) OVER(ORDER BY Date))*100
AS weekly_percent_change
FROM youtube_views;
```

---

# 7. Percentiles & Quantiles

## Concept

Quantiles divide ordered data into equal groups.

Examples

- Quartiles
- Deciles
- Percentiles

Difference

### PERCENTILE_CONT()

Returns interpolated value.

### PERCENTILE_DISC()

Returns actual existing value.

### Problem Statement 1
Find the branch-wise median marks using `PERCENTILE_CONT()` and `PERCENTILE_DISC()`.

### Problem Statement 2
Identify outlier students using the Interquartile Range (IQR) method.

```sql
SELECT *,
PERCENTILE_DISC(0.5)
WITHIN GROUP(ORDER BY marks)
OVER(PARTITION BY branch) AS branch_median_marks,
ROUND(
PERCENTILE_CONT(0.5)
WITHIN GROUP(ORDER BY marks)
OVER(PARTITION BY branch),
2
) AS branch_cont_marks
FROM student_marks;
```

Removing outliers

```sql
SELECT *
FROM(
SELECT *,
PERCENTILE_CONT(0.25) WITHIN GROUP(ORDER BY marks) OVER() AS Q1,
PERCENTILE_CONT(0.75) WITHIN GROUP(ORDER BY marks) OVER() AS Q3
FROM student_marks
)t
WHERE marks>Q1-(1.5*(Q3-Q1))
AND marks<Q3-(1.5*(Q3-Q1));
```

---

# 8. Segmentation using NTILE()

## Concept

NTILE() divides rows into nearly equal-sized buckets.


### Problem Statement 1
Divide students into three equal performance groups.

### Problem Statement 2
Categorize smartphones into Budget, Mid-range, and Premium segments within each brand.

```sql
SELECT *,
NTILE(3) OVER(ORDER BY marks) AS buckets
FROM student_marks;
```

Phone segmentation

```sql
SELECT
brand,
model,
price,
CASE
WHEN bucket=1 THEN 'budget'
WHEN bucket=2 THEN 'mid-range'
WHEN bucket=3 THEN 'premium'
END AS phone_type
FROM(
SELECT
brand,
model,
price,
NTILE(3)
OVER(PARTITION BY brand ORDER BY price) AS bucket
FROM smartphone_final
)t;
```

---

# 9. Cumulative Distribution

## Concept

`CUME_DIST()` returns the percentage of rows less than or equal to the current row.

## Problem Statement
Identify students whose marks fall within the top 10% of the class.

```sql
SELECT *
FROM(
SELECT *,
CUME_DIST() OVER(ORDER BY marks)
AS Percentile_Score
FROM student_marks
)t
WHERE Percentile_Score>0.90;
```

---

# 10. PARTITION BY Multiple Columns

## Concept
Partitions data by multiple columns before ranking.

## Problem Statement
For every source-destination route, find the airline offering the lowest average airfare.

```sql
SELECT *
FROM(
SELECT
source,
destination,
airline,
AVG(price) AS avg_fare,
DENSE_RANK() OVER(
PARTITION BY source,destination
ORDER BY AVG(price)
) AS rank
FROM flights
GROUP BY source,destination,airline
)t
WHERE rank<2;
```

### Key Takeaways

- Multiple columns can define partitions.
- Independent rankings for every group.
- Common in airline, logistics and sales analytics.

---

# Summary

After completing these exercises you should be comfortable with:

- Ranking within groups
- Running totals
- Cumulative averages
- Moving averages
- Percent contribution
- Growth analysis
- Percentiles
- Quartiles
- Segmentation
- Outlier detection
- Cumulative distribution
- Multi-column partitioning

These techniques are heavily used in business intelligence, finance, analytics, dashboards, reporting, and data science.


