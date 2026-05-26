# DBMS & SQL Learning Notes

These are my detailed notes while learning **DBMS** and **SQL**.  
All examples and tables are preserved, with cleaner formatting for GitHub.

# 1. What is a Database

A **database** is an organised collection of related data that is stored electronically and managed in a structured way so that the data can be easily:

- stored
- accessed
- updated
- retrieved
- managed

using software systems.

A database allows users and applications to handle large amounts of information efficiently without confusion, duplication, or data loss.

### **What is CRUD?**

CRUD represents the **four basic operations** performed on data in a database.

CRUD stands for:

| Letter | Meaning |
| --- | --- |
| C | Create |
| R | Read |
| U | Update |
| D | Delete |

These operations are the foundation of working with databases using SQL.

- Create means **adding new data** into the database.
- Read means **retrieving or viewing data** from the database.
- Update means **modifying existing data** in the database.
- Delete means **removing data** from the database.

### **Properties of an Ideal Database**

An **ideal database** is a database system that stores and manages data efficiently, securely, accurately, and reliably.

It should possess certain important properties to ensure smooth data management and better performance.

#### 1. Data Integrity

Data integrity means the data stored in the database should remain:

- accurate
- correct
- consistent
- reliable

## Example

A student's marks should not suddenly become negative or incorrect due to system errors.

If a bank account balance is ₹10,000, the database must always store the correct amount.



## Why Important

Without integrity:

- wrong calculations occur
- reports become unreliable
- systems may fail



# 2. Data Security

Only authorized users should access or modify the data.



## Example

In a banking system:

- customers can view their account
- bank employees have limited permissions
- hackers should not access data



## Why Important

Protects:

- personal information
- financial records
- confidential data



# 3. Data Consistency

The same data should remain uniform everywhere in the database.



## Example

If a student's branch changes from CSE to AIML, every related table should show AIML, not old and new values together.



## Why Important

Prevents confusion and conflicting information.



# 4. Minimal Data Redundancy

Duplicate data should be minimized.



## Example

A student's phone number should not be unnecessarily stored multiple times in different places.



## Why Important

Reduces:

- storage waste
- inconsistency
- update problems



# 5. Data Independence

Changes in database structure should not heavily affect applications using it.



## Example

Suppose a new column `Email` is added to a Students table.

The whole application should not break because of this small change.



## Why Important

Makes databases flexible and easier to maintain.



# 6. Fast Data Access

The database should retrieve data quickly.



## Example

When searching a product on Amazon, results appear instantly even among millions of products.



## Why Important

Improves:

- user experience
- application speed
- performance



# 7. Scalability

The database should handle increasing amounts of data efficiently.



## Example

Instagram started with few users but now stores billions of posts and users.



## Why Important

Allows systems to grow without crashing.



# 8. Reliability

The database should work properly without frequent failures.



## Example

Banking systems must run continuously without losing transaction data.



## Why Important

Ensures trust and uninterrupted service.



# 9. Backup and Recovery

The database should recover data if:

- system crashes
- power failure occurs
- hardware fails



## Example

If a server crashes, backup systems restore the lost data.



## Why Important

Prevents permanent data loss.



# 10. Multi-user Support

Multiple users should access the database simultaneously without problems.



## Example

Thousands of users can use YouTube at the same time.



## Why Important

Essential for real-world applications.



# 11. Concurrency Control

The database should properly manage simultaneous operations.



## Example

Two people booking the last movie seat at the same time should not both get the same seat.



## Why Important

Prevents conflicts and incorrect data updates.



# 12. Efficient Storage Management

The database should use storage space efficiently.



## Example

Large companies store petabytes of data, so efficient storage becomes critical.

# **2. Types of Databases**

Databases are classified based on:

- how data is stored
- how data is organized
- how relationships are maintained

Different types of databases are used for different purposes.

# 1. Relational Database (RDBMS)

## Definition

A relational database stores data in the form of **tables** consisting of:

- rows
- columns

The tables are related to each other using keys.

This is the most commonly used type of database.

Uses SQL.



## Real World Example

College Management System

Different tables:

- Students
- Teachers
- Courses

All connected using relationships.



## Example Table

## Students Table

| Student_ID | Name | Branch |
| --- | --- | --- |
| 101 | Vishesh | AIML |
| 102 | Madhav | CSE |
| 103 | Kunal | IT |



## Courses Table

| Course_ID | Course_Name | Student_ID |
| --- | --- | --- |
| C1 | ML | 101 |
| C2 | OS | 102 |
| C3 | DBMS | 101 |

Here:

- `Student_ID` connects both tables
- relationships are maintained



