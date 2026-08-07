# AI Code Analyzer Deployment Guide

## Prerequisites

- Python 3.12
- pip
- Git
- Docker Desktop (optional)

---

## Clone Repository

```bash
git clone <repository-url>

cd ai_code_analyzer
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

Linux

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Create Environment File

Copy

```
.env.example
```

to

```
.env
```

Fill in:

- SECRET_KEY
- GEMINI_API_KEY

---

## Apply Migrations

```bash
python manage.py migrate
```

---

## Collect Static Files

```bash
python manage.py collectstatic
```

---

## Run Server

```bash
python manage.py runserver
```

Open

http://127.0.0.1:8000

---

# Docker Deployment

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