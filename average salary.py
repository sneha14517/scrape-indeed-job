from pymongo import MongoClient
import numpy as np

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")  # Update if necessary
db = client["indeed_jobs"]
collection = db["python_developer_jobs"]


def calculate_average_salary():
    salaries = []
    for job in collection.find():
        salary = job.get('salary', 'N/A')
        if salary == 'N/A' or not salary.strip():
            continue

        salary = salary.replace('$', '').replace(',', '').split()[0]

        try:
            salaries.append(float(salary))
        except ValueError:
            print("Skipping invalid salary value: {salary}")
            continue

    return np.mean(salaries) if salaries else "No salary data available"

print("Average Salary: {calculate_average_salary():.2f}")