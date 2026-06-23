# SQL DML Commands - Practice Task

This folder contains solutions to SQL DML practice questions performed on an insurance claims dataset.

The goal of this exercise is to practice:

* Data Retrieval (`SELECT`)
* Filtering (`WHERE`)
* Aggregation (`COUNT`, `SUM`, `AVG`, `MIN`, `MAX`)
* Conditional Operators (`BETWEEN`, `IN`, `AND`, `OR`)
* Updating Records (`UPDATE`)
* Deleting Records (`DELETE`)
* Working with Unique Values (`DISTINCT`)

## Dataset

**Dataset:** Insurance Claim Analysis Dataset

### Columns

| Column        | Description               |
| ------------- | ------------------------- |
| PatientID     | Unique patient identifier |
| age           | Age of patient            |
| gender        | Male/Female               |
| bmi           | Body Mass Index           |
| bloodpressure | Blood pressure            |
| diabetic      | Diabetic status           |
| children      | Number of children        |
| smoker        | Smoking status            |
| region        | Patient region            |
| claim         | Insurance claim amount    |

---

## Tasks Performed

### 1. Show records of male patients from southwest region

```sql id="r5l7aq"
SELECT *
FROM insurance_data
WHERE gender = 'male'
  AND region = 'southwest';
```

---

### 2. Show all records having BMI between 30 and 45

```sql id="mimfkj"
SELECT *
FROM insurance_data
WHERE bmi BETWEEN 30 AND 45;
```

---

### 3. Show minimum and maximum blood pressure of diabetic smokers

```sql id="vrrr92"
SELECT
    MIN(bloodpressure) AS MinBP,
    MAX(bloodpressure) AS MaxBP
FROM insurance_data
WHERE smoker = 'Yes'
  AND diabetic = 'Yes';
```

---

### 4. Find number of unique patients not from southwest region

```sql id="uobq5r"
SELECT COUNT(DISTINCT PatientID) AS UniquePatients
FROM insurance_data
WHERE region <> 'southwest';
```

---

### 5. Find total claim amount from male smokers

```sql id="hjz4e8"
SELECT SUM(claim) AS TotalClaimAmount
FROM insurance_data
WHERE smoker = 'Yes'
  AND gender = 'male';
```

---

### 6. Select all records from south region

```sql id="mww70v"
SELECT *
FROM insurance_data
WHERE region IN ('southeast', 'southwest');
```

---

### 7. Find number of patients having normal blood pressure (90–120)

```sql id="szg9l6"
SELECT COUNT(DISTINCT PatientID) AS NormalBloodPressure
FROM insurance_data
WHERE bloodpressure BETWEEN 90 AND 120;
```

---

### 8. Find number of patients below 17 years having normal blood pressure

Formula used:

```text id="6z5rbo"
Lower Limit = 80 + (age × 2)
Upper Limit = 100 + (age × 2)
```

```sql id="0m6v4v"
SELECT COUNT(DISTINCT PatientID) AS NormalBloodPressure
FROM insurance_data
WHERE age < 17
  AND bloodpressure BETWEEN
      (80 + (age * 2))
      AND
      (100 + (age * 2));
```

> Note: The provided dataset does not contain patients below 17 years of age, therefore the result may be 0.

---

### 9. Find average claim amount for non-smoking diabetic female patients

```sql id="wpp9bl"
SELECT AVG(claim) AS AverageClaimAmount
FROM insurance_data
WHERE gender = 'female'
  AND smoker = 'No'
  AND diabetic = 'Yes';
```

---

### 10. Update claim amount of patient with PatientID = 1234

```sql id="xjlwmx"
UPDATE insurance_data
SET claim = 5000
WHERE PatientID = 1234;
```

Verification:

```sql id="o3m9tz"
SELECT *
FROM insurance_data
WHERE PatientID = 1234;
```

---

### 11. Delete records of smokers having no children

```sql id="fgz3v5"
DELETE FROM insurance_data
WHERE smoker = 'Yes'
  AND children = 0;
```

---

## Concepts Practiced

* SELECT
* WHERE
* AND / OR
* IN
* BETWEEN
* DISTINCT
* COUNT
* SUM
* AVG
* MIN
* MAX
* UPDATE
* DELETE
* Data Filtering
* Aggregate Functions
* DML Commands
