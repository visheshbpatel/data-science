# 34 - SQL Joins Task

This task focuses on practicing SQL JOINs, aggregation functions, grouping, filtering grouped results, sorting, and self joins.

---

## 1. Find Top 10 Countries with Maximum A and D Values

```sql
USE sql_cx;

SELECT t1.Country,
       t1.Edition,
       A,
       D
FROM country_ab t1
JOIN country_cd t2
    ON t1.Country = t2.Country
    AND t1.Edition = t2.Edition
ORDER BY A DESC, D DESC
LIMIT 10;
```

---

## 2. Find Highest CL Value for 2020 for Every Region

```sql
USE sql_cx;

SELECT
    t2.Region,
    MAX(t1.CL) AS max_CL
FROM country_cl t1
INNER JOIN country_ab t2
    ON t1.Country = t2.Country
    AND t1.Edition = t2.Edition
WHERE t1.Edition = 2020
GROUP BY t2.Region
ORDER BY max_CL DESC;
```

---

## 3. Find Top 5 Most Sold Products

```sql
USE sql_cx;

SELECT
    t1.ProductID,
    t1.Name,
    SUM(t2.Quantity) AS total_sold
FROM products t1
INNER JOIN sales1 t2
    ON t1.ProductID = t2.ProductID
GROUP BY t1.ProductID, t1.Name
ORDER BY total_sold DESC
LIMIT 5;
```

---

## 4. Find Salesperson Who Sold the Most Products

```sql
USE sql_cx;

SELECT
    t1.SalesPersonID,
    t2.FirstName AS EmployeeName,
    SUM(t1.Quantity) AS total_qant_sold
FROM sales1 t1
JOIN employees t2
    ON t1.SalesPersonID = t2.EmployeeID
GROUP BY t1.SalesPersonID, t2.FirstName
ORDER BY total_qant_sold DESC
LIMIT 1;
```

---

## 5. Find Salesperson with the Highest Number of Unique Customers

```sql
USE sql_cx;

SELECT
    t1.SalesPersonID,
    t2.FirstName AS EmployeeName,
    COUNT(DISTINCT CustomerID) AS customer_count
FROM sales1 t1
JOIN employees t2
    ON t1.SalesPersonID = t2.EmployeeID
GROUP BY t1.SalesPersonID, t2.FirstName
ORDER BY customer_count DESC
LIMIT 1;
```

---

## 6. Find Top 5 Salespeople by Revenue Generated

```sql
USE sql_cx;

SELECT
    t1.SalesPersonID,
    t2.FirstName AS EmployeeName,
    ROUND(SUM(t1.Quantity * t3.Price), 2) AS revenue
FROM sales1 t1
JOIN employees t2
    ON t1.SalesPersonID = t2.EmployeeID
JOIN products t3
    ON t1.ProductID = t3.ProductID
GROUP BY t1.SalesPersonID, t2.FirstName
ORDER BY revenue DESC
LIMIT 5;
```

---

## 7. List All Customers Who Have Made More Than 10 Purchases

```sql
USE sql_cx;

SELECT
    t1.CustomerID,
    t1.FirstName,
    COUNT(*) AS purchases_count
FROM customers t1
JOIN sales1 t2
    ON t1.CustomerID = t2.CustomerID
GROUP BY t1.CustomerID, t1.FirstName
HAVING COUNT(*) > 10;
```

---

## 8. List All Salespeople Who Have Made Sales to More Than 5 Customers

```sql
USE sql_cx;

SELECT
    t2.SalesPersonID,
    t1.FirstName,
    COUNT(DISTINCT CustomerID) AS customers_count
FROM employees t1
JOIN sales1 t2
    ON t1.EmployeeID = t2.SalesPersonID
GROUP BY t2.SalesPersonID, t1.FirstName
HAVING COUNT(DISTINCT CustomerID) > 5;
```

---

## 9. List All Pairs of Customers Who Have Made Purchases with the Same Salesperson

```sql
USE sql_cx;

SELECT DISTINCT
    a.SalesPersonID,
    a.CustomerID AS Customer1,
    b.CustomerID AS Customer2
FROM sales1 a
JOIN sales1 b
    ON a.SalesPersonID = b.SalesPersonID
    AND a.CustomerID < b.CustomerID;
```

**Note:**

```sql
a.CustomerID < b.CustomerID
```

removes duplicate pairs such as:

```text
(C1, C2)
(C2, C1)
```

and self-pairs such as:

```text
(C1, C1)
(C2, C2)
```

so only unique customer pairs are returned.

---

## Key Concepts Covered

- INNER JOIN
- Self JOIN
- GROUP BY
- HAVING
- SUM()
- COUNT()
- COUNT(DISTINCT)
- MAX()
- ROUND()
- ORDER BY
- LIMIT
- DISTINCT
- Aggregate Functions