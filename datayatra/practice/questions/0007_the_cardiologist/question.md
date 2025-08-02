## Find all doctors with specialization in 'Cardiology'


#### Table: `doctor`

| Column           | Data Type   | Description                             |
|------------------|-------------|-----------------------------------------|
| id               | INT         | Unique doctor ID                        |
| name             | VARCHAR     | Doctor's full name                      |
| specialization   | VARCHAR     | Medical field (e.g., Cardiology)        |
| is_government    | BOOLEAN     | Whether the doctor is in Govt. service  |
| years_experience | INT         | Total years of experience               |


#### 📄 Description:  
In a healthcare system, knowing the availability of specialist doctors like cardiologists is crucial for treatment planning. This question checks your ability to use **simple filtering** 

#### 🎯 Objective:  
Write a query to retrieve the names and experience of all doctors who specialize in **Cardiology**.

#### 📥 Example Input (`doctor` table):

| id | name            | specialization | is_government | years_experience |
|----|-----------------|----------------|----------------|------------------|
| 1  | Dr. A. Sinha    | Cardiology     | TRUE           | 12               |
| 2  | Dr. R. Mehra    | Dermatology    | FALSE          | 8                |
| 3  | Dr. Neha Shah   | Cardiology     | TRUE           | 6                |
| 4  | Dr. I. Qureshi  | Neurology      | FALSE          | 15               |



#### 🎯 Expected Output:

| name          | years_experience |
|---------------|------------------|
| Dr. A. Sinha  | 12               |
| Dr. Neha Shah | 6                |



#### 🔰 Difficulty: Easy
