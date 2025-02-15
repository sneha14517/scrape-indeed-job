from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from pymongo import MongoClient
import time


client = MongoClient("mongodb://localhost:27017/")
db = client["indeed_jobs"]
collection = db["python_developer_jobs"]


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


driver.get("https://www.indeed.com/q-Python-Developer-jobs.html?vjk=7994156cad994aa3")


time.sleep(3)


soup = BeautifulSoup(driver.page_source, 'html.parser')


job_elements = soup.find_all("a", class_="jcs-JobTitle")

job_listings = []
for job_element in job_elements:
    job_title = job_element.get_text() if job_element else "N/A"
    

    company_name = job_element.find_previous("span", class_="companyName").get_text() if job_element.find_previous("span", class_="companyName") else "N/A"
    location = job_element.find_previous("div", class_="companyLocation").get_text() if job_element.find_previous("div", class_="companyLocation") else "N/A"
    

    salary = job_element.find_previous("span", class_="salaryText").get_text() if job_element.find_previous("span", class_="salaryText") else "Not Listed"
    
    
    job_listings.append({
        "job_title": job_title,
        "company_name": company_name,
        "location": location,
        "salary": salary
    })

if job_listings:
    for job in job_listings:
        result = collection.insert_one(job)
        print(f"Inserted job listing with ID: {result.inserted_id}")
else:
    print("No job listings found.")


