Got it, Pranav — here’s a **clean, concise, no-fluff `README.md`** that strictly follows the assignment requirement:

> *"Include a README file with instructions on how to set up and run the application"*

Everything is in a **single markdown block** — ready to paste and push.

---

````markdown
# Flask CRUD API using MongoDB (Dockerized)

This is a Flask application that provides REST API endpoints to perform CRUD (Create, Read, Update, Delete) operations on a MongoDB database for a User resource. The application is containerized using Docker and fully tested using Postman.

## How to Set Up and Run the Application

### 1. Clone the Repository

```bash
git clone https://github.com/Pranavchikte/Flask-crud.git
cd Flask-crud
````

### 2. Create Environment File

Copy the example file to `.env`:

```bash
cp .env.example .env
```

Make sure it contains:

```env
FLASK_ENV=development
MONGODB_URI=mongodb://mongo:27017/users_db
```

### 3. Run the Application using Docker

Make sure Docker is installed and running, then run:

```bash
docker-compose up --build
```

This starts both the Flask API and MongoDB.
The API will be available at: `http://localhost:5000`

### 4. Test the API with Postman

Use the following endpoints:

* `GET /users` – List all users
* `GET /users/<id>` – Get user by ID
* `POST /users` – Create new user
* `PUT /users/<id>` – Update user by ID
* `DELETE /users/<id>` – Delete user by ID

#### Sample POST body:

```json
{
  "name": "Pranav",
  "email": "pranav@example.com",
  "password": "securepass123"
}
```

### 5. Stop the Application

To stop and remove containers:

```bash
docker-compose down
```

## Notes

* All passwords are securely hashed using Werkzeug.
* MongoDB is run inside Docker; no local installation is needed.

```

---

✅ You can now copy this into `README.md`, commit, and push.

Let me know if you'd like a **Postman collection export section** or a **sample submission message** for email or portal.
```
