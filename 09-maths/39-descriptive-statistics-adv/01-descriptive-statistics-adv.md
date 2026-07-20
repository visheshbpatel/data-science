# Descriptive Statistics (Part 2)

This document covers important descriptive statistics concepts used to summarize, visualize, and understand data before building Machine Learning models.

---

# 1. Quantiles and Percentiles



A **quantile** is a value that divides a sorted dataset into equal-sized groups.

Different types of quantiles divide the data into different numbers of equal parts.

- **Quartiles** → 4 equal parts
- **Quintiles** → 5 equal parts
- **Deciles** → 10 equal parts
- **Percentiles** → 100 equal parts

The data must always be sorted before calculating quantiles.

---



Imagine arranging exam scores from the lowest to the highest.

Quantiles simply split the ordered list into equal sections.

Instead of asking "What is the average?", quantiles ask:

> "Where does a value lie compared to the rest of the data?"

---

### Formula

For the **k-th percentile**:

```text
Position = (k / 100) × (n + 1)
```

Where:

- **k** = desired percentile
- **n** = total number of observations

> Different software packages may use slightly different percentile calculation methods.

---

### Types of Quantiles

| Type | Number of Groups | Each Group Contains |
|-------|------------------|---------------------|
| Quartiles | 4 | 25% |
| Quintiles | 5 | 20% |
| Deciles | 10 | 10% |
| Percentiles | 100 | 1% |

---

### Quartiles

Quartiles divide the data into four equal parts.

```text
Q1        Q2        Q3
|---------|---------|
25%      50%      75%
```

- **Q1** → 25% of observations are below this value.
- **Q2** → 50% of observations are below this value (Median).
- **Q3** → 75% of observations are below this value.

---

### Quintiles

Quintiles divide the data into five equal groups.

Each group contains approximately **20%** of the observations.

---

### Deciles

Deciles divide the data into ten equal groups.

Each group contains approximately **10%** of the observations.

---

### Percentiles

Percentiles divide the data into one hundred equal groups.

The **k-th percentile** is the value below which approximately **k%** of observations lie.

Examples:

- 50th percentile
- 90th percentile
- 95th percentile
- 99th percentile

---

### Example

Suppose 100 students take an exam.

If your score is at the **90th percentile**, it means you scored higher than about **90 students**.

---

### Why This Is Needed in Machine Learning

- Detect outliers.
- Understand data distribution.
- Create robust summary statistics.
- Used during Exploratory Data Analysis (EDA).

---

# 2. Five-Number Summary



The **Five-Number Summary** summarizes a numerical dataset using five important values:

1. Minimum
2. First Quartile (Q1)
3. Median (Q2)
4. Third Quartile (Q3)
5. Maximum

---



Instead of looking at hundreds of values, these five numbers quickly describe where the data begins, where the middle lies, and where it ends.

---

### Formula

No mathematical formula exists.

The five values are:

| Statistic | Meaning |
|------------|---------|
| Minimum | Smallest observation |
| Q1 | 25th percentile |
| Median | Middle observation |
| Q3 | 75th percentile |
| Maximum | Largest observation |

---

### Example

Dataset:

```text
2 4 6 8 10 12 14 16 18
```

Five-number summary:

| Value | Result |
|--------|--------|
| Minimum | 2 |
| Q1 | 5 |
| Median | 10 |
| Q3 | 15 |
| Maximum | 18 |

---

### Why This Is Needed in Machine Learning

- Quickly summarizes datasets.
- Helps detect skewness.
- Used to build box plots.
- Helps identify unusual observations.

---

# 3. Box Plot



A **Box Plot** is a graphical representation of the Five-Number Summary.

It visualizes:

- Minimum
- Q1
- Median
- Q3
- Maximum

It also highlights potential outliers.

---



A box plot shows where most of the data lies and whether there are unusually high or low values.

---

### Formula

#### Interquartile Range (IQR)

```text
IQR = Q3 - Q1
```

Where:

- **Q1** = First Quartile
- **Q3** = Third Quartile

---

#### Outlier Rule

Potential outliers satisfy:

```text
Lower Limit = Q1 − 1.5 × IQR

Upper Limit = Q3 + 1.5 × IQR
```

Values outside these limits are plotted as outliers.

---

### Structure

```text
Min     Q1    Median    Q3     Max

|-------|======|======|-------|
```

The box represents the middle **50%** of the data.

The whiskers extend to the smallest and largest **non-outlier** observations.

Outliers are plotted separately.

```text
|------|======|======|---|          •
                                  Outlier
```

---

### Example

Suppose most salaries range from ₹30,000 to ₹70,000, but one employee earns ₹5,00,000.

The salary ₹5,00,000 appears as an outlier.

---

### Why This Is Needed in Machine Learning

- Detects outliers quickly.
- Compares distributions.
- Shows spread of data.
- Useful during EDA.

---

# 4. Scatter Plot



A **Scatter Plot** displays the relationship between two numerical variables by plotting observations as points on a two-dimensional graph.

---



Each point represents one observation.

The pattern of points reveals whether two variables are related.

---

### Formula

No formula.

---

### Types of Relationships

#### Positive Relationship

As one variable increases, the other also increases.

```text
•
  •
    •
      •
```

---

#### Negative Relationship

As one variable increases, the other decreases.

```text
      •
    •
  •
•
```

---

#### No Relationship

Points appear randomly scattered.

```text
•   •
   •
 •     •
```

---

### Example

Hours studied vs exam score.

Students who study more often score higher.

---

### Why This Is Needed in Machine Learning

- Detects relationships between features.
- Helps identify trends.
- Reveals clusters.
- Detects unusual observations.

