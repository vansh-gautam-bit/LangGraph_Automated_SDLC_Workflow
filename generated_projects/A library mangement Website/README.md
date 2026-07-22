# A library mangement Website

## Project Overview
A library management website is a web application designed to manage library operations, including user management, book cataloging, and chatbot support. This project utilizes FastAPI and langchain to provide a robust and scalable solution.

## Features
- User management system
- Book cataloging and search functionality
- Chatbot support for user queries
- Secure authentication and authorization
- Scalable and high-performance architecture

## Folder Structure
```bash
backend/
config/
__init__.py
database.py
security.py
app/
__init__.py
main.py
core/
__init__.py
models/
__init__.py
user.py
user_data.py
chatbot_log.py
schemas/
__init__.py
user.py
user_data.py
chatbot_log.py
routes/
__init__.py
chatbot.py
database.py
services/
__init__.py
chatbot_service.py
database_service.py
utils/
__init__.py
logging.py
security.py
requirements.txt
Dockerfile
docker-compose.yml
tests/
__init__.py
test_core.py
test_routes.py
test_services.py
```

## Installation
1. Clone the repository using `git clone`
2. Install dependencies using `pip install -r requirements.txt`
3. Build the Docker image using `docker build -t library-management-website .`
4. Run the Docker container using `docker-compose up`

## Running the Project
1. Start the Docker container using `docker-compose up`
2. Access the application at `http://localhost:8000`

## API Overview
The API provides the following endpoints:
- User management: `/users`, `/users/{id}`
- Book cataloging: `/books`, `/books/{id}`
- Chatbot support: `/chatbot`, `/chatbot/{query}`

## Technology Stack
- FastAPI: Web framework for building high-performance APIs
- langchain: AI-powered chatbot library
- Docker: Containerization platform for deployment
- PostgreSQL: Database management system for storing user and book data