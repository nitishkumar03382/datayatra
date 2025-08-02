# Show patient details whose Aadhar number ends with 5

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

---

#### 📄 Description:  
A government officer in Bihar is trying to locate a patient from **Aurangabad district**, but the only information available is that the person’s **Aadhar number ends with the digit '5'**.  
To assist in identifying the individual, the officer needs to fetch all patients in the **`patient`** table whose **Aadhar ends with '5'** and **belong to Aurangabad**.

---

#### 🎯 Objective:  
Write a SQL query to return **all patient details** where **Aadhar number ends with '5'** and the **district is 'Aurangabad'**.

---

#### 📥 Example Input (`patient` table):

| id | name         | gender | dob        | aadhar_no   | address                | district   | state     |
|----|--------------|--------|------------|-------------|------------------------|------------|-----------|
| 1  | Rani Devi    | Female | 1980-04-11 | 123456789015| Shahpur, Aurangabad    | Aurangabad | Bihar     |
| 2  | Rajat Kumar  | Male   | 1992-01-01 | 234567890123| Patna Main Road        | Patna      | Bihar     |
| 3  | Arvind Yadav | Male   | 1985-03-23 | 345678901235| Civil Lines, Aurangabad| Aurangabad | Bihar     |
| 4  | Jyoti Singh  | Female | 1990-06-15 | 456789012348| Gaya Bazaar            | Gaya       | Bihar     |

---

#### 📤 Expected Output:

| id | name         | gender | dob        | aadhar_no   | address                | district   | state     |
|----|--------------|--------|------------|-------------|------------------------|------------|-----------|
| 1  | Rani Devi    | Female | 1980-04-11 | 123456789015| Shahpur, Aurangabad    | Aurangabad | Bihar     |
| 3  | Arvind Yadav | Male   | 1985-03-23 | 345678901235| Civil Lines, Aurangabad| Aurangabad | Bihar     |

---

#### 🔰 Difficulty: Easy