---

# 5. Covariance



Covariance measures how two variables change together.

It indicates whether variables move in the same direction or opposite directions.

Unlike correlation, covariance is not standardized.

---



Covariance answers the question:

> "When one variable changes, how does the other usually change?"

---

### Formula

### Population Covariance

```text
                N
Cov(X,Y)= (1/N) Σ (Xi−μx)(Yi−μy)
               i=1
```

Where:

- **Xi** = observation of X
- **Yi** = observation of Y
- **μx** = population mean of X
- **μy** = population mean of Y
- **N** = population size

---

### Sample Covariance

```text
                n
Cov(X,Y)= (1/(n−1)) Σ (Xi−x̄)(Yi−ȳ)
               i=1
```

Where:

- **x̄** = sample mean of X
- **ȳ** = sample mean of Y
- **n** = sample size

---

### Interpretation

| Covariance | Meaning |
|------------|---------|
| Positive | Variables increase together |
| Negative | One increases while the other decreases |
| Zero | No linear relationship |

---

### Example

Height and weight usually have positive covariance.

---

### Why This Is Needed in Machine Learning

- Basis for correlation.
- Used in PCA.
- Helps understand feature relationships.
- Used in covariance matrices.

---

# 6. Correlation



Correlation measures both the **strength** and **direction** of the linear relationship between two variables.

Unlike covariance, correlation is standardized.

---



Correlation tells us how strongly two variables move together.

Its value always lies between **−1** and **+1**.

---

### Formula

Pearson Correlation Coefficient:

```text
          Cov(X,Y)
r = -------------------
          σX × σY
```

Where:

- **r** = correlation coefficient
- **Cov(X,Y)** = covariance
- **σX** = standard deviation of X
- **σY** = standard deviation of Y

---

### Interpretation

| Correlation | Meaning |
|-------------|---------|
| +1 | Perfect positive linear relationship |
| +0.8 | Strong positive relationship |
| 0 | No linear relationship |
| -0.8 | Strong negative relationship |
| -1 | Perfect negative linear relationship |

---

### Important Note

Correlation measures **only linear relationships**.

A correlation close to **0** does **not** necessarily mean there is no relationship.

It only means there is **no linear relationship**.

---

### Example

Study hours and exam marks often have a strong positive correlation.

---

### Why This Is Needed in Machine Learning

- Feature selection.
- Detect multicollinearity.
- Understand feature relationships.
- Improve model interpretation.

---

# 7. Correlation vs Causation



**Correlation** means two variables are statistically associated.

**Causation** means one variable directly causes changes in another.

Correlation alone cannot prove causation.

---



Two things may happen together without one causing the other.

Sometimes a third variable influences both.

This third variable is called a **confounding variable**.

---

### Formula

No formula.

---

### Example

Ice cream sales and drowning incidents both increase during summer.

Ice cream does **not** cause drowning.

The confounding variable is:

- Summer temperature

---

### Why This Is Needed in Machine Learning

- Prevents incorrect conclusions.
- Encourages careful feature interpretation.
- Avoids misleading model explanations.
- Important for causal inference.

---

# 8. Visualizing Multiple Variables



When datasets contain more than two variables, specialized visualization techniques help display additional information within a single figure.

---

## 3D Scatter Plot

#

A 3D Scatter Plot visualizes three numerical variables using the X, Y, and Z axes.



Instead of plotting points on a flat graph, points are placed inside a three-dimensional space.

### Formula

No formula.

### Example

- Height
- Weight
- Age

Each axis represents one variable.

### Why This Is Needed in Machine Learning

- Explore relationships among three numerical features.
- Detect clusters.
- Identify multidimensional patterns.

---

## Hue Parameter

#

Hue uses different colors to represent a categorical variable while plotting two numerical variables.



Points are colored based on their category.

### Formula

No formula.

### Example

Scatter plot:

- X = Height
- Y = Weight
- Color = Gender

### Why This Is Needed in Machine Learning

- Compare categories.
- Visualize class labels.
- Detect category-wise patterns.

---

## Facet Grid

#

A Facet Grid creates multiple plots by splitting data according to a categorical variable.



Instead of using colors, each category gets its own graph.

### Formula

No formula.

### Example

Separate scatter plots for:

- Male
- Female

### Why This Is Needed in Machine Learning

- Reduces clutter.
- Makes category comparisons easier.
- Improves readability.

---

## Pair Plot

#

A Pair Plot displays scatter plots for every pair of numerical variables in a dataset along with each variable's distribution.



It automatically compares every numerical feature with every other numerical feature.

### Formula

No formula.

### Example

Features:

- Height
- Weight
- Age
- Income

The pair plot generates scatter plots for all feature pairs.

### Why This Is Needed in Machine Learning

- Explore feature relationships.
- Detect correlations.
- Identify clusters.
- Find outliers.

---

## Bubble Plot

#

A Bubble Plot extends a scatter plot by representing a third numerical variable through the size of each point.



Larger bubbles represent larger values of another variable.

### Formula

No formula.

### Example

- X = Experience
- Y = Salary
- Bubble Size = Number of Projects

### Why This Is Needed in Machine Learning

- Visualize three numerical variables.
- Compare observations more effectively.
- Identify important data points.

---

# Choosing the Right Visualization

| Situation | Recommended Visualization |
|-----------|---------------------------|
| Two numerical variables | Scatter Plot |
| Three numerical variables | 3D Scatter Plot |
| Add one categorical variable | Hue |
| Many categories causing clutter | Facet Grid |
| Compare many numerical features | Pair Plot |
| Add one more numerical variable | Bubble Plot |
