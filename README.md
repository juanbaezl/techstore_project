# TechStore Backend API

A professional, modular Django REST Framework project for managing a technology store. This project is fully containerized using Docker and follows a clean architecture pattern to ensure scalability and maintainability.

## 🚀 Key Features

- Modular Architecture: Separated logic for models, views, serializers, and filters.
- Dockerized Environment: Automated setup with Docker Compose, including a Python backend and a PostgreSQL database.
- Relational Database Design: Includes One-to-Many (Category-Product) and Many-to-Many (Order-Product) relationships.
- Automated Migrations: Custom entrypoint script that waits for the database to be ready before applying migrations.
- Environment Safety: Managed configurations using .env files for development and production.

## 🏗️ Project Structure

The project follows a modular directory structure to keep the code organized:

```
├── docker-compose.yml  # Docker orchestration
└── backend             # Backend service
    ├── api/            # Django Application
    │   ├── filters/    # View filters
    │   ├── models/     # Database models (modularized)
    │   ├── serializers/# Data serializers
    │   ├── views/      # API logic
    │   └── urls.py     # API routing
    ├── app/            # Django project core (settings/urls)
    ├── docker/         # Dockerfiles for dev/prod
    ├── .env.development# Environment variables
    └── requirements.txt# Python dependencies
```

## 🛠️ Tech StackFramework:

- Django & Django REST Framework.
- Database: PostgreSQL 16.
- Containerization: Docker & Docker Compose.
- Language: Python 3.11-slim.🚦

## Getting Started

**Prerequisites**

- Docker and Docker Compose installed.
- Git (optional for cloning).

**Installation & Setup**

1. Clone the repository:

```
git clone <your-repository-url>
cd techstore_project
```

2. Configure Environment Variables:Ensure your backend/.env.development file is set up with the correct database credentials:

```
DEBUG=1
DB_NAME=techstore
DB_USER=techstore
DB_PASSWORD=techstore
DB_HOST=db
DB_PORT=5432
```

3. Launch the Containers:

```
docker-compose up --build
```
