# SQL DDL Commands and Constraints Notes

## 1. What is SQL

SQL stands for **Structured Query Language**.

It is used to communicate with relational databases.

Using SQL we can:

- create databases
- create tables
- insert data
- update data
- delete data
- retrieve data

Databases using SQL:

- MySQL
- PostgreSQL
- Oracle
- SQL Server
- SQLite

---

## 2. Types of SQL Commands

### DDL
Data Definition Language

Commands:
- CREATE
- ALTER
- DROP
- TRUNCATE

### DML
Data Manipulation Language

Commands:
- INSERT
- UPDATE
- DELETE

### DQL
Data Query Language

Command:
```sql
SELECT
```

### DCL
Data Control Language

Commands:
- GRANT
- REVOKE

### TCL
Transaction Control Language

Commands:
- COMMIT
- ROLLBACK
- SAVEPOINT

---

## 3. DDL Commands for Databases

### CREATE DATABASE

```sql
CREATE DATABASE student_management;
```

### CREATE DATABASE IF NOT EXISTS

```sql
CREATE DATABASE IF NOT EXISTS student_management;
```

### DROP DATABASE

```sql
DROP DATABASE student_management;
```

### DROP DATABASE IF EXISTS

```sql
DROP DATABASE IF EXISTS student_management;
```

---

## 4. DDL Commands for Tables

### CREATE TABLE

```sql
CREATE TABLE students (
    student_id INT,
    name VARCHAR(100),
    age INT
);
```

### TRUNCATE TABLE

Deletes all rows but keeps structure.

```sql
TRUNCATE TABLE students;
```

### DROP TABLE

Deletes complete table.

```sql
DROP TABLE students;
```

---

## 5. Data Integrity

Data integrity means data should remain:

- accurate
- correct
- consistent
- reliable

Example:

| id | name | age |
|---:|---|---:|
| 1 | Madhav | 21 |

Invalid:

| id | name | age |
|---:|---|---:|
| 2 | Madhav | -5 |

---

### Constraints

Constraints are rules applied to columns to prevent invalid data.

---

### Transactions

Transaction = group of SQL operations executed together.

Example:

- amount deducted from account A
- amount added to account B

Both should happen together.

---

### Normalization

Normalization is process of organizing data to reduce redundancy.

Normal Forms:

- 1NF
- 2NF
- 3NF
- BCNF

---

## 6. Constraints in MySQL

### NOT NULL

```sql
CREATE TABLE users (
    name VARCHAR(100) NOT NULL
);
```

---

### UNIQUE

```sql
CREATE TABLE users (
    email VARCHAR(100) UNIQUE
);
```

---

### Composite UNIQUE

```sql
CREATE TABLE users (
    name VARCHAR(100),
    email VARCHAR(100),
    UNIQUE(name, email)
);
```

---

### PRIMARY KEY

```sql
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    name VARCHAR(100)
);
```

---

### AUTO_INCREMENT

```sql
CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100)
);
```

---

### CHECK

```sql
CREATE TABLE students (
    age INT CHECK(age >= 18)
);
```

---

### DEFAULT

```sql
CREATE TABLE users (
    city VARCHAR(100) DEFAULT 'Gwalior'
);
```

---

### FOREIGN KEY

Departments table:

```sql
CREATE TABLE departments (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(100)
);
```

Students table:

```sql
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    name VARCHAR(100),
    dept_id INT,
    FOREIGN KEY (dept_id)
    REFERENCES departments(dept_id)
);
```

---

## Reference Actions

### RESTRICT

Parent row cannot be deleted.

### CASCADE

Deletes child rows automatically.

### SET NULL

Sets foreign key to NULL.

### SET DEFAULT

Sets foreign key to default value.

---

## Full Example

```sql
CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    age INT CHECK(age >= 18),
    city VARCHAR(100) DEFAULT 'Gwalior'
);
```

---

## 7. ALTER TABLE Command

### Add Column

```sql
ALTER TABLE students
ADD email VARCHAR(100);
```

---

### Add Multiple Columns

```sql
ALTER TABLE students
ADD phone VARCHAR(20),
ADD city VARCHAR(100);
```

---

### Drop Column

```sql
ALTER TABLE students
DROP COLUMN phone;
```

---

### Modify Column

```sql
ALTER TABLE students
MODIFY age BIGINT;
```

---

### Rename Column

```sql
ALTER TABLE students
RENAME COLUMN name TO full_name;
```

---

## 8. Adding and Deleting Constraints

### Add Constraint

```sql
ALTER TABLE users
ADD CONSTRAINT users_email_unique UNIQUE(email);
```

---

### Delete Constraint

```sql
ALTER TABLE users
DROP INDEX users_email_unique;
```

---

### Editing Constraint

MySQL does not allow direct editing.

Process:

1. Drop old constraint
2. Add new constraint again

Example:

```sql
ALTER TABLE users
DROP INDEX users_email_unique;
```

Then:

```sql
ALTER TABLE users
ADD CONSTRAINT users_email_unique UNIQUE(email, name);
```

---

## Quick Summary

### Database Commands

```sql
CREATE DATABASE
DROP DATABASE
```

### Table Commands

```sql
CREATE TABLE
TRUNCATE TABLE
DROP TABLE
ALTER TABLE
```

### Constraints

```sql
NOT NULL
UNIQUE
PRIMARY KEY
AUTO_INCREMENT
CHECK
DEFAULT
FOREIGN KEY
```

### Reference Actions

```sql
RESTRICT
CASCADE
SET NULL
SET DEFAULT
```
