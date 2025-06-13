# A Data Engineer Nightmare

## 📋 Table: `etl_scheduler`

| Column Name    | Data Type | Description                                 |
|----------------|-----------|---------------------------------------------|
| job_name       | VARCHAR   | Name of the ETL job                         |
| schedule_time  | VARCHAR   | Cron schedule format (e.g., `0 2 * * 0`)     |

---

## 🧾 Question Description

You are given a table `etl_scheduler` that contains ETL job names and their scheduled run times using **cron expressions** in the standard 5-field format:

> `minute hour day-of-month month day-of-week`

Where:
- `day-of-week`: 0 (Sunday) to 6 (Saturday)

Write an SQL query to find all **ETL jobs** that are **scheduled to run on weekends** (i.e., on **Saturday or Sunday**, which correspond to `6` and `0` respectively in cron. Exclude all monthly or daily run jobs.

> 📝 You should only consider entries where `schedule_time` includes `0` or `6` **as the fifth field** (day-of-week).

---

## 🧪 Example Input

Table: `etl_scheduler`

| job_name     | schedule_time    |
|--------------|------------------|
| daily_sales  | 0 2 * * *         |
| weekend_run  | 30 1 * * 0        |
| weekly_sync  | 45 3 * * 6        |
| full_backup  | 0 0 * * 1         |
| log_cleanup  | 0 4 * * 0,6       |

---

## ✅ Example Output

| job_name     |
|--------------|
| weekend_run  |
| weekly_sync  |
| log_cleanup  |

---

## 🏷️ Tags

`hard` `sql` `cron` `string parsing` `etl` `scheduling`
