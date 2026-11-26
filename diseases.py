# generate_diseases.py

diseases = [
    "Diabetes",
    "Hypertension",
    "Asthma",
    "Arthritis",
    "Migraine",
    "Pneumonia",
    "Influenza",
    "Heart Disease",
    "Depression",
    "Anxiety",
    "Tuberculosis",
    "COVID-19",
    "Cancer",
    "Osteoporosis",
    "Bronchitis",
    "Kidney Disease",
    "Liver Disease",
    "Epilepsy",
    "Alzheimer's Disease",
    "Parkinson's Disease"
]

with open("diseases.sql", "w") as f:
    for disease in diseases:
        f.write(
            f"INSERT INTO Diseases (disease_name) VALUES ('{disease}');\n"
        )

print("Disease SQL file generated.")