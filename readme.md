# User Authentication Microservice

This is a user authentication microservice built using Django and Django Rest Framework. The microservice is containerized using Docker and uses a PostgreSQL database. The service provides essential functionalities such as user registration, login, token verification, and profile retrieval.

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Project Setup](#project-setup)
- [API Endpoints](#api-endpoints)


## Features
- **User Registration**: Allows new users to create an account.
- **User Login**: Authenticates users and provides a JWT token.
- **Token Verification**: Validates the authenticity of the issued JWT tokens.
- **User Profile**: Retrieves the profile of an authenticated user.

## Technologies Used
- **Django**: Backend web framework.
- **Django Rest Framework**: Toolkit for building Web APIs.
- **Docker**: Containerization platform for packaging and deploying the application.
- **PostgreSQL**: Relational database management system.
- **Gunicorn**: WSGI HTTP server for serving the application.

## Project Setup
To run this microservice, follow these steps:

1. **Clone the repository**:


3. **Build and run the Docker containers**:

    ```bash
    docker-compose up --build
    ```

6. **Access the application**:

   The application will be running at `http://localhost:8000`.

## API Endpoints

### User Registration - POST REQUEST
- **URL**: `http://localhost:8000/api/v1/register/`
- **Method**: `POST`
- **Description**: Registers a new user.
  ```json
  {
    "first_name": "Demo",
    "last_name" : "User",
    "email" : "demouser@test.com",
    "password": "password"
  }

### User Login - POST REQUEST
- **URL**: `http://localhost:8000/api/v1/login/`
- **Method**: `POST`
- **Description**: Logs in a user and returns a JWT token.

```json
{
    "email" : "demouser@test.com",
    "password": "password"
}
```

### Token Verification - POST REQUEST
- **URL**: `http://localhost:8000/api/v1/token/verify/`
- **Method**: `POST`
- **Description**: Verifies the validity of the given JWT token.
```json
{
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI3NDA2NTY1LCJpYXQiOjE3MjczOTU3NjUsImp0aSI6IjFiMmZhNjA2N2UyOTQ3ZWNiM2VhYTNkOGU1YjQyYmIyIiwidXNlcl9pZCI6NX0.FnKIp4jvEaSCHGlCHleiFaNqnuxmvl0IXWjjghrmavU"
}
```

### Get User Profile - GET REQUEST
- **URL**: `http://localhost:8000/api/v1/users/`
- **Method**: `GET`
- **Description**: Retrieves the profile of the currently authenticated user.

