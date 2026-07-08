# SQL Window Functions - Tasks

> Practice problems demonstrating real-world applications of SQL Window Functions using the **insurance_data** dataset.

## Dataset

* **Database:** `sql_cx`
* **Table:** `insurance_data`

---

# 1. Top 5 Patients with the Highest Insurance Claims

### Objective

Find the top 5 patients who claimed the highest insurance amounts.

### Using ORDER BY

```sql
USE sql_cx;

SELECT *
FROM insurance_data
ORDER BY claim DESC
LIMIT 5;
```

### Using ROW_NUMBER()

```sql
USE sql_cx;

SELECT *
FROM (
    SELECT *,
           ROW_NUMBER() OVER (ORDER BY claim DESC) AS rn
    FROM insurance_data
) t
WHERE rn <= 5;
```

---

# 2. Average Insurance Claim Based on Number of Children

### Objective

Calculate the average insurance claim amount for patients grouped by the number of children they have.

### Using GROUP BY

```sql
USE sql_cx;

SELECT children,
       ROUND(AVG(claim), 2) AS avg_claim
FROM insurance_data
GROUP BY children;
```

### Using Window Function

```sql
USE sql_cx;

SELECT *,
       ROUND(
           AVG(claim) OVER (PARTITION BY children),
           2
       ) AS avg_claim
FROM insurance_data;
```

---

# 3. Highest and Lowest Claim in Each Region

### Objective

Find the highest and lowest insurance claim amount within every region.

### Using GROUP BY

```sql
USE sql_cx;

SELECT region,
       MAX(claim) AS highest_claim,
       MIN(claim) AS lowest_claim
FROM insurance_data
GROUP BY region;
```

### Using Window Function

```sql
USE sql_cx;

SELECT *,
       MAX(claim) OVER (PARTITION BY region) AS highest_claim,
       MIN(claim) OVER (PARTITION BY region) AS lowest_claim
FROM insurance_data;
```

---

# 4. Percentage of Smokers in Each Age Group

### Objective

Calculate the percentage of smokers for every age group.

### Using GROUP BY

```sql
USE sql_cx;

SELECT age,
       ROUND(
           (COUNT(IF(smoker = 'Yes', 1, NULL)) / COUNT(*)) * 100,
           2
       ) AS smoker_percentage
FROM insurance_data
GROUP BY age;
```

### Using Window Function

```sql
USE sql_cx;

SELECT DISTINCT
       age,
       ROUND(
           (
               SUM(IF(smoker = 'Yes', 1, 0))
               OVER (PARTITION BY age)
               /
               COUNT(*) OVER (PARTITION BY age)
           ) * 100,
           2
       ) AS smoker_percentage
FROM insurance_data;
```

---

# 5. Difference Between Current Claim and First Claim of Each Patient

### Objective

Find the difference between each patient's current claim and their first insurance claim.

```sql
USE sql_cx;

SELECT *,
       claim - FIRST_VALUE(claim)
       OVER (PARTITION BY PatientID) AS claim_difference
FROM insurance_data;
```

> **Note:** This question is **not applicable** to the provided dataset because every `PatientID` appears only once. Therefore, the first claim and current claim are the same, making the difference **0** for all records.

---

# 6. Difference from Average Claim of Patients with Same Number of Children

### Objective

Calculate how much each patient's claim differs from the average claim of patients having the same number of children.

```sql
USE sql_cx;

SELECT *,
       ROUND(
           claim - AVG(claim)
           OVER (PARTITION BY children),
           2
       ) AS claim_difference
FROM insurance_data;
```

---

# 7. Highest BMI Patient in Each Region

### Objective

Find the patient having the highest BMI in every region and display their rank.

```sql
USE sql_cx;

SELECT *
FROM (
    SELECT *,
           RANK() OVER (
               PARTITION BY region
               ORDER BY bmi DESC
           ) AS bmi_rank
    FROM insurance_data
    WHERE region <> ''
) t
WHERE bmi_rank = 1;
```

---

# 8. Difference Between Patient's Claim and Highest BMI Patient's Claim

### Objective

Calculate the difference between each patient's claim and the claim of the patient having the highest BMI within the same region.

```sql
USE sql_cx;

SELECT *,
       ROUND(
           claim -
           FIRST_VALUE(claim)
           OVER (
               PARTITION BY region
               ORDER BY bmi DESC
           ),
           2
       ) AS claim_difference
FROM insurance_data;
```

---

# 9. Difference from Highest Claim Within Same BMI, Smoker Status and Region

### Objective

For each patient, calculate the difference between their claim and the highest claim among patients having the same BMI, smoker status, and region.

Return the result in descending order of claim difference.

```sql
USE sql_cx;

SELECT *,
       ROUND(
           claim -
           FIRST_VALUE(claim)
           OVER (
               PARTITION BY bmi, smoker, region
               ORDER BY claim DESC
           ),
           2
       ) AS claim_difference
FROM insurance_data
ORDER BY claim_difference DESC;
```

