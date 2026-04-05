# SafeNest AI Policy Assistant

## Overview
SafeNest AI Policy Assistant is a Retrieval-Augmented Generation (RAG) system that enables users to query company policies using natural language.

The system retrieves relevant information from internal documents and generates accurate responses using an AI model.

---

## Features
- Natural language querying
- Context-aware responses
- Document-based answers
- Fast retrieval using vector database
- Production deployment with Docker

---

## Technologies Used
- Backend: Django (Python)
- Frontend: Bootstrap
- AI Model: Groq (LLM)
- Vector Database: Chroma
- Embeddings: HuggingFace
- Deployment: Docker, Nginx
- CI/CD: GitHub Actions

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/safenest-rag.git
cd safenest-rag
```

### 2. Create virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set environment variables
Create .env:

```bash
GROQ_API_KEY=your_key
```

### 5. Run migrations

```bash
python manage.py migrate
```

### 6. Ingest documents

```bash
python manage.py ingest_docs
```

### 7. Run server

```bash
python manage.py runserver
```

## B. Docker Deployment

```bash
docker compose -f docker-compose.prod.yml up -d --build
```