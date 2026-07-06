
# Window Functions in SQL

> **Comprehensive Notes (Partially condensed due to generation limits)**

## What are Window Functions?

Window functions are analytical SQL functions that perform calculations across a set of rows related to the current row, called a **window**.

Unlike `GROUP BY`, window functions **do not collapse rows**. They return a calculated value for every row while preserving the original dataset.

A window is defined using the `OVER()` clause.

## Window Specification

```sql
window_function() OVER(
    PARTITION BY column_name
    ORDER BY column_name
    ROWS BETWEEN frame_start AND frame_end
)
```

### OVER()

Converts an aggregate function into a window function and defines the window.

### PARTITION BY

Divides rows into independent groups.

### ORDER BY

Defines the order inside each partition.

### ROWS / Frame Clause

Defines which rows participate in the calculation.

---

## Aggregate Window Functions

- AVG()
- SUM()
- COUNT()
- MIN()
- MAX()

Example:

```sql
SELECT *,
       AVG(marks) OVER(PARTITION BY branch) AS branch_avg
FROM marks;
```

---

## Ranking Functions

### ROW_NUMBER()

Unique sequential numbers.

### RANK()

Same rank for ties, skips numbers.

### DENSE_RANK()

Same rank for ties, no skipped numbers.

---

## Value Functions

### FIRST_VALUE()

Returns the first value.

### LAST_VALUE()

Returns the last value.

**Important**

Always specify

```sql
ROWS BETWEEN UNBOUNDED PRECEDING
AND UNBOUNDED FOLLOWING
```

when you need the actual last row.

### NTH_VALUE()

Returns the nth value.

---

## Navigation Functions

### LEAD()

Returns the next row.

### LAG()

Returns the previous row.

---

# Frame Clause

A frame is a subset of rows within a partition.

## Frame Boundaries

### UNBOUNDED PRECEDING

Beginning of partition.

### UNBOUNDED FOLLOWING

End of partition.

### CURRENT ROW

Current row.

### n PRECEDING

n rows before current row.

### n FOLLOWING

n rows after current row.

---

## Common Frames

### Running Total

```sql
ROWS BETWEEN UNBOUNDED PRECEDING
AND CURRENT ROW
```

All rows from the beginning to the current row.

### Entire Partition

```sql
ROWS BETWEEN UNBOUNDED PRECEDING
AND UNBOUNDED FOLLOWING
```

All rows in the partition.

### Previous + Current + Next

```sql
ROWS BETWEEN 1 PRECEDING
AND 1 FOLLOWING
```

Previous row, current row and next row.

### Sliding Window

```sql
ROWS BETWEEN 3 PRECEDING
AND 2 FOLLOWING
```

Three previous rows, current row and two following rows.

---

## GROUP BY vs Window Functions

| GROUP BY | Window Functions |
|----------|------------------|
| Collapses rows | Keeps every row |
| Summary | Analytical calculations |
| One row per group | One value per row |

---

## Common Use Cases

- Ranking
- Running totals
- Moving averages
- Previous/Next row comparison
- Month-over-month growth
- Top-N per category

---

## Best Practices

- Use GROUP BY for summaries.
- Use window functions when original rows are needed.
- Always think about PARTITION BY first.
- ORDER BY determines processing order.
- LAST_VALUE usually requires an explicit frame.

---

## Key Takeaways

- Window functions preserve rows.
- OVER() defines the window.
- PARTITION BY creates groups.
- ORDER BY sorts rows inside each group.
- ROW_NUMBER, RANK and DENSE_RANK are ranking functions.
- FIRST_VALUE, LAST_VALUE and NTH_VALUE return specific values.
- LEAD and LAG access adjacent rows.
- Frames determine the rows included in calculations.