---

# 10. Maximum BMI Among the Next Three Patients

### Objective

For every patient, find the maximum BMI value among the next three records when ordered by age.

```sql
USE sql_cx;

SELECT *,
       MAX(bmi)
       OVER (
           ORDER BY age
           ROWS BETWEEN 1 FOLLOWING
           AND 3 FOLLOWING
       ) AS max_next_3_bmi
FROM insurance_data;
```

---

# 11. Rolling Average of Previous Two Claims

### Objective

Calculate the rolling average of the previous two claim amounts.

```sql
USE sql_cx;

SELECT *,
       ROUND(
           AVG(claim)
           OVER (
               ORDER BY claim
               ROWS BETWEEN 2 PRECEDING
               AND 1 PRECEDING
           ),
           2
       ) AS rolling_avg
FROM insurance_data;
```

---

# 12. First Claim Amount by Gender and Region

### Objective

Find the first insurance claim amount for male and female patients within each region, ordered by age, considering only non-diabetic patients whose BMI lies between 25 and 30.

```sql
USE sql_cx;

SELECT *,
       FIRST_VALUE(claim)
       OVER (
           PARTITION BY gender, region
           ORDER BY age
       ) AS first_claim_amt
FROM insurance_data
WHERE diabetic = 'No'
  AND bmi BETWEEN 25 AND 30
ORDER BY gender, region, age;
```

---

# Window Functions Covered

* `ROW_NUMBER()`
* `RANK()`
* `FIRST_VALUE()`
* `AVG() OVER()`
* `MAX() OVER()`
* `MIN() OVER()`
* `SUM() OVER()`
* `COUNT() OVER()`
* `PARTITION BY`
* `ORDER BY`
* `ROWS BETWEEN ...`

---

# Key Takeaways

* Window functions return a result for every row without collapsing the dataset.
* `PARTITION BY` creates logical groups while preserving all rows.
* Ranking functions are useful for identifying top-N records within groups.
* Aggregate window functions calculate averages, totals, maximums, and minimums without using `GROUP BY`.
* `FIRST_VALUE()` allows comparison with the first row in a partition.
* Frame clauses such as `ROWS BETWEEN` enable running totals, rolling averages, and moving-window calculations.
* Window functions are ideal for comparative analytics and reporting queries.
# SQL Window Functions - Tasks

> Practice problems demonstrating real-world applications of SQL Window Functions using the **insurance_data** dataset.

## Dataset

* **Database:** `sql_cx`
* **Table:** `insurance_data`

---

# 1. Top 5 Patients with the Highest Insurance Claims

### Objective

Find the top 5 patients who claimed the highest insurance amounts.

### Using ORDER BY

```sql
USE sql_cx;

SELECT *
FROM insurance_data
ORDER BY claim DESC
LIMIT 5;
```

### Using ROW_NUMBER()

```sql
USE sql_cx;

SELECT *
FROM (
    SELECT *,
           ROW_NUMBER() OVER (ORDER BY claim DESC) AS rn
    FROM insurance_data
) t
WHERE rn <= 5;
```

---

# 2. Average Insurance Claim Based on Number of Children

### Objective

Calculate the average insurance claim amount for patients grouped by the number of children they have.

### Using GROUP BY

```sql
USE sql_cx;

SELECT children,
       ROUND(AVG(claim), 2) AS avg_claim
FROM insurance_data
GROUP BY children;
```

### Using Window Function

```sql
USE sql_cx;

SELECT *,
       ROUND(
           AVG(claim) OVER (PARTITION BY children),
           2
       ) AS avg_claim
FROM insurance_data;
```

---

# 3. Highest and Lowest Claim in Each Region

### Objective

Find the highest and lowest insurance claim amount within every region.

### Using GROUP BY

```sql
USE sql_cx;

SELECT region,
       MAX(claim) AS highest_claim,
       MIN(claim) AS lowest_claim
FROM insurance_data
GROUP BY region;
```

### Using Window Function

```sql
USE sql_cx;

SELECT *,
       MAX(claim) OVER (PARTITION BY region) AS highest_claim,
       MIN(claim) OVER (PARTITION BY region) AS lowest_claim
FROM insurance_data;
```

---

# 4. Percentage of Smokers in Each Age Group

### Objective

Calculate the percentage of smokers for every age group.

### Using GROUP BY

```sql
USE sql_cx;

SELECT age,
       ROUND(
           (COUNT(IF(smoker = 'Yes', 1, NULL)) / COUNT(*)) * 100,
           2
       ) AS smoker_percentage
FROM insurance_data
GROUP BY age;
```

### Using Window Function

