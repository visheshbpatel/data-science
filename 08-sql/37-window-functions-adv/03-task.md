# SQL Window Functions - Advanced (Part 2)

> Advanced SQL Window Function practice using the **Northwind** and **Drug Review** datasets.

## Overview

This document contains solutions to advanced SQL Window Function problems involving:

- Ranking
- Running Total
- Cumulative Sum
- Percentage of Total
- Year-over-Year Growth
- Median Calculation
- Running Average
- Cumulative Distribution
- LAG()
- RANK()
- DENSE_RANK()

---

# Dataset Used

## 1. Northwind Database

Tables Used:

- `nw_employees`
- `nw_orders`
- `nw_order_details`
- `nw_products`
- `nw_suppliers`

---

## 2. Drug Review Dataset

Table Used:

- `drug_clean`

---

# Question 1

## Rank employees in terms of revenue generation.

**Show:**

- Employee ID
- First Name
- Revenue
- Rank

### SQL Query

```sql
USE sql_cx;

SELECT
    t1.EmployeeID,
    t1.FirstName,
    ROUND(SUM(UnitPrice * Quantity), 2) AS revenue,
    RANK() OVER (
        ORDER BY SUM(UnitPrice * Quantity) DESC
    ) AS employee_rank
FROM nw_employees t1
JOIN nw_orders t2
    ON t1.EmployeeID = t2.EmployeeID
JOIN nw_order_details t3
    ON t2.OrderID = t3.OrderID
GROUP BY
    t1.EmployeeID,
    t1.FirstName
ORDER BY revenue DESC;
```

---

# Question 2

## Show cumulative sum of units sold for every product month-wise.

### SQL Query

```sql
USE sql_cx;

SELECT
    MONTH(t1.OrderDate) AS order_month,
    t2.ProductID,
    t3.ProductName,
    SUM(t2.Quantity) AS units_sold,
    SUM(SUM(t2.Quantity))
        OVER (
            PARTITION BY t2.ProductID
            ORDER BY MONTH(t1.OrderDate)
            ROWS BETWEEN UNBOUNDED PRECEDING
            AND CURRENT ROW
        ) AS cumulative_sum_units
FROM nw_orders t1
JOIN nw_order_details t2
    ON t1.OrderID = t2.OrderID
JOIN nw_products t3
    ON t2.ProductID = t3.ProductID
GROUP BY
    MONTH(t1.OrderDate),
    t2.ProductID,
    t3.ProductName
ORDER BY
    t2.ProductID,
    order_month;
```

---

# Question 3

## Show percentage contribution of total revenue by each supplier.

### SQL Query

```sql
USE sql_cx;

SELECT
    t2.SupplierID,
    t2.CompanyName,
    ROUND(SUM(t3.UnitPrice * Quantity),2) AS revenue,

    ROUND(
        SUM(t3.UnitPrice * Quantity)
        /
        SUM(SUM(t3.UnitPrice * Quantity)) OVER()
        *100,
        2
    ) AS percentage_of_total_revenue

FROM nw_products t1
JOIN nw_suppliers t2
ON t1.SupplierID=t2.SupplierID
JOIN nw_order_details t3
ON t1.ProductID=t3.ProductID

GROUP BY
    t2.SupplierID,
    t2.CompanyName

ORDER BY revenue DESC;
```

---

# Question 4

## Show percentage contribution of total orders by each supplier.

### SQL Query

```sql
USE sql_cx;

SELECT
    t1.SupplierID,
    t2.CompanyName,

    COUNT(DISTINCT t3.OrderID) AS total_orders,

    ROUND(
        COUNT(DISTINCT t3.OrderID)
        /
        SUM(COUNT(DISTINCT t3.OrderID)) OVER()
        *100,
        2
    ) AS percentage_of_total_orders

FROM nw_products t1
JOIN nw_suppliers t2
ON t1.SupplierID=t2.SupplierID
JOIN nw_order_details t3
ON t1.ProductID=t3.ProductID

GROUP BY
    t1.SupplierID,
    t2.CompanyName

ORDER BY percentage_of_total_orders DESC;
```

