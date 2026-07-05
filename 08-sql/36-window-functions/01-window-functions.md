# Window Functions in SQL

Window functions perform calculations across a set of rows related to the current row without collapsing the result into a single row.

Unlike `GROUP BY`, window functions return a value for **every row** while still allowing aggregate calculations.

---

# Dataset

```sql
USE sql_cx;

CREATE TABLE marks (
    student_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255),
    branch VARCHAR(255),
    marks INTEGER
);

INSERT INTO marks (name, branch, marks) VALUES
('Nitish','EEE',82),
('Rishabh','EEE',91),
('Anukant','EEE',69),
('Rupesh','EEE',55),
('Shubham','CSE',78),
('Ved','CSE',43),
('Deepak','CSE',98),
('Arpan','CSE',95),
('Vinay','ECE',95),
('Ankit','ECE',88),
('Anand','ECE',81),
('Rohit','ECE',95),
('Prashant','MECH',75),
('Amit','MECH',69),
('Sunny','MECH',39),
('Gautam','MECH',51);
```

---

# Syntax of Window Function

```sql
window_function() OVER (
    PARTITION BY column_name
    ORDER BY column_name
)
```

- **PARTITION BY** → Divides rows into groups.
- **ORDER BY** → Defines the order inside each partition.
- **OVER()** → Converts an aggregate function into a window function.

---

# 1. Aggregate Functions with OVER()

Aggregate functions can be used as window functions.

Examples:

- AVG()
- SUM()
- COUNT()
- MIN()
- MAX()

Unlike `GROUP BY`, every row remains visible.

## Example: Find students scoring above their branch average

```sql
SELECT *
FROM (
    SELECT *,
           AVG(marks) OVER (PARTITION BY branch) AS branch_avg
    FROM marks
) t
WHERE marks > branch_avg;
```

### Output Concept

| Name | Branch | Marks | Branch Avg |
|------|---------|-------|------------|
| Nitish | EEE | 82 | 74.25 |
| Rishabh | EEE | 91 | 74.25 |

---

# 2. Ranking Window Functions

Ranking functions assign rankings to rows.

## Available Functions

- ROW_NUMBER()
- RANK()
- DENSE_RANK()

---

## 2.1 ROW_NUMBER()

Assigns a unique sequential number.

Duplicate values still receive different numbers.

Example:

```text
Marks

98
95
95
88
```

Result

```text
98 → 1
95 → 2
95 → 3
88 → 4
```

---

### Example: Generate Roll Numbers

```sql
SELECT *,
       CONCAT(
           branch,
           '-',
           ROW_NUMBER() OVER (
               PARTITION BY branch
               ORDER BY name
           )
       ) AS branch_roll_no
FROM marks;
```

Example Output

```text
CSE-1
CSE-2
EEE-1
EEE-2
```

---

## 2.2 RANK()

Rows with equal values receive the same rank.

The next rank is skipped.

Example

```text
Marks

98
95
95
88
```

Result

```text
98 → 1
95 → 2
95 → 2
88 → 4
```

---

## 2.3 DENSE_RANK()

Same as RANK(), but without gaps.

Example

```text
98 → 1
95 → 2
95 → 2
88 → 3
```

---

### Example: Top 2 Customers Every Month

```sql
SELECT *
FROM (
    SELECT
        MONTHNAME(date) AS month,
        user_id,
        SUM(amount) AS total,
        RANK() OVER (
            PARTITION BY MONTH(date)
            ORDER BY SUM(amount) DESC
        ) AS month_rank
    FROM orders
    GROUP BY MONTH(date), MONTHNAME(date), user_id
) t
WHERE month_rank <= 2
ORDER BY MONTH(STR_TO_DATE(month, '%M')), month_rank;
```

---

# 3. Value Window Functions

These functions return values from specific rows inside a window.

Functions

- FIRST_VALUE()
- LAST_VALUE()
- NTH_VALUE()

---

## 3.1 FIRST_VALUE()

Returns the first value in the window.

### Example: Find Branch Toppers

```sql
SELECT name, branch, marks
FROM (
    SELECT *,
           FIRST_VALUE(name) OVER w AS topper_name,
           FIRST_VALUE(marks) OVER w AS topper_marks
    FROM marks
    WINDOW w AS (
        PARTITION BY branch
        ORDER BY marks DESC
    )
) t
WHERE name = topper_name
  AND marks = topper_marks;
```

