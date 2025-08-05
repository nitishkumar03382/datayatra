# All Patients

## Table: `Patient`

| Column Name   | Data Type |
|---------------|-----------|
| id            | int       |
| name          | varchar   |
| physician_id  | int       |

---

## Task

Write an SQL query to retrieve **all patient records** from the `Patient` table.

---

## Requirements

- Select all columns.
- Return **all rows** in the table.
- The **order of output does not matter**.

---

## Example

### Input

**Patient Table**

| id | name       | physician_id |
|----|------------|--------------|
| 1  | Jhon Doe   | 096          |
| 2  | Krish Jay  | 099          |
| 4  | Herman Sen | 099          |

### Output

| id | name       | physician_id |
|----|------------|--------------|
| 1  | Jhon Doe   | 096          |
| 2  | Krish Jay  | 099          |
| 4  | Herman Sen | 099          |

---

## SQL Query

```sql
SELECT * FROM Patient;