## Examples of RDBMS

- MySQL
- PostgreSQL
- Oracle Database
- Microsoft SQL Server



# 2. NoSQL Database

## Definition

NoSQL databases store data in flexible formats instead of fixed tables.

Used for:

- huge data
- real-time systems
- unstructured data



## Types of NoSQL Databases

- Document databases
- Key-value databases
- Column databases
- Graph databases



# 2.1 Document Database

## Definition

Stores data in document-like structures, usually JSON format.



## Example

User Profile Data

```
{
  "id":101,
  "name":"Vishesh",
  "skills": ["Python","SQL","ML"],
  "age":21
}
```

Flexible structure:

- one user can have extra fields
- no fixed schema needed



## Example Software

- MongoDB



# 2.2 Key-Value Database

## Definition

Stores data as:

- key
- value

Similar to a dictionary in Python.



## Example Table

| Key | Value |
| --- | --- |
| username | Vishesh |
| theme | dark |
| language | English |



## Real World Use

- caching
- session storage
- fast lookups



## Example Software

- Redis



# 2.3 Column-Oriented Database

## Definition

Stores data column-wise instead of row-wise.

Good for:

- analytics
- data warehousing
- big data



## Traditional Row Storage

| ID | Name | Marks |
| --- | --- | --- |
| 1 | Madhav | 85 |
| 2 | Kunal | 90 |

Stored row by row.



## Column Storage

### ID Column

ID



1



2



### Name Column

Name



Madhav



Kunal



### Marks Column

Marks



85



90





## Why Useful

If we only need marks:

- database reads only Marks column
- faster analytics



## Example Software

- Apache Cassandra



# 2.4 Graph Database

## Definition

Stores data using:

- nodes
- edges
- relationships

Used when relationships are very important.



## Example

Social Media Connections

| Person | Follows |
| --- | --- |
| Vishesh | Madhav |
| Madhav | Kunal |
| Kunal | Aman |



## Graph Representation

```
Vishesh ---> Madhav ---> Kunal
```



## Real World Use

- social networks
- recommendation systems
- fraud detection



## Example Software

- Neo4j



# 3. Hierarchical Database

## Definition

Stores data in a tree-like parent-child structure.

One parent can have many children.



## Example

Company Structure

```
CEO
 ├── Manager 1
 │     ├── Employee A
 │     └── Employee B
 └── Manager 2
       ├── Employee C
```



## Characteristics

- fast hierarchical access
- rigid structure



# 4. Network Database

## Definition

Similar to hierarchical databases but allows many-to-many relationships.



## Example

Students and Courses

| Student | Course |
| --- | --- |
| Vishesh | DBMS |
| Vishesh | ML |
| Madhav | DBMS |

One student can take many courses.

One course can have many students.



# 5. Distributed Database

## Definition

Data is stored across multiple computers or servers but appears as a single database.



## Example

Google stores data across servers worldwide.



## Advantages

- high availability
- better speed
- fault tolerance



# 6. Cloud Database

## Definition

Database hosted on cloud platforms.

Accessible through internet.



## Example Services

- Amazon Web Services RDS
- Google Cloud SQL
- Microsoft Azure Database Services

# Comparison Table

| Database Type | Data Structure | Best Use |
| --- | --- | --- |
| Relational | Tables | Structured data |
| Document | JSON Documents | Flexible data |
| Key-Value | Key and value pairs | Fast retrieval |
| Column-Oriented | Columns | Analytics |
| Graph | Nodes & relationships | Connected data |
| Hierarchical | Tree structure | Parent-child systems |
| Network | Linked records | Complex relationships |
| Distributed | Multiple servers | Large-scale systems |
| Cloud | Internet-hosted | Modern scalable apps |

# 3. What is DBMS?

DBMS stands for:

# Database Management System

A DBMS is software that is used to:

- create databases
- store data
- manage data
- retrieve data
- update data
- control access to data

in an organized and efficient way.



A DBMS is a software system that acts as an interface between:

- the user
- and the database

It helps users interact with the database easily without directly handling raw data files.



# Real World Analogy

Think of a **library**.

- Books = Data
- Library = Database
- Librarian = DBMS

The librarian helps:

- store books properly
- find books quickly
- issue books
- update records
- manage access

Similarly, a DBMS manages the database.



A DBMS is software that enables users to define, create, maintain, manipulate, and control access to databases.



# Example

Suppose a college stores student data.

Without DBMS:

- data may be scattered
- searching becomes difficult
- updates become messy
- security becomes weak

With DBMS:

- data is organized
- records are easy to search
- multiple users can access data
- security and backup are maintained



# Example Table

## Students Table

