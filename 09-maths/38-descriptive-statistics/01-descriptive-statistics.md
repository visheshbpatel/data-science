# Descriptive Statistics

Descriptive Statistics is the branch of statistics that focuses on collecting, organizing, summarizing, analyzing, and presenting data to understand its main characteristics.

It helps us understand **what the data looks like**, but it **does not make predictions**.

Machine Learning begins with descriptive statistics because understanding the data is the first step before building any model.

---

# Learning Roadmap

1. Statistics
2. Types of Statistics
3. Data vs Information
4. Population vs Sample
5. Types of Data
   - Categorical Data
     - Nominal Data
     - Ordinal Data
   - Numerical Data
     - Discrete Data
     - Continuous Data
6. Measures of Central Tendency
   - Mean
   - Median
   - Mode
   - Weighted Mean
   - Trimmed Mean
7. Measures of Dispersion
   - Range
   - Variance
   - Population Variance
   - Sample Variance
   - Mean Absolute Deviation (MAD)
   - Standard Deviation
   - Coefficient of Variation
8. Graphs for Univariate Analysis
   - Frequency Distribution Table
   - Cumulative Frequency
   - Histogram
9. Graphs for Bivariate Analysis
   - Contingency Table (Cross Tabulation)
   - Scatter Plot
   - Categorical vs Numerical Analysis

---

# Statistics



Statistics is the science of collecting, organizing, summarizing, analyzing, and interpreting data to discover useful information and support decision-making.

---

Statistics helps us understand data by turning large collections of numbers into meaningful information.

### Example

A school wants to know how students performed in an exam.

Instead of checking every mark individually, statistics calculates the average score, highest score, and score distribution.

## Why This Is Needed in Machine Learning

- Helps understand datasets before training models.
- Detects unusual patterns and outliers.
- Summarizes data efficiently.
- Forms the foundation of Exploratory Data Analysis (EDA).

---

# Types of Statistics

Statistics is divided into two major branches.

## Descriptive Statistics



Descriptive statistics summarizes and presents the characteristics of observed data without making conclusions beyond that dataset.



It describes the data you already have.

#### Example

Marks:

```
50 60 70 80 90
```

Descriptive statistics tells us:

- Mean = 70
- Median = 70
- Range = 40

### Why This Is Needed in Machine Learning

- Understands data before model training.
- Finds missing values.
- Detects outliers.
- Creates summary reports.

---

## Inferential Statistics



Inferential statistics uses sample data to make estimates or draw conclusions about an entire population.



Instead of studying everyone, we study a small group and make conclusions about the whole group.

#### Example

Surveying 1,000 voters to estimate the opinion of millions of voters.

### Why This Is Needed in Machine Learning

- Estimates model performance.
- Performs hypothesis testing.
- Builds confidence intervals.
- Helps evaluate model generalization.

---

| Feature | Descriptive | Inferential |
|----------|-------------|-------------|
| Purpose | Describe data | Draw conclusions |
| Uses Sample | Sometimes | Usually |
| Prediction | No | Yes |
| ML Usage | EDA | Model Evaluation |

---

# Data vs Information



- **Data** is a collection of raw facts or observations.
- **Information** is processed data that has meaning and usefulness.

---

Data is the input.

Information is the useful result after processing the data.

### Example

Data:

```
70
80
90
```

Information:

"The average score is 80."

## Why This Is Needed in Machine Learning

- ML models learn from data.
- Predictions produce useful information.
- Data preprocessing converts raw data into meaningful features.

---

# Population vs Sample

## Population



A population is the complete set of all individuals, objects, or observations of interest.



Everything you want to study.

#### Example

All students in a university.

---

## Sample



A sample is a subset of the population selected for analysis.



A smaller group chosen from the whole population.

#### Example

500 students selected from 20,000 students.

---

## Biased Sample



A biased sample does not represent the population fairly.



The sample gives an unfair picture of the population.

#### Example

Surveying only engineering students to estimate the average height of all college students.

---

## Random Sample



A random sample gives every population member an equal (or known) probability of selection.



Everyone has a fair chance of being selected.

---

## Census