---

# Question 5

## Show year-wise quantity sold and percentage change from previous year for every product.

### SQL Query

```sql
USE sql_cx;

WITH yearly_sales AS
(
    SELECT
        t2.ProductID,
        t3.ProductName,
        YEAR(t1.OrderDate) AS order_year,
        SUM(t2.Quantity) AS total_quantity

    FROM nw_orders t1
    JOIN nw_order_details t2
    ON t1.OrderID=t2.OrderID
    JOIN nw_products t3
    ON t2.ProductID=t3.ProductID

    GROUP BY
        t2.ProductID,
        t3.ProductName,
        YEAR(t1.OrderDate)
)

SELECT
    ProductID,
    ProductName,
    order_year,
    total_quantity,

    ROUND(
        (
            total_quantity -
            LAG(total_quantity)
            OVER(
                PARTITION BY ProductID
                ORDER BY order_year
            )
        )
        /
        LAG(total_quantity)
        OVER(
            PARTITION BY ProductID
            ORDER BY order_year
        )*100,
        2
    ) AS percentage_change

FROM yearly_sales

ORDER BY
    ProductID,
    order_year;
```

---

# Question 6

## Find the average satisfaction level for On Label vs Off Label drugs for every condition.

### SQL Query

```sql
USE sql_cx;

SELECT
    `Condition`,
    Indication,
    ROUND(AVG(Satisfaction),2) AS avg_satisfaction

FROM drug_clean

GROUP BY
    `Condition`,
    Indication

ORDER BY
    `Condition`,
    Indication;
```

---

# Question 7

## Find average Ease of Use and Satisfaction for drugs priced above the median of their drug type.

### SQL Query

```sql
USE sql_cx;

WITH ranked AS
(
    SELECT *,
        ROW_NUMBER() OVER(
            PARTITION BY Type
            ORDER BY Price
        ) AS rn,

        COUNT(*) OVER(
            PARTITION BY Type
        ) AS cnt

    FROM drug_clean
),

median_price AS
(
    SELECT
        Type,
        AVG(Price) AS median_price

    FROM ranked

    WHERE rn IN
    (
        FLOOR((cnt+1)/2),
        CEIL((cnt+1)/2)
    )

    GROUP BY Type
)

SELECT
    t2.Type,

    ROUND(AVG(EaseOfUse),2) AS avg_ease_of_use,
    ROUND(AVG(Satisfaction),2) AS avg_satisfaction

FROM median_price t1
JOIN drug_clean t2
ON t1.Type=t2.Type

WHERE t2.Price>t1.median_price

GROUP BY t2.Type

ORDER BY t2.Type;
```

---

# Question 8

## Show cumulative distribution of EaseOfUse for every drug type.

### SQL Query

```sql
USE sql_cx;

SELECT
    Type,
    Drug,
    EaseOfUse,

    CUME_DIST()
    OVER(
        PARTITION BY Type
        ORDER BY EaseOfUse DESC
    ) AS cumulative_distribution

FROM drug_clean

WHERE Type IS NOT NULL
AND TRIM(Type)<>''

ORDER BY
    Type DESC,
    cumulative_distribution DESC;
```

---

# Question 9

## Find the median satisfaction level for every medical condition.

### SQL Query

```sql
USE sql_cx;

WITH ranked AS
(
    SELECT
        `Condition`,
        Satisfaction,

        ROW_NUMBER()
        OVER(
            PARTITION BY `Condition`
            ORDER BY Satisfaction
        ) AS rn,

        COUNT(*)
        OVER(
            PARTITION BY `Condition`
        ) AS cnt

    FROM drug_clean
),

median_cte AS
(
    SELECT
        `Condition`,
        AVG(Satisfaction) AS median_satisfaction

    FROM ranked

    WHERE rn IN
    (
        FLOOR((cnt+1)/2),
        CEIL((cnt+1)/2)
    )

    GROUP BY `Condition`
)

SELECT *

FROM median_cte

ORDER BY median_satisfaction DESC;
```

