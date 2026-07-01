# SQL Grouping & Sorting - Practice Tasks

This folder contains solutions to SQL practice problems focused on grouping, aggregation, sorting, filtering grouped data, and analyzing real-world datasets.

## Concepts Practiced

* GROUP BY
* ORDER BY
* HAVING
* COUNT()
* SUM()
* AVG()
* LIMIT
* OFFSET
* Subqueries
* Multi-column Grouping
* Multi-column Sorting

---

## 1. Average Sleep Duration of Top 15 Male Candidates

Find the average sleep duration of the top 15 male candidates whose sleep duration is at least 7.5 hours.

```sql
USE sql_cx;

SELECT AVG(`Sleep duration`) AS avg_sleep
FROM (
    SELECT `Sleep duration`
    FROM sleep_efficiency
    WHERE Gender = 'Male'
      AND `Sleep duration` >= 7.5
    ORDER BY `Sleep duration` DESC
    LIMIT 15
) top_15_males;
```

---

## 2. Average Deep Sleep Time by Gender

Calculate average deep sleep time for both genders.

```sql
USE sql_cx;

SELECT Gender,
       ROUND(
           AVG(`Sleep duration` * `Deep sleep percentage` * 0.01),
           2
       ) AS avg_deep_sleep
FROM sleep_efficiency
GROUP BY Gender;
```

---

## 3. Lowest 10th to 30th Light Sleep Percentage Records

Display age, light sleep percentage and deep sleep percentage for records where deep sleep percentage is between 25 and 45.

```sql
USE sql_cx;

SELECT age,
       `Light sleep percentage`,
       `Deep sleep percentage`
FROM sleep_efficiency
WHERE `Deep sleep percentage` BETWEEN 25 AND 45
ORDER BY `Light sleep percentage` ASC
LIMIT 21 OFFSET 9;
```

---

## 4. Average Sleep Metrics by Exercise Frequency and Smoking Status

Display average deep sleep time, average light sleep time and average REM sleep time.

```sql
USE sql_cx;

SELECT `Exercise frequency`,
       `Smoking status`,
       ROUND(AVG(`Sleep duration` * `Deep sleep percentage` * 0.01), 2) AS avg_deep_sleep_time,
       ROUND(AVG(`Sleep duration` * `Light sleep percentage` * 0.01), 2) AS avg_light_sleep_time,
       ROUND(AVG(`Sleep duration` * `REM sleep percentage` * 0.01), 2) AS avg_rem_sleep_time
FROM sleep_efficiency
GROUP BY `Exercise frequency`, `Smoking status`;
```

---

## 5. Sleep Analysis Based on Awakenings

For people exercising at least 3 days a week, display average caffeine consumption, average deep sleep time and average alcohol consumption.

```sql
USE sql_cx;

SELECT Awakenings,
       ROUND(AVG(`Caffeine consumption`), 2) AS avg_caffeine_consumption,
       ROUND(AVG(`Sleep duration` * `Deep sleep percentage` * 0.01), 2) AS avg_deep_sleep_time,
       ROUND(AVG(`Alcohol consumption`), 2) AS avg_alcohol_consumption
FROM sleep_efficiency
WHERE `Exercise frequency` >= 3
GROUP BY Awakenings
ORDER BY Awakenings DESC;
```

---

## 6. Power Stations Based on Average Monitored Capacity

Display power stations whose average monitored capacity lies between 1000 and 2000 MW and occurrence count is greater than 200.

```sql
USE sql_cx;

SELECT `Power Station`,
       COUNT(*) AS occurance,
       ROUND(AVG(`Monitored Cap.(MW)`), 2) AS avg_MW
FROM powergeneration
GROUP BY `Power Station`
HAVING avg_MW BETWEEN 1000 AND 2000
   AND occurance > 200
ORDER BY avg_MW ASC;
```

---

## 7. Lowest Cost Public In-State Education States

Display top 10 states with lowest average value for years 2013, 2017 and 2021.

```sql
USE sql_cx;

SELECT State,
       COUNT(*) AS occurance,
       ROUND(AVG(Value), 2) AS avg_value
FROM college
WHERE Year IN (2013, 2017, 2021)
  AND Type = 'Public In-State'
GROUP BY State
HAVING COUNT(*) BETWEEN 6 AND 10
ORDER BY avg_value ASC
LIMIT 10;
```

---

## 8. Best States for Low Public Education Cost

Find states with lowest average tuition fee for public universities.

```sql
USE sql_cx;

SELECT State,
       ROUND(AVG(Value), 2) AS avg_tuition_fee
FROM college
WHERE Expense = 'Fees/Tuition'
  AND Type IN ('Public In-State', 'Public Out-of-State')
GROUP BY State
ORDER BY avg_tuition_fee ASC
LIMIT 10;
```

---

## 9. Second Costliest State for Private Education (2021)

Consider tuition fees and room/board charges only.

```sql
USE sql_cx;

SELECT State,
       SUM(Value) AS fees
FROM college
WHERE Type = 'Private'
  AND Year = 2021
  AND Expense IN ('Fees/Tuition', 'Room/Board')
GROUP BY State
ORDER BY fees DESC
LIMIT 1,1;
```

---

## 10. Discount Analysis by Shipment Mode and Warehouse

For male customers and high product importance, display total and average discounts.

```sql
USE sql_cx;

SELECT Mode_of_Shipment,
       Warehouse_block,
       SUM(Discount_offered) AS total_discount,
       ROUND(AVG(Discount_offered), 2) AS avg_discount
FROM shipping_ecommerce
WHERE Gender = 'M'
  AND Product_importance = 'high'
GROUP BY Mode_of_Shipment, Warehouse_block
ORDER BY Mode_of_Shipment DESC,
         Warehouse_block ASC;
```

---

## Key Learnings

### WHERE vs HAVING

Use `WHERE` to filter rows before grouping.

```sql
WHERE Gender = 'Male'
```

Use `HAVING` to filter aggregated results after grouping.

```sql
HAVING COUNT(*) > 200
```

### GROUP BY

Used to divide records into groups before applying aggregate functions.

```sql
GROUP BY State
```

### ORDER BY

Used to sort the final result.

```sql
ORDER BY avg_value ASC
```

### LIMIT and OFFSET

Used to return a specific range of rows.

```sql
LIMIT 21 OFFSET 9
```

Returns rows ranked from 10th to 30th.

### Aggregate Functions

```sql
COUNT()
SUM()
AVG()
MIN()
MAX()
```

Used to summarize grouped data.
