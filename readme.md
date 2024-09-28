# Tradie Services Microservice

This is a tradie services microservice developed using Django and Django Rest Framework. The microservice is containerized using Docker and uses a PostgreSQL database. The microservice provides functionality for creating, viewing, updating, and deleting a list of services. Authenticated users can create a service list that they want to provide, view all the services on the website, edit their own service, and delete their own service.

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Project Setup](#project-setup)
- [API Endpoints](#api-endpoints)

## Features
- **Create a Service**: Authenticated users can add new services they want to provide.
- **View Services**: Allows anyone to view the list of available services.
- **Update Service**: Authenticated users can update their own service information.
- **Delete Service**: Authenticated users can delete their own service.

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
    ```

6. **Access the application**:

   The application will be running at `http://localhost:8001`.

## API Endpoints

### Create a Service
- **URL**: `http://localhost:8001/api/v1/services/`
- **Method**: `POST`
- **Description**: Creates a new service.
- **Request Body**:
  ```json
  {
    "service_name": "EL",
    "email": "demouser@test.com",
    "phone_number": "0567891234",
    "service_cost": "700.00",
    "description": "I am available for all kinds of Electricity services.",
    "ABN": "JNC45789"
  }

### View All Services
- **URL**: `http://localhost:8001/api/v1/services/`
- **Method**: `GET`
- **Description**: Retrieves a list of all available services.

### Delete a Service
- **URL**: `http://localhost:8001/api/v1/services/:id/`
- **Method**: `DELETE`
- **Description**: Deletes a service by its ID. Only the service owner can delete it.

### Update a Service
- **URL**: `http://localhost:8001/api/v1/services/:id/`
- **Method**: `PUT`
- **Description**: Updates the details of a service by its ID. Only the service owner can update it.

```json
{
    "service_name": "EL",
    "email": "demouser@test.com",
    "phone_number": "124561234",
    "service_cost": "500.00",
    "description": "This is changed with put method. THe price is changed."
}

```
