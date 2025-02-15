# Python Developer Job Scraping and Admin Panel
This project scrapes job listings for the keyword "Python Developer" from Indeed.com and stores the data in a MongoDB database. It then creates a Django Admin Panel where users can search, edit, and delete job listings. Additionally, the project uses NumPy to calculate the average salary for Python developers in the user's city.

Project Components
Web Scraping with Python

Scrapes job listings from Indeed.com for the keyword "Python Developer."
Extracts relevant information, such as job title, company, location, salary, and job description.
Stores the scraped data in a MongoDB database.
Django Admin Panel

Provides an admin panel where users can view, search, edit, and delete job listings from the MongoDB database.
Built using the Django framework, integrated with MongoDB using django-mongoengine.
Salary Analysis

Uses NumPy to calculate the average salary for Python developers in a given city.
Features
Scraping: Data is fetched using BeautifulSoup and Requests libraries.
Database: Scraped data is saved to MongoDB.
Admin Panel: Users can view and manage job listings using Django's admin interface.
Salary Calculation: NumPy is used to compute average salaries from the listings.
Hosting: Admin panel can be hosted on a platform like Heroku.
Setup Instructions
Prerequisites
Python 3.x
MongoDB (locally or via a cloud service like MongoDB Atlas)
Django
NumPy
BeautifulSoup
Requests
Django-MongoEngine (for MongoDB integration)
1. Clone the Repository
bash
Copy
git clone https://github.com/sneha14517/python-job-scraping.git
cd python-job-scraping
2. Install Dependencies
Create a virtual environment and activate it:

bash
Copy
python -m venv venv
venv\Scripts\activate  # For Windows
Install the required packages:

bash
Copy
pip install -r requirements.txt
3. Set Up MongoDB
Install MongoDB locally, or sign up for a cloud-based MongoDB service like MongoDB Atlas.
Create a database called python_jobs in MongoDB.
Update the database connection string in your Django settings (settings.py).
# settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.dummy',
        'NAME': 'python_jobs',
    },
    'mongo': {
        'ENGINE': 'django.db.backends.mongo',
        'NAME': 'python_jobs',
        'HOST': 'your_mongo_host',  # Use the connection URL
        'PORT': 27017,
    }
}
4. Run the Scraper
To scrape job listings from Indeed.com, run the script scraper.py:

bash
Copy
python scraper.py
This will scrape job listings for "Python Developer" and store them in the MongoDB database.

5. Run Django Server
Run the Django server to access the admin panel:

bash
Copy
python manage.py migrate
python manage.py runserver
Visit http://127.0.0.1:8000/admin/ to access the Django Admin Panel.

we can log in using the superuser credentials you created during the Django setup.
In the admin panel, we can search for jobs, edit their details, and delete listings.
6. Hosting the Admin Panel
To host the Django admin panel, you can deploy the app to Heroku or another hosting platform.

Follow the official Heroku deployment guide for Django.
Push your code to Heroku and set up the environment variables for MongoDB.
Salary Calculation with NumPy
You can calculate the average salary for Python developers in your city by running the following command:

bash
Copy
python salary_calculation.py
This will calculate the average salary by processing the salary information from the job listings stored in MongoDB.

Project Structure
bash
Copy
python-job-scraping/
│
├── admin.py              # Django admin configuration
├── manage.py             # Django project management
├── models.py             # Database models (MongoDB)
├── scraper.py            # Web scraping script
├── salary_calculation.py # Salary analysis using NumPy
├── settings.py           # Django settings
├── requirements.txt      # List of dependencies
└── README.md             # Project documentation
Technologies Used
Python: Programming language for scraping, backend, and calculations.
Django: Web framework for creating the admin panel.
MongoDB: NoSQL database to store job listings.
NumPy: Used to calculate the average salary.
BeautifulSoup: HTML parsing library to scrape job listings from Indeed.
Requests: HTTP library to fetch web pages for scraping.


Acknowledgments
Indeed.com for the job listings data.
MongoDB for the database solution.
Django for the easy-to-use admin panel.
NumPy for the salary analysis functionality.
