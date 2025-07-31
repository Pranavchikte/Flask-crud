# Flask CRUD API with MongoDB (Dockerized)

A scalable Flask application with RESTful API for performing **CRUD operations on MongoDB**, built using **MongoEngine**, and **containerized with Docker**. This assignment meets the requirements given for the SDE Intern Task.

---

## Problem Statement (from Assignment)

> Build a Flask application that performs **CRUD (Create, Read, Update, Delete)** operations on a MongoDB database for a `User` resource via REST API, tested using Postman. Use Docker. Emphasis is on **code structure**, **scalability**, and **clean system design**.

---

## Tech Stack

- **Python 3.11**
- **Flask** – Web framework
- **MongoDB** – NoSQL database
- **MongoEngine** – MongoDB ORM for Python
- **Docker + Docker Compose** – Container orchestration
- **Werkzeug** – Password hashing
- **Postman** – API testing

---

## Folder Structure

flask-crud/
├── app/
│ ├── models/ # MongoEngine schema
│ ├── routes/ # Flask Blueprint routes
│ ├── services/ # Core business logic
│ ├── utils/ # Helpers (future extension)
│ └── init.py # App factory + Mongo config
│
├── run.py # Entry point
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .env # Local environment vars (excluded from git)
├── .env.example # Sample env config
├── README.md

 Step-by-Step Instructions
 
 1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/Pranavchikte/Flask-crud.git
cd Flask-crud

 2. Setup Environment File
Create a .env file by copying the example:

bash
Copy
Edit
cp .env.example .env
Make sure it contains:

env
Copy
Edit
FLASK_ENV=development
MONGODB_URI=mongodb://mongo:27017/users_db
No need to change anything — this is already configured to work inside Docker.

 3. Build and Run with Docker
Make sure Docker is installed and running on your machine.

bash
Copy
Edit
docker-compose up --build
This will spin up two containers:

flask-app (your API)

mongo (MongoDB database)

Flask will be available at:

arduino
Copy
Edit
http://localhost:5000
