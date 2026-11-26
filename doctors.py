# Generate 100 doctors for MySQL

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

# Create doctors.sql
with open("doctors.sql", "w", encoding="utf-8") as f:

    for x in range(100):

        first_name = random.choice(first_names)
        last_name = random.choice(last_names)

        dob = fake.date_of_birth(
            minimum_age=30,
            maximum_age=65
        )

        address = fake.street_address()
        address = address.replace("'", "")

        phone = "".join(
            c for c in fake.phone_number()
            if c.isdigit()
        )

        email = (
            first_name.lower()
            + "."
            + last_name.lower()
            + "@hospital.com"
        )

        hospital_id = random.randint(1, 40)

        sql = f"""INSERT INTO doctors
(first_name,last_name,date_of_birth,address,phone_number,email,hospital_id)
VALUES
('{first_name}','{last_name}','{dob}','{address}','{phone}','{email}',{hospital_id});

"""

        f.write(sql)

print("100 doctors generated successfully.")
print("File created: doctors.sql")