A census collects data from every member of the population.



Study everyone instead of selecting a sample.

---

## Why This Is Needed in Machine Learning

- Training datasets are samples.
- Good samples improve model accuracy.
- Biased samples create biased models.
- Random sampling improves generalization.

---

# Types of Data

Data is broadly divided into two categories.

```
            Data
             │
     ┌───────┴────────┐
     │                │
Categorical      Numerical
(Qualitative)   (Quantitative)
```

---

# Categorical Data (Qualitative)



Categorical data consists of values representing groups, labels, or categories rather than numerical measurements.

---

The values describe *what something is* instead of *how much*.

### Example

- Color
- Blood Group
- Country

## Why This Is Needed in Machine Learning

- Used in classification problems.
- Requires encoding before model training.
- Common in customer and survey datasets.

---

# Nominal Data



Nominal data consists of categories without any natural ordering.

---

Categories that have names only.

### Example

- Red
- Blue
- Green

No color is greater than another.

## Why This Is Needed in Machine Learning

- Requires One-Hot Encoding.
- Used in classification datasets.

---

# Ordinal Data



Ordinal data consists of categories that have a meaningful order but unknown spacing between categories.

---

Categories can be ranked.

### Example

- Small
- Medium
- Large

## Why This Is Needed in Machine Learning

- Common in surveys.
- May require ordinal encoding.
- Preserves ranking information.

---

# Numerical Data (Quantitative)



Numerical data represents measurable quantities expressed as numbers.

---

Numbers that measure or count something.

### Example

- Height
- Weight
- Salary

## Why This Is Needed in Machine Learning

- Used directly by most algorithms.
- Supports mathematical operations.
- Used in regression problems.

---

# Discrete Data



Discrete data consists of countable values that take distinct numbers.

---

Things you count.

### Example

- Number of students
- Number of cars

## Why This Is Needed in Machine Learning

- Appears in counting problems.
- Used in classification and regression.

---

# Continuous Data



Continuous data consists of measurable values that can take any value within a range.

---

Things you measure.

### Example

- Height
- Temperature
- Weight

## Why This Is Needed in Machine Learning

- Used heavily in regression.
- Supports statistical calculations.

---

# Measures of Central Tendency



Measures of central tendency identify the central or typical value of a dataset.

---

They tell us what value best represents the entire dataset.

---

# Mean



The arithmetic mean is the sum of all observations divided by the number of observations.

## Formula

```text
Population Mean

μ = (Σx) / N

Sample Mean

x̄ = (Σx) / n
```

### Variables

- μ = Population mean
- x̄ = Sample mean
- Σx = Sum of observations
- N = Population size
- n = Sample size

### Example

```
10 20 30

Mean = (10+20+30)/3 = 20
```

## Why This Is Needed in Machine Learning

- Used for feature scaling.
- Used in normalization.
- Used to compute variance.
- Used in many ML algorithms.

---

# Median



The median is the middle observation after sorting the data.

If the dataset has an even number of observations, the median is the average of the two middle values.

---

The value exactly in the middle.

### Example

```
2 4 6 8 10

Median = 6
```

Even observations:

```
2 4 6 8

Median = (4+6)/2 = 5
```

## Why This Is Needed in Machine Learning

- Resistant to outliers.
- Useful for skewed datasets.
- Used for missing value imputation.

---

# Mode



Mode is the observation that occurs most frequently.

---

The most common value.

### Example

```
2 2 3 4 5

Mode = 2
```

If two values occur with the highest frequency, the dataset is **bimodal**.

If more than two values share the highest frequency, it is **multimodal**.

If no value repeats, the dataset has **no mode**.

| Dataset | Mode | Type |
|---------|------|------|
| 1, 2, 2, 3, 4 | 2 | Unimodal |
| 1, 1, 2, 2, 3, 4 | 1, 2 | Bimodal |
| 1, 1, 2, 2, 3, 3, 4 | 1, 2, 3 | Multimodal |
| 1, 2, 3, 4, 5 | No mode | No Mode |

## Why This Is Needed in Machine Learning

- Used for categorical data.
- Used to fill missing categorical values.

