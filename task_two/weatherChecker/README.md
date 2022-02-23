# Weather Checker API

Weather Checker is a simple web app that uses the open source data available on openweather api to create a database of the current temprature in various cities

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.


## Running

To Run this project you will need postgres installed and running
To start up make sure to activate the environment
```bash
source weatherenv/bin/activate
```
The details are added into the settings.py file (below), please change as required 

DATABASES = {
    'default': {

        'ENGINE': 'django.db.backends.postgresql_psycopg2',

        'NAME': 'weatherData',

        'USER': {{DATABASE USERNAME}},

        'PASSWORD': {{DATABASE PASSWORD}},

        'HOST': 'localhost',

        'PORT': '5432',

    }
}
Once Navigated into the project we can then use basic django to start up the App

```bash
 python manage.py makemigrations weatherApp
 python manage.py migrate weatherApp
 python manage.py runserver
```

## Technical Details

Because of the nature of the form I chose to create the user could insert a city of any type so chose to strip all the capitals from the word for consistency within the database, resulting in only one table row for SYDNEY and sydney

I chose to publish results to the page including an error where this occurs, partly so a User was aware that they may have made a spelling mistake or that the API was not working

Currently only the temperature is stored within the database but as the output of the function that makes the apicalls is a dictionary we have a number of options to expand this further if required

