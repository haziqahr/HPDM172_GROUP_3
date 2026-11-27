# HPDM172_GROUP_3

# Hospital Database Management System

## Overview

This project was developed for the **HPDM172 Computational Skills for Health and Life Sciences** module. The aim of the project is to design and implement a relational hospital database using MySQL.

The system manages hospitals, doctors, patients, medications, prescriptions, diseases, appointments, and laboratory results. The database demonstrates the use of relational database design, primary and foreign keys, SQL queries, and automated data generation using Python.

---

## Project Objectives

- Develop a hospital database in MySQL.
- Create relationships between database tables.
- Generate realistic sample data using Python.
- Implement SQL queries to retrieve and manipulate data.
- Demonstrate the use of joins, subqueries, filtering, and aggregation.
- Use Git and GitHub for version control and collaboration.

---

## Database Tables

### Hospitals
Stores information about hospitals including:

- Hospital ID
- Hospital Name
- Address
- Number of Beds
- Hospital Type
- Accreditation Year
- Emergency Service Status

### Doctors
Stores doctor information including:

- Doctor ID
- Hospital ID
- First Name
- Last Name
- Date of Birth
- Address

### Patients
Stores patient information including:

- Patient ID
- Doctor ID
- First Name
- Last Name
- Date of Birth
- Address

### Medications
Stores medication details including:

- Medication ID
- Medication Name

### Prescriptions
Stores prescription records including:

- Prescription ID
- Patient ID
- Doctor ID
- Medication ID
- Prescription Date

### Diseases
Stores disease information.

### Disease_Medications
Links diseases to medications used for treatment.

### Doctor_Disease_Specialties
Links doctors to diseases they specialise in.

### Appointments
Stores appointment information including:

- Appointment ID
- Patient ID
- Doctor ID
- Appointment Date and Time
- Appointment Status
- Appointment Reason

### LabResults
Stores laboratory test records including:

- Lab Result ID
- Patient ID
- Doctor ID
- Test Type
- Result
- Test Date

---

## Database Relationships

The database contains the following relationships:

- One Hospital can have many Doctors.
- One Doctor can have many Patients.
- One Patient can have many Prescriptions.
- One Medication can be prescribed to many Patients.
- Doctors can specialise in multiple Diseases.
- Diseases can be treated by multiple Medications.
- Patients can have multiple Appointments.
- Patients can have multiple Lab Results.

---

## Data Generation

Python scripts were developed to automatically generate realistic sample data for the database, including:

- 2 Hospitals
- 100 Doctors
- 600 Patients
- 30 Medications
- 500 Prescriptions
- Diseases
- Appointments
- Laboratory Results

The generated data was imported into MySQL using SQL scripts.

---

## SQL Queries Implemented

### Basic Queries

1. List all doctors based at a particular hospital.
2. List all prescriptions for a particular patient ordered by prescription date.
3. List all prescriptions prescribed by a specific doctor.
4. Display all prescriptions ordered alphabetically by patient name.

### Advanced Queries

5. Add a new patient to the database.
6. Modify a patient's address.
7. Display patients registered with doctors at a selected hospital.
8. Display doctors based at teaching hospitals accredited between 2015 and 2024.
9. Identify patients who may have a particular disease based on prescribed medication.
10. List doctors who specialise in a specific disease.
11. Display all lab results for patients over 60 years old.
12. Display appointments for a given patient.
13. Display appointments for a given doctor.
14. Display prescriptions from a particular hospital ordered by medication name.
15. Identify the doctor who has made the most prescriptions.
16. Display all doctors working at the hospital with the largest number of beds.
17. List hospitals accredited before 2015 that provide emergency services.
18. List patients registered with doctors from hospitals containing fewer than 400 beds.
19. Display lab results from hospitals accredited between 2013 and 2020.

---

## Technologies Used

- MySQL
- SQL
- Python
- Git
- GitHub

---

## Repository Structure

```text
Hospital-Database/
│
├── hospitals
├── doctors.py
├── patients.py
├── medications.py
├── prescriptions.py
├── diseases.py
├── appointments.py
├── lab_results.py
│
├── hospital_database.sql
├── sql_queries.sql
│
├── ERD/
│   └── erd_diagram.png
│
├── TeamPortfolio/
│   ├── Meeting_Agenda_1
│   ├── Meeting_Agenda_2
│   ├── Meeting_Minutes_1
│   ├── Meeting_Minutes_2
│   └── Action_Plan
│
└── README.md
```

---

## Learning Outcomes

This project demonstrates:

- Relational database design
- Entity Relationship Diagram (ERD) development
- SQL query writing
- Data generation using Python
- Database normalisation
- Version control using Git and GitHub
- Collaborative software development

---

## Authors
- Abraham Nkrumah
- Ferrao Sarah Rosario
- Hj Abdul Razak Haziqah
- Onyemachi Favour Chioma
- Kunnumpurath Gireesh Abhirami
