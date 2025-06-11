# Multiple Cardio Visits

## 📋 Table: `patient_visits`

| Column Name     | Data Type | Description                             |
|------------------|-----------|-----------------------------------------|
| visit_id         | INT       | Unique identifier for the visit         |
| patient_id       | INT       | ID of the patient                       |
| doctor_id        | INT       | ID of the doctor seen during the visit  |
| visit_date       | DATE      | Date of the visit                       |
| department       | VARCHAR   | Department of the hospital visited      |
| diagnosis_code   | VARCHAR   | Diagnosis code assigned                 |

---

## 🧾 Question Description

Write an SQL query to find the IDs of **unique patients** who have visited the **Cardiology department** more than **once**, based on distinct visit dates. A patient is considered to have multiple visits if they have entries on **different dates** to the Cardiology department.

Return only the `patient_id`s of such patients.

---

## 🧪 Example Input

Table: `patient_visits`

| visit_id | patient_id | doctor_id | visit_date | department  | diagnosis_code |
|----------|------------|-----------|------------|-------------|----------------|
| 1        | 1001       | 201       | 2024-01-01 | Cardiology  | C01            |
| 2        | 1002       | 202       | 2024-01-02 | Cardiology  | C02            |
| 3        | 1002       | 203       | 2024-01-05 | Cardiology  | C03            |
| 4        | 1003       | 204       | 2024-01-07 | Neurology   | N01            |
| 5        | 1031       | 205       | 2024-02-10 | Cardiology  | C02            |
| 6        | 1031       | 206       | 2024-02-15 | Cardiology  | C03            |
| 7        | 1105       | 207       | 2024-03-01 | Cardiology  | C05            |
| 8        | 1105       | 207       | 2024-03-02 | Cardiology  | C05            |
| 9        | 1001       | 201       | 2024-03-05 | Oncology    | O01            |

---

## ✅ Example Output

| patient_id |
|------------|
| 1002       |
| 1031       |
| 1105       |

---

## 🏷️ Tags

`medium` `sql` `select distinct` `group by` `healthcare` `data filtering` `cardiology`
