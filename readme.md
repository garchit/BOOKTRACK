BOOKTRACK is a library management system built with Vue.js , Flask also implemented with redis and celery for asynchronus backend operations. 
It allows users to track and manage books effectively, providing functionalities like user authentication, book searching, and more. 

## Table of Contents

- [Features](#features)

- [Installation](#installation)
- [Usage](#usage)


- [Technologies Used](#technologies-used)
- [Contributers](#contributers)
- [License](#license)


## Features

- User authentication (login/signup)
- Search books
- Track borrowed and returned books
- Responsive UI with Vue.js
- API integration with Flask backend
- For asynchronus backend operations Celery redis is used 
- Asynchronus Daily Reminders 

## Installations 

Install the Python version (Python 3.9) if not already installed. You can download it from the official Python website: Python Downloads

- Install backend dependencies using pip:
- Inside backend Folder 
pip install -r requirements.txt

Install and set up Redis:

- Linux:

sudo apt-get update
sudo apt-get install redis-server
sudo systemctl start redis-server


- Install Celery with Redis backend:

pip install celery[redis]

- Install frontend dependencies using npm(Inside Frontend Folder):

npm install

- Set Up MailHog 

sudo apt-get -y install golang-go
go install github.com/mailhog/MailHog@latest


## Usage
- open the main folder 
    change directory to bootcamp 

npm run serve 

    change directory to backend

python app.py

    open Terminals in wsl 

redis-server

    open new terminal again 

go/bin/mailhog

    open new terminal change directory to backend 

celery -A teask.celery worker --loglevel "INFO"

    open new terminal change directory to backend 

celery -A teask.celery beat --loglevel "INFO"



## Technologies Used
- Frontend: Vue.js, Axios, Material-UI , Bootstrap
- Backend: Flask, SQLAlchemy, Celery, Redis
- Database: Sqlite , redis 

## Contributers
Contributions are welcome! Please fork the repository and submit a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.