| Student_ID | Name | Branch | Marks |
| --- | --- | --- | --- |
| 101 | Vishesh | AIML | 89 |
| 102 | Madhav | CSE | 90 |
| 103 | Kunal | IT | 92 |

The DBMS helps:

- insert new students
- search student records
- update marks
- delete records



# Functions of DBMS



# 1. Data Storage

Stores data systematically inside the database.



# 2. Data Retrieval

Allows users to retrieve data quickly.

Example:

```
SELECT*FROM Students;
```



# 3. Data Manipulation

Allows:

- insertion
- updation
- deletion

Example:

```
INSERTINTO StudentsVALUES (104,'Aman','AIML',85);
```



# 4. Security Management

Controls who can:

- view data
- modify data
- delete data



# 5. Backup and Recovery

Recovers data after:

- crashes
- failures
- power loss



# 6. Concurrency Control

Handles multiple users accessing data simultaneously.

Example:

Many users using Instagram together.



# 7. Data Integrity

Ensures data remains:

- accurate
- valid
- consistent



# 8. Reduces Data Redundancy

Avoids unnecessary duplicate data.



# Architecture of DBMS

```
User/Application
        ↓
       DBMS
        ↓
     Database
```

The user interacts with the DBMS, and the DBMS communicates with the database.



# Examples of DBMS Software

| DBMS | Type |
| --- | --- |
| MySQL | Relational DBMS |
| PostgreSQL | Relational DBMS |
| Oracle Database | Enterprise DBMS |
| MongoDB | NoSQL DBMS |
| Microsoft SQL Server | Relational DBMS |



# Advantages of DBMS

| Advantage | Explanation |
| --- | --- |
| Better organization | Data stored systematically |
| Fast retrieval | Quick searching |
| Security | Protects data |
| Backup | Prevents data loss |
| Multi-user access | Many users can work together |
| Reduced redundancy | Less duplicate data |
| Data consistency | Accurate information |



# Disadvantages of DBMS

| Disadvantage | Explanation |
| --- | --- |
| Complex | Requires learning |
| Costly | Large DBMS systems can be expensive |
| Requires hardware | Needs storage and processing power |
| Maintenance | Requires administration |



# Difference Between Database and DBMS

| Database | DBMS |
| --- | --- |
| Collection of data | Software managing the data |
| Stores information | Controls and manages information |
| Passive | Active software system |



# Important Point

A database stores the data.

A DBMS manages the database.

### Database Keys

# Database Keys

Database keys are special attributes (columns) used to:

- uniquely identify records
- establish relationships between tables
- maintain data integrity

Keys are one of the most important concepts in relational databases and SQL.



# Why Keys are Needed

Imagine a Students table:

| Name | Branch |
| --- | --- |
| Madhav | CSE |
| Madhav | AIML |

There are two students with the same name.

Now if we want to find a specific Madhav:

- confusion occurs
- data retrieval becomes difficult

So we use a unique identifier called a key.



# Example Table

## Students Table

| Student_ID | Name | Branch |
| --- | --- | --- |
| 101 | Vishesh | AIML |
| 102 | Madhav | CSE |
| 103 | Kunal | IT |

Here:

- `Student_ID` uniquely identifies each student
- no two students can have same ID

So `Student_ID` is a key.



# 4. Types of Database Keys

# 1. Primary Key

## Definition

A primary key is a column (or set of columns) that uniquely identifies each record in a table.



## Properties of Primary Key

A primary key:

- must be unique
- cannot contain NULL values
- each table can have only one primary key



## Example

| Student_ID | Name | Branch |
| --- | --- | --- |
| 101 | Vishesh | AIML |
| 102 | Madhav | CSE |

Here:

- `Student_ID` is the primary key

because:

- every ID is unique
- no NULL values



## SQL Example

```
CREATETABLE Students (
    Student_IDINTPRIMARYKEY,
    NameVARCHAR(50),
    BranchVARCHAR(20)
);
```



# 2. Foreign Key

## Definition

A foreign key is a column that creates a relationship between two tables.

It refers to the primary key of another table.



# Real Understanding

Primary key:

- identifies records inside its own table

Foreign key:

- connects one table to another



# Example

## Students Table

| Student_ID | Name |
| --- | --- |
| 101 | Vishesh |
| 102 | Madhav |



## Courses Table

| Course_ID | Course_Name | Student_ID |
| --- | --- | --- |
| C1 | DBMS | 101 |
| C2 | ML | 101 |
| C3 | OS | 102 |

Here:

- `Student_ID` in Students table = Primary Key
- `Student_ID` in Courses table = Foreign Key

