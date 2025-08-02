# All Patients

### Table: `patient`

| Column      | Data Type   | Description                    |
|-------------|-------------|--------------------------------|
| id          | INT         | Unique patient ID              |
| name        | VARCHAR     | Patient's full name            |
| gender      | VARCHAR     | Gender (Male/Female/Other)     |
| dob         | DATE        | Date of birth                  |
| aadhar_no   | VARCHAR     | Aadhar number (12-digit)       |
| address     | TEXT        | Full address                   |
| district    | VARCHAR     | District the patient belongs to|

---
#### 📄 Description:  
In any healthcare system, maintaining a registry of all patients is fundamental. This question tests your ability to perform a **basic SELECT** operation from the `patient` table.

#### 🎯 Objective:  
Write a query to fetch the name, gender, and district of all patients in the system.

#### 📦 Table Involved:  
- `patient(id, name, gender, dob, aadhar_no, address, district)`

#### 📥 Example Input (`patient` table):

| id | name           | gender | dob        | aadhar_no     | address                     | district     |
|----|----------------|--------|------------|---------------|-----------------------------|--------------|
| 1  | Rahul Verma    | Male   | 1992-04-15 | 123456789012  | 123 MG Road, Kanpur         | Kanpur       |
| 2  | Asha Rani      | Female | 1985-10-20 | 987654321098  | 45 Civil Lines, Bhopal      | Bhopal       |
| 3  | Ramesh Kumar   | Male   | 1975-12-05 | 112233445566  | Sector 3, Gandhinagar       | Gandhinagar  |

---

#### 🎯 Expected Output:

| name         | gender | district    |
|--------------|--------|-------------|
| Rahul Verma  | Male   | Kanpur      |
| Asha Rani    | Female | Bhopal      |
| Ramesh Kumar | Male   | Gandhinagar |

---



#### 🧪 Expected Output Columns:  
- `name`
- `gender`
- `district`



#### 🔰 Difficulty: Easy
