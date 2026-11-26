# Generate 600 patients for MySQL

import random
from faker import Faker

fake = Faker()

# Simple names only
first_names = [
    "Adam", "James", "John", "Michael", "David",
    "Daniel", "Robert", "Mark", "Thomas", "Simon",
    "Sarah", "Emma", "Mary", "Lucy", "Grace",
    "Anna", "Olivia", "Emily", "Chloe", "Rachel"
]

last_names = [
    "Gray", "Smith", "Brown", "Taylor", "Wilson",
    "Evans", "Thomas", "Jones", "White", "Walker",
    "Hall", "Young", "King", "Scott", "Green",
    "Turner", "Hill", "Ward", "Clark", "Baker"
]

with open("patients.sql", "w", encoding="utf-8") as f:

    for x in range(600):

        first_name = random.choice(first_names)
        last_name = random.choice(last_names)

        dob = fake.date_of_birth(
            minimum_age=1,
            maximum_age=95
        )

        address = fake.street_address()
        address = address.replace("'", "")

        phone = "".join(
            c for c in fake.phone_number()
            if c.isdigit()
        )

        # Assign patient to one of the 100 doctors
        doctor_id = random.randint(1, 100)

        sql = f"""INSERT INTO patients
(first_name,last_name,date_of_birth,address,phone_number,doctor_id)
VALUES
('{first_name}','{last_name}','{dob}','{address}','{phone}',{doctor_id});

"""

        f.write(sql)

print("600 patients generated successfully.")
print("File created: patients.sql")