It creates a relationship between students and courses.



## SQL Example

```
CREATETABLE Courses (
    Course_IDVARCHAR(10),
    Course_NameVARCHAR(50),
    Student_IDINT,
FOREIGNKEY (Student_ID)
REFERENCES Students(Student_ID)
);
```



# 3. Candidate Key

## Definition

A candidate key is a column that can uniquely identify records.

A table can have multiple candidate keys.

One of them is selected as the primary key.



## Example

| Student_ID | Email | Phone |
| --- | --- | --- |
| 101 | a@gmail.com | 987654 |
| 102 | b@gmail.com | 987655 |

Possible unique columns:

- Student_ID
- Email
- Phone

All are candidate keys.

One becomes primary key.



# 4. Alternate Key

## Definition

Candidate keys that are not selected as the primary key are called alternate keys.



## Example

If:

- Student_ID = Primary Key

then:

- Email
- Phone

become alternate keys.



# 5. Composite Key

## Definition

A composite key is formed using two or more columns together to uniquely identify a record.



## Example

## Student_Courses Table

| Student_ID | Course_ID | Marks |
| --- | --- | --- |
| 101 | C1 | 89 |
| 101 | C2 | 92 |

Here:

- Student_ID alone is not unique
- Course_ID alone is not unique

But together:

- `(Student_ID, Course_ID)` becomes unique

This combination is a composite key.



## SQL Example

```
PRIMARYKEY (Student_ID, Course_ID)
```



# 6. Unique Key

## Definition

A unique key ensures all values in a column are unique.

Unlike primary key:

- it can allow NULL values (depends on DBMS)



## Example

| Student_ID | Email |
| --- | --- |
| 101 | a@gmail.com |
| 102 | b@gmail.com |

Email can be a unique key.



## SQL Example

```
EmailVARCHAR(100)UNIQUE
```



# 7. Super Key

## Definition

A super key is any set of columns that can uniquely identify records.

It may contain extra unnecessary attributes.



## Example

| Student_ID | Email | Name |
| --- | --- | --- |

Possible super keys:

- Student_ID
- Email
- Student_ID + Name

All uniquely identify rows.



# Simple Relationship Between Keys

```
Super Key
   ↓
Candidate Key
   ↓
Primary Key
```



# Comparison Table

| Key Type | Purpose |
| --- | --- |
| Primary Key | Unique identification |
| Foreign Key | Relationship between tables |
| Candidate Key | Possible primary keys |
| Alternate Key | Candidate keys not chosen |
| Composite Key | Combination of columns |
| Unique Key | Prevent duplicate values |
| Super Key | Any unique identifier |



# Real World Analogy

## College Example

| Concept | Real Example |
| --- | --- |
| Primary Key | Roll Number |
| Foreign Key | Department ID |
| Composite Key | Student + Subject |
| Unique Key | Email ID |



# Important Point

Keys are essential because they:

- uniquely identify data
- prevent duplication
- create relationships
- maintain integrity
- improve database organization

# **5. Cardinality of Relationship in DBMS**

Cardinality defines the **number of entities** that can participate in a relationship between tables in a database.

In simple words:

It tells us:

# "How many records of one table can be related to records of another table?"

Cardinality is one of the most important concepts in database relationships and ER models.



# Real World Understanding

Suppose we have:

- Students
- Courses

Questions:

- Can one student take many courses?
- Can one course have many students?

Cardinality answers these types of questions.



# Types of Cardinality

There are mainly 4 types:

| Type | Meaning |
| --- | --- |
| One-to-One | One record relates to one record |
| One-to-Many | One record relates to many records |
| Many-to-One | Many records relate to one record |
| Many-to-Many | Many records relate to many records |



# 1. One-to-One Relationship (1:1)

# Definition

One record in Table A is related to only one record in Table B.

And vice versa.



# Real World Example

One person has one passport.

One passport belongs to one person.



# Example Tables

## Person Table

| Person_ID | Name |
| --- | --- |
| 101 | Vishesh |
| 102 | Madhav |



## Passport Table

| Passport_ID | Person_ID |
| --- | --- |
| P1 | 101 |
| P2 | 102 |

Here:

- one person → one passport
- one passport → one person



# 2. One-to-Many Relationship (1:M)

# Definition

One record in Table A can relate to many records in Table B.

But one record in Table B relates to only one record in Table A.



# Real World Example

One teacher teaches many students.

But one student may have one class teacher.



# Example Tables

## Teacher Table

| Teacher_ID | Name |
| --- | --- |
| T1 | Sharma |



## Students Table