---

# Question 10

## Find the running average price of drugs for every medical condition.

### SQL Query

```sql
USE sql_cx;

SELECT
    `Condition`,
    Drug,
    Price,

    ROUND(
        AVG(Price)
        OVER(
            PARTITION BY `Condition`
            ORDER BY Drug
            ROWS BETWEEN UNBOUNDED PRECEDING
            AND CURRENT ROW
        ),
        2
    ) AS running_avg_price

FROM drug_clean

ORDER BY
    `Condition`,
    Drug;
```

---

# Question 11

## Calculate percentage change in reviews compared to the previous row.

### SQL Query

```sql
USE sql_cx;

SELECT
    Drug,
    Reviews,

    ROUND(
        (
            Reviews -
            LAG(Reviews)
            OVER(
                ORDER BY Reviews
            )
        )
        /
        LAG(Reviews)
        OVER(
            ORDER BY Reviews
        )*100,
        2
    ) AS percentage_change

FROM drug_clean

ORDER BY percentage_change DESC;
```

---

# Question 12

## Show percentage contribution of total satisfaction for every drug type.

### SQL Query

```sql
USE sql_cx;

SELECT
    Type,

    ROUND(
        SUM(Satisfaction),
        2
    ) AS total_satisfaction,

    ROUND(
        SUM(Satisfaction)
        /
        SUM(SUM(Satisfaction))
        OVER()
        *100,
        2
    ) AS percentage_of_total_satisfaction

FROM drug_clean

GROUP BY Type

ORDER BY
    Type DESC,
    percentage_of_total_satisfaction DESC;
```

---

# Question 13

## Show cumulative sum of effectiveness for every Condition and Drug Form.

### SQL Query

```sql
USE sql_cx;

SELECT
    `Condition`,
    Form,
    Drug,
    Effective,

    ROUND(
        SUM(Effective)
        OVER(
            PARTITION BY `Condition`, Form
            ORDER BY Drug
            ROWS BETWEEN UNBOUNDED PRECEDING
            AND CURRENT ROW
        ),
        2
    ) AS cumulative_effective

FROM drug_clean

ORDER BY
    `Condition`,
    Form,
    Drug;
```

---

# Question 14

## Rank drug types based on average Ease of Use.

### SQL Query

```sql
USE sql_cx;

SELECT
    Type,

    ROUND(
        AVG(EaseOfUse),
        2
    ) AS avg_ease_of_use,

    RANK()
    OVER(
        ORDER BY AVG(EaseOfUse) DESC
    ) AS ranking

FROM drug_clean

GROUP BY Type

ORDER BY
    ranking,
    Type DESC;
```

---

# Question 15

## Find average effectiveness of the top 3 most reviewed drugs for every condition.

### SQL Query

```sql
USE sql_cx;

WITH ranked AS
(
    SELECT
        `Condition`,
        Drug,
        Reviews,
        Effective,

        DENSE_RANK()
        OVER(
            PARTITION BY `Condition`
            ORDER BY Reviews DESC
        ) AS rn

    FROM drug_clean
)

SELECT
    `Condition`,

    ROUND(
        AVG(Effective),
        2
    ) AS avg_effectiveness

FROM ranked

WHERE rn<=3

GROUP BY `Condition`

ORDER BY `Condition`;
```

---

# Key Takeaways

During this exercise, the following SQL concepts were practiced:

- `RANK()`
- `DENSE_RANK()`
- `ROW_NUMBER()`
- `LAG()`
- `CUME_DIST()`
- `SUM() OVER()`
- `AVG() OVER()`
- Running Average
- Running Total
- Cumulative Sum
- Percentage of Total
- Percentage Change
- Year-over-Year Analysis
- Median Calculation using Window Functions
- `PARTITION BY`
- `ORDER BY` inside Window Functions
- `ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW`
- Common Table Expressions (CTEs)
- Aggregate Window Functions
- Analytical SQL Queries

