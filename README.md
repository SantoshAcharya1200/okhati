# Okhati Task

REST API implementation using django rest framework for managing the date/time and checking opening hour of current week.

## Features

- View/Post the date/time for opening hours
- Set the exception day
- View/Post current week opening hours


## Technologies Used

- Django
- Django Rest Framework
- PostgreSql

## Getting Started

### Prerequisites

- Python installed
- Django installed


### Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/SantoshAcharya1200/okhati.git
   cd okhati
   ```

2. Pip
     ```
    (.venv) $ pip install -r requirements.txt
    (.venv) $ python manage.py makemigrations
    (.venv) $ python manage.py migrate
    (.venv) $ python manage.py createsuperuser
    (.venv) $ python manage.py runserver
    # Load the site at http://127.0.0.1:8000
     ```
3. Connect to PostgreSql database:
   Open your Django project’s settings.py file (located inside the main project folder) and navigate to the DATABASES setting.
   By default, Django is configured to use SQLite, but we’ll change that to use PostgreSQL. Replace the DATABASES setting with the following code:
   ```
         DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_database_name',
        'USER': 'your_database_user',
        'PASSWORD': 'your_database_password',
        'HOST': 'localhost',  # Replace with your PostgreSQL server's address if necessary
        'PORT': '',          # Leave empty to use the default PostgreSQL port (usually 5432)
       }
   }
   ```
   Next, apply the initial database migrations to create the necessary tables in the PostgreSQL database. Run the following commands:
   ```
     python manage.py makemigrations
     python manage.py migrate
   ```
   Now run the server:
   ```
   py manage.py runserver
   ```
   Visit http://127.0.0.1:8000/ in your web browser, and if everything is set up correctly, you should see the Django default landing page.
##Screenshots
1. View/Post opening hour details at  http://127.0.0.1:8000/opening_hours/
   
![opening hours](https://github.com/SantoshAcharya1200/okhati/assets/41406942/e33471c9-1967-4a03-9173-5461dca0f098)

2. View/Post exception days at http://127.0.0.1:8000/exceptions/
   ![exception days](https://github.com/SantoshAcharya1200/okhati/assets/41406942/f750fda2-8306-469d-9ac7-7d5feebee6b6)
3. View Current week opening hours at http://127.0.0.1:8000/current_week_opening_hours/
   ![currentweekopeinghours](https://github.com/SantoshAcharya1200/okhati/assets/41406942/6243ea87-1e6f-42ad-aa92-f760e657508e)
