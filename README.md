# AI-Powered Multi-Language Code Error Detection and Explanation System

An AI-powered web application that analyzes source code using Google's Gemini Large Language Model (LLM). The system detects programming errors, explains them in simple language, generates corrected code, recommends best coding practices, maintains analysis history, generates downloadable PDF reports, and provides administrative analytics through a secure Django web application.

---

# Features

- User Registration & Authentication
- AI-Based Source Code Analysis
- Multi-Language Support
- Error Detection
- Detailed Error Explanation
- Corrected Source Code Generation
- Coding Best Practices Recommendation
- Confidence Score
- Analysis History
- PDF Report Generation
- Dashboard Analytics
- Administration Module
- User Management
- Analysis Management
- System Analytics
- Docker Support
- Production Ready Configuration

---

# Supported Programming Languages

- Python
- Java
- C
- C++
- JavaScript
- Go

---

# Technology Stack

## Backend

- Python 3.12
- Django 5

## Frontend

- HTML5
- CSS3
- Bootstrap 5
- JavaScript

## Database

- SQLite

## AI

- Google Gemini API

## Authentication

- Django Authentication System

## PDF

- ReportLab

## Containerization

- Docker
- Docker Compose

## Version Control

- Git
- GitHub

---

# Project Structure

```
ai_code_analyzer/

├── apps/
│   ├── accounts/
│   ├── administration/
│   ├── code_analysis/
│   ├── dashboard/
│   ├── reports/
│   └── common/
│
├── config/
│
├── static/
├── media/
├── templates/
│
├── docs/
│
├── logs/
│
├── Dockerfile
├── docker-compose.yml
├── entrypoint.sh
├── requirements.txt
├── manage.py
└── README.md
```

---

# Architecture

```
User

↓

Browser

↓

Django Views

↓

Services

↓

Validators

↓

Gemini Service

↓

Google Gemini API

↓

JSON Parser

↓

Repositories

↓

SQLite Database
```

---

# Design Principles

This project follows:

- SOLID Principles
- DRY Principle
- KISS Principle
- Repository Pattern
- Service Layer Pattern
- DTO Pattern
- Clean Architecture

---

# Main Modules

## Accounts

- Registration
- Login
- Logout
- Profile

---

## Dashboard

- User Dashboard
- Statistics
- Charts

---

## Code Analysis

- Analyze Code
- AI Response
- JSON Parsing
- History

---

## Reports

- PDF Generation
- Download Reports

---

## Administration

- Dashboard
- User Management
- Analysis Management
- System Analytics

---

# Installation

## Clone Repository

```bash
git clone https://github.com/indra1805/mca-ai-code-analyzer.git

cd ai-code-analyzer
```

---

## Create Virtual Environment

Windows

```bash
python -m venv venv

venv\Scripts\activate
```

Linux

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## Install Requirements

```bash
pip install -r requirements.txt
```

---

## Create Environment Variables

Create

```
.env
```

Example

```env
DEBUG=True

SECRET_KEY=your-secret-key

ALLOWED_HOSTS=127.0.0.1,localhost

GEMINI_API_KEY=your-api-key

GEMINI_MODEL=gemini-2.5-flash
```

---

## Apply Migrations

```bash
python manage.py migrate
```

---

## Create Superuser

```bash
python manage.py createsuperuser
```

---

## Run Server

```bash
python manage.py runserver
```

Open

```
http://127.0.0.1:8000
```

---

# Docker

Build

```bash
docker compose build
```

Run

```bash
docker compose up
```

Stop

```bash
docker compose down
```

---

# Screens

- Login
- Registration
- Dashboard
- Analyze Code
- Analysis Result
- Analysis History
- PDF Report
- User Profile
- Admin Dashboard
- User Management
- Analysis Management
- System Analytics

---

# Security

- CSRF Protection
- Django Authentication
- Environment Variables
- Secure Password Hashing
- HTTPOnly Cookies
- XSS Protection
- Clickjacking Protection

---

# Future Enhancements

- More Programming Languages
- Syntax Highlighting
- AI Chat Assistant
- Code Complexity Analysis
- Code Quality Score
- Real-Time Analysis
- Email Reports
- Cloud Deployment
- PostgreSQL Support

---

# Author

**Indra K N**

Python Developer

MCA Final Year Project

AI-Powered Multi-Language Code Error Detection and Explanation System

---

# License

This project is developed for academic purposes as part of the Master of Computer Applications (MCA) curriculum.
