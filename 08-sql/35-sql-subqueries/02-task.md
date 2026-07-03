# 34 - SQL Subqueries

This section contains practice problems focused on SQL Subqueries. The tasks cover scalar subqueries, nested subqueries, derived tables, aggregate functions, filtering, grouping, and analytical comparisons using Olympic and Insurance datasets.

## Concepts Covered

* Scalar Subqueries
* Nested Subqueries
* Subqueries in `WHERE`
* Subqueries in `FROM` (Derived Tables)
* Aggregate Functions (`AVG()`, `COUNT()`)
* `IN` Operator
* `GROUP BY`
* `HAVING`
* `JOIN`
* Multi-level Filtering
* Analytical Comparisons

---

## Tasks

### 1. Gold Medalists Above Average Height (2008 Olympics)

Display the names of athletes who won a gold medal in the 2008 Olympics and whose height is greater than the average height of all athletes in the 2008 Olympics.

```sql
USE sql_cx;

SELECT DISTINCT Name, Height, Year, Medal
FROM athlete_events
WHERE Year = 2008
  AND Medal = 'Gold'
  AND Height > (
        SELECT AVG(Height)
        FROM athlete_events
        WHERE Year = 2008
  );
```

---

### 2. Basketball Medalists Below Average Weight (2016 Olympics)

Display the names of athletes who won a medal in Basketball during the 2016 Olympics and whose weight is less than the average weight of all medal winners in the 2016 Olympics.

```sql
USE sql_cx;

SELECT Name, Weight, Year, Medal
FROM athlete_events
WHERE Medal IN ('Gold', 'Silver', 'Bronze')
  AND Year = 2016
  AND Sport = 'Basketball'
  AND Weight < (
        SELECT AVG(Weight)
        FROM athlete_events
        WHERE Medal IN ('Gold', 'Silver', 'Bronze')
          AND Year = 2016
  );
```

---

### 3. Swimming Medalists in Both 2008 and 2016 Olympics

Display the names of athletes who won a medal in Swimming in both the 2008 and 2016 Olympics.

```sql
USE sql_cx;

SELECT DISTINCT Name
FROM athlete_events
WHERE Medal IS NOT NULL
  AND Sport = 'Swimming'
  AND Year = 2016
  AND Name IN (
        SELECT DISTINCT Name
        FROM athlete_events
        WHERE Medal IS NOT NULL
          AND Sport = 'Swimming'
          AND Year = 2008
  );
```

---

### 4. Countries Winning More Than 50 Medals in a Single Year

Display the names of countries that won more than 50 medals in a single Olympic year.

```sql
USE sql_cx;

SELECT DISTINCT region
FROM noc_regions t1
JOIN (
    SELECT NOC
    FROM athlete_events
    WHERE Medal IS NOT NULL
    GROUP BY NOC, Year
    HAVING COUNT(*) > 50
) t2
ON t1.NOC = t2.NOC;
```

---

### 5. Athletes Winning Medals in Multiple Sports in the Same Year

Display the names of athletes who won medals in more than one sport during the same year.

```sql
USE sql_cx;

SELECT DISTINCT Name
FROM (
    SELECT Name, Year
    FROM athlete_events
    WHERE Medal IS NOT NULL
    GROUP BY Name, Year
    HAVING COUNT(DISTINCT Sport) > 1
) t;
```

---

### 6. Average Weight Difference Between Male and Female Medalists

Calculate the average weight difference between male and female athletes who won medals in the same event.

```sql
USE sql_cx;

SELECT ROUND(
         AVG(
             ABS(m.avg_male_weight - f.avg_female_weight)
         ), 2
       ) AS avg_weight_difference
FROM (
    SELECT Event,
           AVG(Weight) AS avg_male_weight
    FROM athlete_events
    WHERE Medal IS NOT NULL
      AND Sex = 'M'
      AND Weight IS NOT NULL
    GROUP BY Event
) m
JOIN (
    SELECT Event,
           AVG(Weight) AS avg_female_weight
    FROM athlete_events
    WHERE Medal IS NOT NULL
      AND Sex = 'F'
      AND Weight IS NOT NULL
    GROUP BY Event
) f
ON m.Event = f.Event;
```

---

### 7. Claims Above Average for Smokers with Children in Southeast Region

Find the number of patients whose claim amount is greater than the average claim amount of smokers with at least one child from the southeast region.

```sql
USE sql_cx;

SELECT COUNT(*) AS claims
FROM insurance_data
WHERE claim > (
        SELECT AVG(claim)
        FROM insurance_data
        WHERE smoker = 'Yes'
          AND children >= 1
          AND region = 'southeast'
);
```

---

### 8. Claims Above Average for Non-Smokers with High BMI

Find the number of patients whose claim amount exceeds the average claim amount of non-smokers whose BMI is greater than the average BMI of patients with at least one child.

```sql
USE sql_cx;

SELECT COUNT(*)
FROM insurance_data
WHERE claim > (
        SELECT AVG(claim)
        FROM insurance_data
        WHERE smoker = 'No'
          AND bmi > (
                SELECT AVG(bmi)
                FROM insurance_data
                WHERE children >= 1
          )
);
```

---

### 9. Claims Above Average for High-BMI Patients in a Specific Group

Find the number of patients whose claim amount exceeds the average claim amount of patients whose BMI is greater than the average BMI of diabetic patients with at least one child from the southwest region.

```sql
USE sql_cx;

SELECT COUNT(*)
FROM insurance_data
WHERE claim > (
        SELECT AVG(claim)
        FROM insurance_data
        WHERE bmi > (
                SELECT AVG(bmi)
                FROM insurance_data
                WHERE diabetic = 'Yes'
                  AND children >= 1
                  AND region = 'southwest'
        )
);
```

---

### 10. Average Claim Difference Between Smokers and Non-Smokers

Calculate the difference in average claim amounts between smokers and non-smokers having the same BMI and number of children.

```sql
USE sql_cx;

SELECT ROUND(
         AVG(s.avg_claim - n.avg_claim),
         2
       ) AS avg_claim_diff
FROM (
    SELECT bmi,
           children,
           AVG(claim) AS avg_claim
    FROM insurance_data
    WHERE smoker = 'Yes'
    GROUP BY bmi, children
) s
JOIN (
    SELECT bmi,
           children,
           AVG(claim) AS avg_claim
    FROM insurance_data
    WHERE smoker = 'No'
    GROUP BY bmi, children
) n
ON s.bmi = n.bmi
AND s.children = n.children;
```

---

## Key Takeaways

* Scalar subqueries return a single value and are commonly used for comparisons.
* Nested subqueries allow multi-level filtering and analytical calculations.
* Derived tables enable aggregation before performing joins.
* Aggregate functions can be combined with subqueries for advanced analysis.
* `GROUP BY` and `HAVING` are frequently used with subqueries to filter grouped data.
* Subqueries can be used to compare records against dynamic benchmarks such as averages and counts.
* Analytical SQL problems often require combining aggregation, filtering, and joins to derive insights.
