<h1>COVID-19 Analyzer</h1>

<h2>About the Project</h2>
<h6>Please visit the link below to to the PPT and a demo video:</h6>

https://drive.google.com/drive/folders/1ZJkS0VXSl_grxlaYHkF1nKh8tB2x3ZF0?usp=sharing

## Note: We had mentioned postgresql in our solution. The default database is sqlite as in case you don't want to setup postgresql. Follow the given steps only if you want to use postgresql, otherwise the default database will be sqlite.
- Go to SA_COVID_19/settings.py
- Comment out the database part of sqlite
- Uncomment the database part above it (of postgresql)
- On pgAdmin, create:
    - user with admin rights, with username and password: 'sa_covid_19'
    - database with name: sa_covid_19
    - host: localhost
    - port: 5432

<h2>Project Setup</h2>

- Clone this Repo
- Go to the root folder of this Repo

## Installing Dependencies

- Backend: Django (Python)

```bash
pip install -r requirements.txt
```

- Frontend: React (JavaScript)

```bash
npm install
```
Or if using yarn
```bash
yarn
```

## Configuring environment variables

- Make a '.env' file in the root folder of this project
- Copy the contents of the '.env.example' file in the '.env' file
- Fill the credentials inside the single quotes in the '.env' file
- Third Party Credentials:
    - Twitter access token
    - Twitter access token secret
    - Twitter consumer key
    - Twitter consumer key secret
    - Google maps API key
    - IBM Tone analyzer key
    - IBM Tone analyzer url
    - IBM assistant (watson assistant) id
    - IBM assistant (watson assistant) service id
- Setup Admin title and header for the website and url for main website (default values are set in .env.example file just copy paste them)

## Starting the server

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## Starting the react application

```bash
npm start
```
Or if using yarn
```bash
yarn start
```