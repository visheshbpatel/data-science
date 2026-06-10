# SQL Joins

## 1. What is SQL JOIN?

A JOIN is used to combine rows from two or more tables based on a related column.

Most real-world databases store data in multiple tables. JOIN allows us to retrieve related information from those tables in a single query.

Example:

- Users table contains customer details.
- Orders table contains order details.

Using JOIN, we can get customer name along with order information.

---

## 2. Why Have Data in Multiple Tables?

Storing everything in one table creates:

- Data redundancy
- Data inconsistency
- More storage usage
- Difficult maintenance

Benefits of multiple tables:

- Better organization
- Reduced duplication
- Easier updates
- Improved scalability

This concept is called normalization.

---

## 3. Types of Joins

1. Cross Join
2. Inner Join
3. Left Join
4. Right Join
5. Full Outer Join
6. Self Join

---

## 4. Cross Join (Cartesian Product)

Returns every row of first table combined with every row of second table.

Formula:

```text
Rows Returned =
Rows in Table A × Rows in Table B
```

### Query

```sql
SELECT *
FROM users t1
CROSS JOIN groups t2;
```

---

## 5. Inner Join

Returns only matching rows from both tables.

### Syntax

```sql
SELECT *
FROM table1 t1
INNER JOIN table2 t2
ON t1.id = t2.id;
```

### Example

```sql
SELECT *
FROM membership t1
INNER JOIN users t2
ON t1.user_id = t2.user_id;
```

---

## 6. Left Join

Returns:

- All rows from left table
- Matching rows from right table

### Example

```sql
SELECT *
FROM membership t1
LEFT JOIN users t2
ON t1.user_id = t2.user_id;
```

---

## 7. Right Join

Returns:

- All rows from right table
- Matching rows from left table

### Example

```sql
SELECT *
FROM membership t1
RIGHT JOIN users t2
ON t1.user_id = t2.user_id;
```

---

## 8. Full Outer Join

Returns:

- All matching rows
- All non-matching rows from both tables

MySQL does not directly support FULL OUTER JOIN.

### MySQL Trick

```sql
SELECT *
FROM membership t1
LEFT JOIN users t2
ON t1.user_id = t2.user_id

UNION

SELECT *
FROM membership t1
RIGHT JOIN users t2
ON t1.user_id = t2.user_id;
```

---

# SQL Hands-on on JOIN

## Cross Join

```sql
SELECT *
FROM users t1
CROSS JOIN groups t2;
```

---

## Inner Join

```sql
SELECT *
FROM membership t1
INNER JOIN users t2
ON t1.user_id = t2.user_id;
```

---

## Left Join

```sql
SELECT *
FROM membership t1
LEFT JOIN users t2
ON t1.user_id = t2.user_id;
```

---

## Right Join

```sql
SELECT *
FROM membership t1
RIGHT JOIN users t2
ON t1.user_id = t2.user_id;
```

---

This section demonstrates the practical implementation of different types of joins and set operations using sample tables.

---

## 1. Cross Join

### Query

```sql
SELECT *
FROM sql_cx.users t1
CROSS JOIN sql_cx.groups t2;
```

### Explanation

Every row from `users` is combined with every row from `groups`.

Formula:

```text
Total Rows = Rows in users × Rows in groups
```

---

## 2. Inner Join

### Query

```sql
SELECT *
FROM sql_cx.membership t1
INNER JOIN sql_cx.users t2
ON t1.user_id = t2.user_id;
```

### Explanation

Returns only matching records from both tables.

---

## 3. Left Join

### Query

```sql
SELECT *
FROM sql_cx.membership t1
LEFT JOIN sql_cx.users t2
ON t1.user_id = t2.user_id;
```

### Explanation

Returns:

- All rows from membership
- Matching rows from users

---

## 4. Right Join

### Query

```sql
SELECT *
FROM sql_cx.membership t1
RIGHT JOIN sql_cx.users t2
ON t1.user_id = t2.user_id;
```

### Explanation

Returns:

- All rows from users
- Matching rows from membership

---

## 5. Full Outer Join (MySQL Trick)

### Query

```sql
SELECT *
FROM sql_cx.membership t1
LEFT JOIN sql_cx.users t2
ON t1.user_id = t2.user_id

UNION

SELECT *
FROM sql_cx.membership t1
RIGHT JOIN sql_cx.users t2
ON t1.user_id = t2.user_id;
```

### Explanation

MySQL does not support FULL OUTER JOIN directly.

We combine:

- LEFT JOIN
- RIGHT JOIN

using UNION.

---

## 6. UNION

### Query

```sql
SELECT *
FROM sql_cx.person1

UNION

SELECT *
FROM sql_cx.person2;
```

### Explanation

Combines rows and removes duplicates.

---

## 7. UNION ALL

### Query

```sql
SELECT *
FROM sql_cx.person1

UNION ALL

SELECT *
FROM sql_cx.person2;
```

### Explanation

Combines rows and keeps duplicates.

---

## 8. INTERSECT

### Query

```sql
SELECT *
FROM sql_cx.person1

INTERSECT

SELECT *
FROM sql_cx.person2;
```

### Explanation

Returns only common rows.

---

## 9. EXCEPT

### Query

```sql
SELECT *
FROM sql_cx.person1

EXCEPT

SELECT *
FROM sql_cx.person2;
```

### Explanation

Returns rows from first table that are not present in second table.

---

## 10. Self Join

### Query

