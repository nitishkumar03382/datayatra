## List the names of all government hospitals in Bihar

#### Table: `hospital`

| Column   | Data Type | Description                              |
|----------|-----------|------------------------------------------|
| id       | INT       | Unique hospital ID                       |
| name     | VARCHAR   | Hospital's name                          |
| type     | VARCHAR   | 'Government' or 'Private'                |
| state    | VARCHAR   | State in which the hospital is located   |
| district | VARCHAR   | District in which the hospital is located|

#### 📄 Description:  
Understanding the distribution of **government hospitals** across states helps analyze public healthcare infrastructure. This query focuses on filtering hospitals by **type** and **location**.

#### 🎯 Objective:  
Write a query to retrieve the names of all hospitals that are **government-run** and located in the state of **Bihar**.

#### 📥 Example Input (`hospital` table):

| id | name                      | type        | state | district     |
|----|---------------------------|-------------|-------|--------------|
| 1  | Patna Medical College     | Government  | Bihar | Patna        |
| 2  | AIIMS Delhi               | Government  | Delhi | New Delhi    |
| 3  | Fortis Hospital Mumbai    | Private     | Maharashtra | Mumbai |
| 4  | Nalanda District Hospital | Government  | Bihar | Nalanda      |
| 5  | Max Hospital              | Private     | Bihar | Patna        |

#### 🎯 Expected Output:

| name                      |
|---------------------------|
| Patna Medical College     |
| Nalanda District Hospital |

#### 🔰 Difficulty: Easy