---

# Weighted Mean



Weighted mean assigns different importance (weights) to different observations.

## Formula

```text
x̄w = Σ(wixi) / Σwi
```

### Variables

- xi = Observation
- wi = Weight
- Σ = Summation

### Example

Marks:

```
80 (weight 2)

100 (weight 1)

Weighted Mean

= (80×2 +100×1)/(2+1)

= 86.67
```

## Why This Is Needed in Machine Learning

- Used in weighted loss functions.
- Used in ensemble learning.
- Used when observations have different importance.

---

# Trimmed Mean



Trimmed mean is calculated after removing a fixed percentage of the smallest and largest observations.

---

Ignore extreme values before calculating the average.

### Example

```
5%

Lowest removed

Highest removed

Calculate mean of remaining values.
```

## Why This Is Needed in Machine Learning

- Reduces outlier influence.
- Produces more robust averages.

---

# Measures of Dispersion



Measures of dispersion describe how spread out the observations are around the center.

---

They measure how much the data varies.

---

# Range



Range is the difference between the largest and smallest observations.

## Formula

```text
Range = Maximum − Minimum
```

### Example

```
5 8 12 20

Range = 20−5 =15
```

## Why This Is Needed in Machine Learning

- Quick estimate of spread.
- Detects extreme variation.

---

# Variance



Variance is the average of the squared deviations from the mean.

## Formula

```text
Population

σ² = Σ(x−μ)² / N

Sample

s² = Σ(x−x̄)² / (n−1)
```

### Variables

- σ² = Population variance
- s² = Sample variance
- μ = Population mean
- x̄ = Sample mean
- N = Population size
- n = Sample size

---

Variance measures how far the data points are spread around the average.

Large variance means data is widely spread.

Small variance means data is close together.

### Example

Two classes:

```
10 11 12

10 50 90
```

Both may have similar means.

The second class has much larger variance.

## Why This Is Needed in Machine Learning

- Used in PCA.
- Used in feature selection.
- Measures feature variability.

---

# Population Variance



Population variance measures spread using the entire population.

## Formula

```text
σ² = Σ(x−μ)² / N
```

### Example

Calculate variance using every employee in a company.

## Why This Is Needed in Machine Learning

- Used when complete data is available.
- Forms the theoretical definition of variance.

---

# Sample Variance



Sample variance estimates population variance using a sample.

It divides by **n − 1**, known as **Bessel's Correction**, to produce an unbiased estimate of the population variance.

## Formula

```text
s² = Σ(x−x̄)² / (n−1)
```

### Example

Estimate the variance of all students using 100 randomly selected students.

## Why This Is Needed in Machine Learning

- Most datasets are samples.
- Produces better variance estimates.

---

# Mean Absolute Deviation (MAD)



Mean Absolute Deviation is the average of the absolute differences between observations and the mean.

## Formula

```text
MAD = Σ|x−x̄| / n
```

### Variables

- | | = Absolute value
- x = Observation
- x̄ = Mean
- n = Number of observations

### Example

```
10 20 30

Mean =20

Absolute deviations

10

0

10

MAD=20/3
```

## Why This Is Needed in Machine Learning

- Less sensitive to outliers than variance.
- Measures average deviation.

---

# Standard Deviation



Standard deviation is the positive square root of variance.

## Formula

```text
Population

σ = √σ²

Sample

s = √s²
```

---

Average distance of observations from the mean.

### Example

Small standard deviation means values stay close together.

Large standard deviation means values are widely spread.

## Why This Is Needed in Machine Learning

- Used in Z-score normalization.
- Used in anomaly detection.
- Used in probability distributions.

---

# Coefficient of Variation (CV)



Coefficient of Variation measures the relative spread by comparing the standard deviation to the mean.

## Formula

```text
CV = (Standard Deviation / Mean) ×100%
```

### Variables

- CV = Coefficient of Variation
- Standard Deviation = Spread
- Mean = Average

### Example

Two datasets may have different units.

CV helps compare their variability fairly.

## Why This Is Needed in Machine Learning

- Compares variability across datasets.
- Independent of measurement units.

---



