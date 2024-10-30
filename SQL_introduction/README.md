# SQL Introduction

This project covers the basics of SQL, using MySQL as the database management system.

## HELPER : SQL CHEATSHEET FROM [NOZIOP](https://github.com/Noziop) :
###### [SQL CLEAN SHEET](https://github.com/Noziop/usefull_tools/blob/main/SQL/SQL-cheat_sheet.md)
---
## Tasks

### 0. List databases
**File:** `0-list_databases.sql`

Write a script that lists all databases of your MySQL server.

### 1. Create a database
**File:** `1-create_database_if_missing.sql`

Write a script that creates the database `hbtn_0c_0` in your MySQL server.
- If the database `hbtn_0c_0` already exists, your script should not fail.
- You are not allowed to use the SELECT or SHOW statements.

### 2. Delete a database
**File:** `2-remove_database.sql`

Write a script that deletes the database `hbtn_0c_0` in your MySQL server.
- If the database `hbtn_0c_0` doesn’t exist, your script should not fail.
- You are not allowed to use the SELECT or SHOW statements.

### 3. List tables
**File:** `3-list_tables.sql`

Write a script that lists all the tables of a database in your MySQL server.
- The database name will be passed as an argument of the mysql command.

### 4. First table
**File:** `4-first_table.sql`

Write a script that creates a table called `first_table` in the current database in your MySQL server.
- `first_table` description:
  - id INT
  - name VARCHAR(256)
- The database name will be passed as an argument of the mysql command.
- If the table `first_table` already exists, your script should not fail.
- You are not allowed to use the SELECT or SHOW statements.

### 5. Full description
**File:** `5-full_table.sql`

Write a script that prints the following description of the table `first_table` from the database `hbtn_0c_0` in your MySQL server.
- The database name will be passed as an argument of the mysql command.
- You are not allowed to use the DESCRIBE or EXPLAIN statements.

### 6. List all in table
**File:** `6-list_values.sql`

Write a script that lists all rows of the table `first_table` from the database `hbtn_0c_0` in your MySQL server.
- All fields should be printed.
- The database name will be passed as an argument of the mysql command.

### 7. First add
**File:** `7-insert_value.sql`

Write a script that inserts a new row in the table `first_table` (database `hbtn_0c_0`) in your MySQL server.
- New row:
  - id = 89
  - name = Best School

### 8. Count 89
**File:** `8-count_89.sql`

Write a script that displays the number of records with id = 89 in the table `first_table` of the database `hbtn_0c_0` in your MySQL server.
  
### 9. Full creation
**File:** `9-full_creation.sql`

Write a script that creates a table called `second_table` in the database `hbtn_0c_0` in your MySQL server and adds multiple rows.
- `second_table` description:
  - id INT
  - name VARCHAR(256)
  - score INT

### 10. List by best
**File:** `10-top_score.sql`

Write a script that lists all records of the table `second_table` from the database `hbtn_0c_0` in your MySQL server.
- Results should display both score and name (in this order).
- Records should be ordered by score (top first).

### 11. Select the best
**File:** `11-best_score.sql`

Write a script that lists all records with a score >= 10 in the table `second_table` from the database `hbtn_0c_0` in your MySQL server.
  
### 12. Cheating is bad
**File:** `12-no_cheating.sql`

Write a script that updates Bob's score to 10 in the table `second_table`.

### 13. Score too low
**File:** `13-change_class.sql`

Write a script that removes all records with a score <= 5 from the table `second_table` of the database `hbtn_0c_0`.

### 14. Average
**File:** `14-average.sql`

Write a script that computes the average score of all records in the table `second_table` from the database `hbtn_0c_0`.

### 15. Number by score
**File:** `15-groups.sql`

Write a script that lists the number of records with the same score from the table `second_table` of the database `hbtn_0c_0`.
- The result should display:
  - The score 
  - The number of records for this score labeled as "number".
- The list should be sorted by number of records (descending).

### 16. Say my name
**File:** `16-no_link.sql`

Write a script that lists all records from the table second_table of the database hbtn_0c_0, excluding rows without a name value.
- Results should display score and name (in this order).
- Records should be listed by descending score.

Authors :
[Zyke](https://github.com/ZykeLaDebrouille)