```sql
SELECT *
FROM sql_cx.users t1
JOIN sql_cx.users t2
ON t1.emergency_contact = t2.user_id;
```

### Explanation

A table is joined with itself.

Used when rows inside the same table have relationships.

---

## 11. Joining on More Than One Column

### Query

```sql
SELECT *
FROM sql_cx.students t1
JOIN sql_cx.class t2
ON t1.class_id = t2.class_id
AND t1.enrollment_year = t2.class_year;
```

### Explanation

Both conditions must match.

This is called a composite join condition.

---

# 9. Set Operations

## UNION

Combines results and removes duplicates.

```sql
SELECT *
FROM person1

UNION

SELECT *
FROM person2;
```

---

## UNION ALL

Combines results and keeps duplicates.

```sql
SELECT *
FROM person1

UNION ALL

SELECT *
FROM person2;
```

---

## INTERSECT

Returns common rows.

```sql
SELECT *
FROM person1

INTERSECT

SELECT *
FROM person2;
```

---

## EXCEPT

Returns rows from first table that are not present in second table.

```sql
SELECT *
FROM person1

EXCEPT

SELECT *
FROM person2;
```

---

## 10. Self Join

A table joined with itself.

Used when relationship exists inside same table.

Example:

Employee and Manager

### Query

```sql
SELECT *
FROM users t1
JOIN users t2
ON t1.emergency_contact = t2.user_id;
```

---

## 11. Joining on More Than One Column

Sometimes one column is not enough.

### Query

```sql
SELECT *
FROM students t1
JOIN class t2
ON t1.class_id = t2.class_id
AND t1.enrollment_year = t2.class_year;
```

---

## 12. Joining More Than Two Tables

### Find Order Information and Customer Name

```sql
SELECT t1.order_id,
       t1.amount,
       t1.profit,
       t3.name
FROM order_details t1
JOIN orders t2
ON t1.order_id = t2.order_id
JOIN users_ t3
ON t2.user_id = t3.user_id;
```

### Concepts Used

- Multiple JOINs
- Foreign Keys
- Data Linking

---

## 13. Filtering Columns

### Problem 1

Find order_id, customer name and city.

```sql
SELECT t1.order_id,
       t2.name,
       t2.city
FROM orders t1
JOIN users_ t2
ON t1.user_id = t2.user_id;
```

---

### Problem 2

Find order_id and product category.

```sql
SELECT t1.order_id,
       t2.vertical
FROM order_details t1
JOIN category t2
ON t1.category_id = t2.category_id;
```

---

## 14. Filtering Rows

### Problem 1

Find all orders placed in Pune.

```sql
SELECT *
FROM orders t1
JOIN users_ t2
ON t1.user_id = t2.user_id
WHERE t2.city = 'Pune';
```

---

### Problem 2

Find all orders under Chairs category.

```sql
SELECT *
FROM order_details t1
JOIN category t2
ON t1.category_id = t2.category_id
WHERE t2.vertical = 'Chairs';
```

---

## 15. Query Execution Order in JOIN

```text
FROM
JOIN
ON
WHERE
GROUP BY
HAVING
SELECT
ORDER BY
LIMIT
```

Understanding this order is extremely important.

---

# 16. Practice Questions

## Problem 1

### Find All Profitable Orders

```sql
SELECT t1.order_id,
       SUM(t2.profit) AS profit
FROM orders t1
JOIN order_details t2
ON t1.order_id = t2.order_id
GROUP BY t1.order_id
HAVING SUM(t2.profit) > 0;
```

---

## Problem 2

### Customer Who Has Placed Maximum Orders

```sql
SELECT t2.name,
       COUNT(*) AS num_orders
FROM orders t1
JOIN users_ t2
ON t1.user_id = t2.user_id
GROUP BY t2.name
ORDER BY num_orders DESC
LIMIT 1;
```

---

## Problem 3

### Most Profitable Category

```sql
SELECT t2.vertical,
       SUM(t1.profit) AS profit
FROM order_details t1
JOIN category t2
ON t1.category_id = t2.category_id
GROUP BY t2.vertical
ORDER BY profit DESC
LIMIT 1;
```

---

## Problem 4

### Most Profitable State

```sql
SELECT t3.state,
       SUM(t2.profit) AS profit
FROM orders t1
JOIN order_details t2
ON t1.order_id = t2.order_id
JOIN users_ t3
ON t1.user_id = t3.user_id
GROUP BY t3.state
ORDER BY profit DESC
LIMIT 1;
```

---

## Problem 5

### Categories with Profit Greater Than 5000

```sql
SELECT t1.vertical,
       SUM(t2.profit) AS profit
FROM category t1
JOIN order_details t2
ON t1.category_id = t2.category_id
GROUP BY t1.vertical
HAVING SUM(t2.profit) > 5000;
```

---

## Common Mistakes

### Forgetting ON Clause

Wrong:

```sql
SELECT *
FROM orders
JOIN users_;
```

---

### Using WHERE Instead of ON

Join conditions should generally go inside ON.

---

### Confusing LEFT and RIGHT JOIN

Remember:

- LEFT JOIN keeps all rows from left table
- RIGHT JOIN keeps all rows from right table

---

## Quick Revision

### Types of Joins

```text
Cross Join
Inner Join
Left Join
Right Join
Full Outer Join
Self Join
```

### Set Operations

```text
UNION
UNION ALL
INTERSECT
EXCEPT
```

### Execution Order

```text
FROM
JOIN
ON
WHERE
GROUP BY
HAVING
SELECT
ORDER BY
LIMIT
```
