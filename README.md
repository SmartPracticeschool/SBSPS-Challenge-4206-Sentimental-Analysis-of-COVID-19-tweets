<h1>COVID-19 Analyzer</h1>

<h2>About the Project</h2>
<h6>Please visit the link below to to the PPT and a demo video:</h6>

https://drive.google.com/drive/folders/1ZJkS0VXSl_grxlaYHkF1nKh8tB2x3ZF0?usp=sharing

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