---

## 3.2 LAST_VALUE()

Returns the last value inside the window.

**Important**

By default, `LAST_VALUE()` only looks up to the current row.

To get the true last row, specify the frame:

```sql
ROWS BETWEEN UNBOUNDED PRECEDING
     AND UNBOUNDED FOLLOWING
```

### Example: Find Lowest Scoring Student in Every Branch

```sql
SELECT name, branch, marks
FROM (
    SELECT *,
           LAST_VALUE(name) OVER (
               PARTITION BY branch
               ORDER BY marks DESC
               ROWS BETWEEN UNBOUNDED PRECEDING
               AND UNBOUNDED FOLLOWING
           ) AS last_student
    FROM marks
) t
WHERE name = last_student;
```

---

## 3.3 NTH_VALUE()

Returns the nth row of the window.

Example:

```sql
SELECT *,
       NTH_VALUE(name, 2) OVER (
           PARTITION BY branch
           ORDER BY marks DESC
           ROWS BETWEEN UNBOUNDED PRECEDING
           AND UNBOUNDED FOLLOWING
       ) AS second_topper
FROM marks;
```

---

# 4. LEAD() and LAG()

These functions access previous or next rows.

---

## LAG()

Returns the previous row value.

```text
100
120
150
```

LAG()

```text
NULL
100
120
```

---

## LEAD()

Returns the next row value.

```text
100
120
150
```

LEAD()

```text
120
150
NULL
```

---

## Example: Month-over-Month Revenue Growth

```sql
SELECT
    MONTHNAME(date) AS month,
    SUM(amount) AS revenue,

    ROUND(
        (
            (
                SUM(amount) -
                LAG(SUM(amount)) OVER (
                    ORDER BY MONTH(date)
                )
            )
            /
            LAG(SUM(amount)) OVER (
                ORDER BY MONTH(date)
            )
        ) * 100,
        2
    ) AS revenue_growth_percent

FROM orders
GROUP BY MONTH(date), MONTHNAME(date)
ORDER BY MONTH(date);
```

---

# Frames in Window Functions

A **Frame** specifies which rows inside a partition are considered for the calculation.

Syntax

```sql
ROWS BETWEEN frame_start AND frame_end
```

Common Frames

### Current Row

```sql
ROWS BETWEEN CURRENT ROW
AND CURRENT ROW
```

Only the current row.

---

### Running Total

```sql
ROWS BETWEEN UNBOUNDED PRECEDING
AND CURRENT ROW
```

Includes all previous rows and the current row.

---

### Entire Partition

```sql
ROWS BETWEEN UNBOUNDED PRECEDING
AND UNBOUNDED FOLLOWING
```

Includes every row in the partition.

This frame is commonly used with:

- LAST_VALUE()
- NTH_VALUE()

---

# Difference Between GROUP BY and Window Functions

| GROUP BY | Window Function |
|----------|-----------------|
| Returns one row per group | Returns every row |
| Aggregates data | Performs calculations without collapsing rows |
| Cannot access original rows | Original rows remain visible |
| Used for summaries | Used for ranking, running totals, comparisons, analytics |

---

# Common Window Functions

| Category | Functions |
|-----------|-----------|
| Aggregate | AVG(), SUM(), COUNT(), MAX(), MIN() |
| Ranking | ROW_NUMBER(), RANK(), DENSE_RANK() |
| Value | FIRST_VALUE(), LAST_VALUE(), NTH_VALUE() |
| Navigation | LEAD(), LAG() |

---

# Key Takeaways

- Window functions perform calculations without reducing the number of rows.
- `OVER()` converts aggregate functions into window functions.
- `PARTITION BY` creates independent groups.
- `ORDER BY` defines row order inside each partition.
- `ROW_NUMBER()` always generates unique numbers.
- `RANK()` skips ranks after ties.
- `DENSE_RANK()` does not skip ranks.
- `FIRST_VALUE()` returns the first row in a window.
- `LAST_VALUE()` often requires an explicit frame.
- `NTH_VALUE()` returns the nth value from the window.
- `LEAD()` accesses the next row.
- `LAG()` accesses the previous row.
- Frames control which rows participate in a window calculation.