## Why Do We Need Standard Deviation?

Variance tells us how spread out the data is, but it has one major problem.

When calculating variance, we **square each deviation**, so the final unit is also squared.

### Example

Suppose the heights of students are measured in **centimeters (cm)**.

After calculation:

```text
Variance = 64 cm²
```

What does **64 cm²** mean?

It is difficult to interpret because our original data was measured in **cm**, not **cm²**.

To bring the result back to the original unit, we take the **square root** of the variance.

```text
Standard Deviation = √64 = 8 cm
```

Now the result is in **centimeters**, making it much easier to understand.

### In Simple Words

- Variance tells us the spread in **squared units**.
- Standard deviation tells us the spread in the **original unit**.

---

## Why is Standard Deviation Important?

Standard deviation tells us **how much the data typically deviates from the mean**.

### Example 1: Low Standard Deviation

```text
Data:
50, 50, 50, 50, 50
```

Mean = 50

Standard Deviation = **0**

Since every value is exactly the same, there is **no variation**.

---

### Example 2: High Standard Deviation

```text
Data:
20, 35, 50, 65, 80
```

Mean = 50

The values are spread far from the mean.

Therefore, the **standard deviation is large**.

---

## Interpretation

- **Small Standard Deviation**
  - Data points are close to the mean.
  - Less variability.
  - More consistency.

- **Large Standard Deviation**
  - Data points are far from the mean.
  - Greater variability.
  - Less consistency.

---

## Applications of Standard Deviation

- Measures the spread of data.
- Compares the consistency of different datasets.
- Detects outliers.
- Used in Normal Distribution.
- Used to calculate Z-Scores.
- Used in Machine Learning for feature scaling and data preprocessing.
- Used in Finance to measure investment risk.

---

## Quick Summary

| Variance | Standard Deviation |
|----------|--------------------|
| Average squared deviation from the mean | Square root of variance |
| Unit is squared (cm², kg², etc.) | Same unit as the original data (cm, kg, etc.) |
| Harder to interpret | Easier to interpret |
| Used mainly for calculations | Used for interpretation |


---

## Why Do We Need Coefficient of Variation?

Suppose we have two datasets.

### Dataset A

```text
Mean = 10
Standard Deviation = 2
```

### Dataset B

```text
Mean = 100
Standard Deviation = 10
```

If we only compare the standard deviations:

- Dataset A → SD = 2
- Dataset B → SD = 10

It seems Dataset B has much more variation.

But let's calculate CV.

```text
Dataset A:
CV = (2 / 10) × 100 = 20%

Dataset B:
CV = (10 / 100) × 100 = 10%
```

Now we see:

- Dataset A has **20% variation**
- Dataset B has **10% variation**

Even though Dataset B has a larger standard deviation, **Dataset A is actually more variable relative to its mean**.

This is why CV is useful.

---

## When Should We Use CV?

Use the Coefficient of Variation when:

- Comparing datasets with **different means**.
- Comparing datasets with **different units**.
- Measuring **relative variability** instead of absolute variability.
- Comparing consistency between different experiments or investments.

---

## Interpretation

| CV Value | Interpretation |
|----------|----------------|
| Low CV | Data is more consistent (less relative variation) |
| High CV | Data is less consistent (more relative variation) |

---

## Applications of CV

- Comparing investment risk in finance.
- Comparing consistency of manufacturing processes.
- Comparing variability between different experiments.
- Comparing datasets measured on different scales.
- Feature analysis in statistics and machine learning.

---

## Difference Between Standard Deviation and CV

| Standard Deviation | Coefficient of Variation |
|--------------------|--------------------------|
| Measures absolute spread | Measures relative spread |
| Unit is the same as the data | Unitless (percentage) |
| Cannot fairly compare datasets with different means | Best for comparing datasets with different means |
| Example: 8 cm | Example: 12% |

---

## Quick Summary

- **Variance** → Average squared distance from the mean.
- **Standard Deviation** → Typical distance from the mean (same unit as the data).
- **Coefficient of Variation** → Relative variability expressed as a percentage, useful for comparing different datasets.


---

