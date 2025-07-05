# 🏏 SQL Challenge: Cricket Match Analysis

## 🧩 Problem Statement

You are given a table named `match_scores` that contains the performance statistics of players in a T20 cricket league. Your task is to filter and sort the data using conditional logic.

### 📊 Table: `match_scores`

| Column Name     | Data Type    | Description                            |
|------------------|--------------|----------------------------------------|
| match_id         | INT          | Unique ID for each match               |
| player_name      | VARCHAR      | Name of the player                     |
| team_name        | VARCHAR      | Team to which the player belongs       |
| runs_scored      | INT          | Runs scored by the player in the match|
| balls_faced      | INT          | Balls faced by the player             |
| is_out           | BOOLEAN      | TRUE if the player got out             |
| match_date       | DATE         | Date of the match                      |

---

## 📝 Question

Write an SQL query to **find the names of players** who:

- Belong to the team `'Super Strikers'` **or** `'Power Hitters'`
- Scored **more than 30 runs**
- **Did not get out** in the match
- The match was **not played in the month of May**
- Order the result by `runs_scored` in **descending** order and then by `player_name` in **ascending** order

### ✅ Expected Output Columns

- `player_name`
- `team_name`
- `runs_scored`
- `match_date`

---

## 💡 Hints

- Use `WHERE` to filter the team and conditions.
- Use `OR`, `AND`, and `NOT` carefully to combine conditions.
- Use the `MONTH()` function to extract the month from `match_date`.
- Use `ORDER BY` with multiple columns.

---

## 📥 Sample Data

| match_id | player_name | team_name      | runs_scored | balls_faced | is_out | match_date |
|----------|-------------|----------------|-------------|-------------|--------|------------|
| 1        | R. Sharma   | Super Strikers | 45          | 32          | FALSE  | 2024-04-21 |
| 2        | V. Kohli    | Power Hitters  | 60          | 40          | TRUE   | 2024-05-11 |
| 3        | D. Padikkal | Power Hitters  | 35          | 28          | FALSE  | 2024-06-12 |
| 4        | M. Agarwal  | Super Strikers | 20          | 18          | FALSE  | 2024-06-10 |

✅ From this data, the output should include:
- R. Sharma
- D. Padikkal

---

