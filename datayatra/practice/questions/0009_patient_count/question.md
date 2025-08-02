## Show total number of patients from each district of Bihar

#### Table: `patient`

| Column     | Data Type | Description                      |
|------------|-----------|----------------------------------|
| id         | INT       | Unique patient ID                |
| name       | VARCHAR   | Patient's full name              |
| gender     | VARCHAR   | Gender (Male/Female/Other)       |
| dob        | DATE      | Date of birth                    |
| aadhar_no  | VARCHAR   | 12-digit Aadhar number           |
| address    | TEXT      | Full address                     |
| district   | VARCHAR   | District patient belongs to      |
| state      | VARCHAR   | State patient belongs to         |

#### 📄 Description:  
District-wise patient distribution is a vital metric for healthcare policy planning. This question focuses on using the `GROUP BY` clause along with filtering patients from the state of **Bihar**.

#### 🎯 Objective:  
Write a query to show the **district** and corresponding **total number of patients** from each district of **Bihar**.

#### 📥 Example Input (`patient` table):

| id | name         | gender | dob        | aadhar_no   | address              | district     | state |
|----|--------------|--------|------------|-------------|----------------------|--------------|--------|
| 1  | Rani Devi    | Female | 1980-04-11 | 123456789012| Gaya Bazaar, Bihar   | Gaya         | Bihar  |
| 2  | Rajat Kumar  | Male   | 1992-01-01 | 234567890123| Main Road, Patna     | Patna        | Bihar  |
| 3  | Arvind Yadav | Male   | 1985-03-23 | 345678901234| Civil Lines, Gaya    | Gaya         | Bihar  |
| 4  | Priya Singh  | Female | 1999-09-09 | 456789012345| Kankarbagh, Patna    | Patna        | Bihar  |
| 5  | Sanjay Jha   | Male   | 1975-12-12 | 567890123456| Sector 1, Ranchi     | Ranchi       | Jharkhand |

#### 🎯 Expected Output:

| district | total_patients |
|----------|----------------|
| Gaya     | 2              |
| Patna    | 2              |

#### 🔰 Difficulty: Medium