```sql
USE sql_cx;

SELECT DISTINCT
       age,
       ROUND(
           (
               SUM(IF(smoker = 'Yes', 1, 0))
               OVER (PARTITION BY age)
               /
               COUNT(*) OVER (PARTITION BY age)
           ) * 100,
           2
       ) AS smoker_percentage
FROM insurance_data;
```

---

# 5. Difference Between Current Claim and First Claim of Each Patient

### Objective

Find the difference between each patient's current claim and their first insurance claim.

```sql
USE sql_cx;

SELECT *,
       claim - FIRST_VALUE(claim)
       OVER (PARTITION BY PatientID) AS claim_difference
FROM insurance_data;
```

> **Note:** This question is **not applicable** to the provided dataset because every `PatientID` appears only once. Therefore, the first claim and current claim are the same, making the difference **0** for all records.

---

# 6. Difference from Average Claim of Patients with Same Number of Children

### Objective

Calculate how much each patient's claim differs from the average claim of patients having the same number of children.

```sql
USE sql_cx;

SELECT *,
       ROUND(
           claim - AVG(claim)
           OVER (PARTITION BY children),
           2
       ) AS claim_difference
FROM insurance_data;
```

---

# 7. Highest BMI Patient in Each Region

### Objective

Find the patient having the highest BMI in every region and display their rank.

```sql
USE sql_cx;

SELECT *
FROM (
    SELECT *,
           RANK() OVER (
               PARTITION BY region
               ORDER BY bmi DESC
           ) AS bmi_rank
    FROM insurance_data
    WHERE region <> ''
) t
WHERE bmi_rank = 1;
```

---

# 8. Difference Between Patient's Claim and Highest BMI Patient's Claim

### Objective

Calculate the difference between each patient's claim and the claim of the patient having the highest BMI within the same region.

```sql
USE sql_cx;

SELECT *,
       ROUND(
           claim -
           FIRST_VALUE(claim)
           OVER (
               PARTITION BY region
               ORDER BY bmi DESC
           ),
           2
       ) AS claim_difference
FROM insurance_data;
```

---

# 9. Difference from Highest Claim Within Same BMI, Smoker Status and Region

### Objective

For each patient, calculate the difference between their claim and the highest claim among patients having the same BMI, smoker status, and region.

Return the result in descending order of claim difference.

```sql
USE sql_cx;

SELECT *,
       ROUND(
           claim -
           FIRST_VALUE(claim)
           OVER (
               PARTITION BY bmi, smoker, region
               ORDER BY claim DESC
           ),
           2
       ) AS claim_difference
FROM insurance_data
ORDER BY claim_difference DESC;
```

---

# 10. Maximum BMI Among the Next Three Patients

### Objective

For every patient, find the maximum BMI value among the next three records when ordered by age.

```sql
USE sql_cx;

SELECT *,
       MAX(bmi)
       OVER (
           ORDER BY age
           ROWS BETWEEN 1 FOLLOWING
           AND 3 FOLLOWING
       ) AS max_next_3_bmi
FROM insurance_data;
```

---

# 11. Rolling Average of Previous Two Claims

### Objective

Calculate the rolling average of the previous two claim amounts.

```sql
USE sql_cx;

SELECT *,
       ROUND(
           AVG(claim)
           OVER (
               ORDER BY claim
               ROWS BETWEEN 2 PRECEDING
               AND 1 PRECEDING
           ),
           2
       ) AS rolling_avg
FROM insurance_data;
```

---

# 12. First Claim Amount by Gender and Region

### Objective

Find the first insurance claim amount for male and female patients within each region, ordered by age, considering only non-diabetic patients whose BMI lies between 25 and 30.

```sql
USE sql_cx;

SELECT *,
       FIRST_VALUE(claim)
       OVER (
           PARTITION BY gender, region
           ORDER BY age
       ) AS first_claim_amt
FROM insurance_data
WHERE diabetic = 'No'
  AND bmi BETWEEN 25 AND 30
ORDER BY gender, region, age;
```

---

# Window Functions Covered

* `ROW_NUMBER()`
* `RANK()`
* `FIRST_VALUE()`
* `AVG() OVER()`
* `MAX() OVER()`
* `MIN() OVER()`
* `SUM() OVER()`
* `COUNT() OVER()`
* `PARTITION BY`
* `ORDER BY`
* `ROWS BETWEEN ...`

---

# Key Takeaways

* Window functions return a result for every row without collapsing the dataset.
* `PARTITION BY` creates logical groups while preserving all rows.
* Ranking functions are useful for identifying top-N records within groups.
* Aggregate window functions calculate averages, totals, maximums, and minimums without using `GROUP BY`.
* `FIRST_VALUE()` allows comparison with the first row in a partition.
* Frame clauses such as `ROWS BETWEEN` enable running totals, rolling averages, and moving-window calculations.
* Window functions are ideal for comparative analytics and reporting queries.