# Graphs for Univariate Analysis

Univariate Analysis studies **one variable at a time**.

---

# Frequency Distribution Table



A frequency distribution table summarizes how many times each value or category occurs.

---

A table that counts occurrences.

### Example

| Color | Frequency |
|--------|----------|
| Red | 5 |
| Blue | 3 |
| Green | 2 |

## Why This Is Needed in Machine Learning

- Summarizes categorical data.
- Detects class imbalance.
- Supports exploratory analysis.

---

# Cumulative Frequency



Cumulative frequency is the running total of frequencies.

---

It shows how many observations are at or below a certain value.

### Example

| Marks | Frequency | Cumulative |
|--------|-----------|------------|
|10|2|2|
|20|3|5|
|30|4|9|

## Why This Is Needed in Machine Learning

- Understands cumulative distributions.
- Helps calculate percentiles.

---

# Histogram



A histogram displays the distribution of numerical data using adjacent bars representing frequency intervals.

---

A graph showing how values are distributed.

### Example

Student heights grouped into intervals.

## Why This Is Needed in Machine Learning

- Detects skewness.
- Finds outliers.
- Understands feature distributions.


```text
Frequency

9 |                █
8 |                █
7 |                █
6 |           █    █
5 |           █    █    █
4 |           █    █    █
3 |      █    █    █    █
2 |      █    █    █    █    █
1 | █    █    █    █    █    █
0 +----------------------------------------
    40-49 50-59 60-69 70-79 80-89 90-99
```

### Interpretation

- **X-axis** → Class intervals (Bins)
- **Y-axis** → Frequency
- Bars **touch each other** because the data is continuous.
- Taller bars indicate that more observations fall within that interval.

---

# Graphs for Bivariate Analysis

Bivariate Analysis studies **two variables together**.

---

# Contingency Table (Cross Tabulation)



A contingency table summarizes the relationship between two categorical variables.

---

A table comparing two categories.

### Example

| Gender | Purchased | Not Purchased |
|---------|-----------|---------------|
|Male|40|10|
|Female|35|15|

## Why This Is Needed in Machine Learning

- Studies relationships between categories.
- Useful for feature analysis.

---

# Scatter Plot



A scatter plot displays pairs of numerical observations to visualize their relationship.

---

Each point represents two numerical values.

### Example

Height vs Weight

Each person appears as one point.


```text
Y
10 |                         ●
 9 |
 8 |                   ●
 7 |
 6 |              ●
 5 |
 4 |         ●
 3 |
 2 |    ●
 1 |
 0 +----------------------------------------> X
    1    2    3    4    5    6    7
```

### Example Dataset

| X (Study Hours) | Y (Marks) |
|-----------------|-----------|
| 1 | 2 |
| 2 | 4 |
| 3 | 6 |
| 4 | 8 |
| 5 | 10 |

### Interpretation

- **X-axis** → First numerical variable
- **Y-axis** → Second numerical variable
- Each **●** represents one data point.
- The pattern of points helps identify the relationship between the two variables.

## Why This Is Needed in Machine Learning

- Detects correlation.
- Finds clusters.
- Identifies outliers.
- Visualizes regression data.

---

# Categorical vs Numerical Analysis



Categorical vs Numerical analysis compares a numerical variable across different categories.

Common visualizations include:

- Box Plot
- Violin Plot
- Bar Chart (using summary statistics)

---

Compare numbers between groups.

### Example

Compare salaries of:

- Engineers
- Doctors
- Teachers

## Why This Is Needed in Machine Learning

- Compares feature distributions.
- Helps identify useful predictive features.
- Supports feature engineering.
- Detects differences between classes.

---

# Summary

Descriptive Statistics helps us understand the structure, center, spread, and relationships within data before building Machine Learning models.

It includes:

- Understanding populations and samples
- Identifying data types
- Measuring the center of data
- Measuring the spread of data
- Visualizing one variable (Univariate Analysis)
- Visualizing relationships between two variables (Bivariate Analysis)

Mastering these concepts is essential for Exploratory Data Analysis (EDA), feature engineering, data preprocessing, and building reliable Machine Learning models.