<h1>COVID-19 Analyzer</h1>

<h2>About the Project</h2>
### Please visit the link below to to the PPT and a demo video:

https://drive.google.com/drive/folders/1ZJkS0VXSl_grxlaYHkF1nKh8tB2x3ZF0?usp=sharing

<h2>Project Setup</h2>

- Clone this Repo
- Go to the root folder of this Repo

## Installing Dependencies

- Backend: Django (Python)

```bash
pip install -r reqiuirements.txt
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