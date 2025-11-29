FastAPI CRUD & GET Methods — Learning Project

This repository contains a collection of beginner-friendly FastAPI examples demonstrating GET, POST, PUT, and DELETE operations.
The project is designed to help understand how FastAPI handles routing, path parameters, query parameters, and Pydantic models.

🚀 Features
✔️ Basic GET Endpoints

Includes routes for:

Simple greeting

Dynamic greetings using path parameters

Mathematical operations (square, addition)

Nested route parameters

Query parameters for filtering results

✔️ CRUD Operations

Includes routes for:

Create User (POST)

Update User (PUT)

Delete User (DELETE)

✔️ Pydantic Models

A User model is used to validate incoming request bodies containing:

name

age

email

📁 Project Structure
📦 FastAPI-Basics
 ┣ 📜 Crud.py              # POST, PUT, DELETE examples
 ┣ 📜 Get_Methods.py       # Multiple GET endpoints
 ┣ 📜 Put.py               # Standalone PUT example
 ┗ 📜 requirements.txt     # (optional) FastAPI & Uvicorn dependencies

📌 Endpoints Overview
🔹 GET Endpoints (Get_Methods.py)
Method	Endpoint	Description
GET	/	Welcome message
GET	/hello	Static greeting
GET	/hello/{name}	Dynamic greeting
GET	/square/{num}	Returns square of a number
GET	/User/{user_id}/Order/{order_id}	Demonstrates nested parameters
GET	/add?a=10&b=20	Query-based addition
GET	/users?role=student&limit=10	Query params example
🔹 CRUD Endpoints (Crud.py)
Method	Endpoint	Description
POST	/create-user	Creates a user using request body
PUT	/update-user/{user_id}	Updates a user
DELETE	/delete-user/{user_id}	Deletes a user
🔹 PUT Endpoint (Put.py)

A separate example focused on updating user details.

▶️ How to Run the Project

Install dependencies:

pip install fastapi uvicorn


Run any file using Uvicorn:

uvicorn Crud:app --reload


Or:

uvicorn Get_Methods:app --reload


Open your browser and visit:

http://127.0.0.1:8000


Access automatic API documentation:

http://127.0.0.1:8000/docs

🧑‍💻 Technologies Used

FastAPI — High-performance API framework

Pydantic — Data validation

Uvicorn — ASGI server

📚 Purpose of This Project

This repository is created as part of my FastAPI learning journey.
It covers the fundamentals needed to build REST APIs, including routing, request handling, data validation, and CRUD structure.
