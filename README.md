# Secure Data Analysis Pipeline (SDAP)

## Overview

The **Secure Data Analysis Pipeline (SDAP)** is a backend system for securely ingesting, encrypting, storing, and analyzing data with end-to-end encryption. It is designed for privacy-sensitive environments where data confidentiality is critical, and it features encryption, authentication, and secure storage.

## Features

- End-to-end encryption for data at rest and in transit.
- User authentication using JSON Web Tokens (JWT).
- Secure data storage using PostgreSQL or SQLite for development.
- Role-based access control (RBAC) (hope I can finish it).
- Anonymization and data analysis (coming soon hopefully).

## Requirements

- Python 3.10 or higher
- PostgreSQL (for production) or SQLite (for development)
- FastAPI, SQLAlchemy, and other dependencies (listed below)

## Installation


   ```bash
   git clone https://github.com/Notle-eltoN/Secure-Data-Analysis-Pipeline-SDAP-.git

   pip install -r requirements.txt //Install the required dependencies

   cd Secure-Data-Analysis-Pipeline-SDAP-
   
   //Set up the database
   psql -U postgres
   CREATE DATABASE sdap_db;
   //For PostgreSQL, ensure the database is running on localhost:5432

   //Update the database URL in app/database.py
   SQLALCHEMY_DATABASE_URL = "postgresql://username:password@localhost:5432/sdap_db"
   
   //Run the FastAPI server
   uvicorn app.main:app --reload

   Access the API docs at http://127.0.0.1:8000/docs


