## Identify the Most Visited Hospital in Bihar

#### Table: `visit`

| Column       | Data Type | Description                       |
|--------------|-----------|-----------------------------------|
| id           | INT       | Unique visit ID                   |
| patient_id   | INT       | Reference to patient ID           |
| hospital_id  | INT       | Reference to hospital ID          |
| visit_date   | DATE      | Date of the hospital visit        |

#### Table: `hospital`

| Column       | Data Type | Description                        |
|--------------|-----------|------------------------------------|
| id           | INT       | Unique hospital ID                 |
| name         | VARCHAR   | Name of the hospital               |
| district     | VARCHAR   | District where it is located       |
| state        | VARCHAR   | State where hospital is located    |

#### 📄 Description:  
The Bihar Health Department is analyzing hospital footfall across the state. They are interested in identifying the busiest hospital to improve staff allocation and medical supplies. An analyst has been given the hospital visit logs and hospital details to generate a report.

#### 🎯 Objective:  
Write a SQL query to find the **name** and **total number of visits** for the hospital with the **maximum number of visits in Bihar**.

#### 📥 Example Input (`hospital` table):

| id | name              | district     | state  |
|----|-------------------|--------------|--------|
| 1  | Patna General     | Patna        | Bihar  |
| 2  | Aurangabad Care   | Aurangabad   | Bihar  |
| 3  | Ranchi Trauma     | Ranchi       | Jharkhand |

#### 📥 Example Input (`visit` table):

| id | patient_id | hospital_id | visit_date |
|----|------------|-------------|------------|
| 1  | 101        | 1           | 2023-01-02 |
| 2  | 102        | 1           | 2023-01-05 |
| 3  | 103        | 2           | 2023-01-07 |
| 4  | 104        | 1           | 2023-01-08 |

#### 🎯 Expected Output:

| name           | total_visits |
|----------------|---------------|
| Patna General  | 3             |

#### 🔰 Difficulty: Medium