| Student_ID | Name | Teacher_ID |
| --- | --- | --- |
| 101 | Vishesh | T1 |
| 102 | Madhav | T1 |
| 103 | Kunal | T1 |

Here:

- one teacher teaches many students
- each student linked to one teacher



# 3. Many-to-One Relationship (M:1)

# Definition

Many records in Table A relate to one record in Table B.

This is basically the reverse of One-to-Many.



# Example

Many students belong to one department.



## Students Table

| Student_ID | Name | Department_ID |
| --- | --- | --- |
| 101 | Vishesh | D1 |
| 102 | Madhav | D1 |
| 103 | Kunal | D1 |



## Department Table

| Department_ID | Department_Name |
| --- | --- |
| D1 | AIML |

Here:

- many students → one department



# 4. Many-to-Many Relationship (M:N)

# Definition

Many records in Table A can relate to many records in Table B.



# Real World Example

Students and Courses.

- one student can take many courses
- one course can have many students



# Example Tables

## Students Table

| Student_ID | Name |
| --- | --- |
| 101 | Vishesh |
| 102 | Madhav |



## Courses Table

| Course_ID | Course_Name |
| --- | --- |
| C1 | DBMS |
| C2 | ML |



## Student_Course Table

| Student_ID | Course_ID |
| --- | --- |
| 101 | C1 |
| 101 | C2 |
| 102 | C1 |

Here:

- Vishesh takes DBMS and ML
- DBMS has Vishesh and Madhav



# Important Point

Many-to-Many relationships are usually implemented using a:

# Junction Table / Bridge Table

Example:

`Student_Course`

because relational databases cannot directly store M:N relationships.



# Summary Table

| Cardinality | Meaning | Example |
| --- | --- | --- |
| 1:1 | One to one | Person and Passport |
| 1:M | One to many | Teacher and Students |
| M:1 | Many to one | Students and Department |
| M:N | Many to many | Students and Courses |



# Why Cardinality is Important

Cardinality helps:

- design proper databases
- establish relationships
- reduce redundancy
- improve integrity
- organize data efficiently

### **Drawbacks of Databases**

Although databases are extremely useful for storing and managing data, they also have some disadvantages and limitations.



# 1. High Cost

## Explanation

Database systems can be expensive because they require:

- powerful hardware
- licensed DBMS software
- maintenance
- trained professionals



## Example

Large companies using enterprise DBMS like Oracle Database spend huge amounts on:

- servers
- cloud infrastructure
- database administrators



# 2. Complexity

## Explanation

Database systems are complex to:

- design
- manage
- maintain

Learning database concepts like:

- normalization
- indexing
- transactions
- relationships

takes time.



## Example

Designing a banking database with millions of transactions is not simple.



# 3. Requires Skilled Professionals

## Explanation

Databases require experts such as:

- Database Administrators (DBA)
- Backend Developers
- Data Engineers

to manage and maintain them properly.



## Why Problematic

Small companies may not afford skilled database professionals.



# 4. Large Hardware Requirements

## Explanation

Big databases require:

- high storage
- large memory
- powerful processors

especially for applications with millions of users.



## Example

YouTube stores enormous amounts of video-related data requiring massive servers.



# 5. Security Risks

## Explanation

If database security is weak:

- hackers may steal data
- sensitive information may leak



## Example

Banking or hospital databases contain confidential information.

A security breach can be very dangerous.



# 6. Backup and Recovery Complexity

## Explanation

Managing backups and recovery systems for huge databases is difficult.



## Problem

If backup systems fail:

- important data may be permanently lost



# 7. Performance Overhead

## Explanation

DBMS software adds extra processing overhead.

For very small applications, using a database may actually reduce performance compared to simple files.



## Example

A tiny calculator app does not need a full database system.



# 8. Data Corruption Risk

## Explanation

Hardware failure, software bugs, or improper handling may corrupt database files.



## Example

Server crashes during transactions can damage data if recovery systems are weak.



# 9. System Failure Affects Entire Organization

## Explanation

If the central database fails:

- applications stop working
- users cannot access data



## Example

If an airline database server crashes:

- ticket booking may stop completely



# 10. Frequent Maintenance Required

## Explanation

Databases need regular:

- updates
- optimization
- monitoring
- backups



## Example

Indexes need optimization to maintain query speed.



# 11. Concurrency Issues

## Explanation

When many users access the database simultaneously:

- conflicts may occur
- deadlocks may happen



## Example

Two users trying to book the same movie seat at the same time.



# 12. Migration Difficulty

## Explanation

Moving data from one database system to another can be difficult and time-consuming.



## Example

Migrating from MySQL to PostgreSQL may require:

- schema conversion
- query changes
- data transformation
