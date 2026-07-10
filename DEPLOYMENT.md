# Deployment Guide

This document explains how ProtoStruc is deployed to production using Docker, Jenkins, and AWS EC2.

---

# Deployment Architecture

```
GitHub Repository
        │
        ▼
     Jenkins Server
        │
        ▼
SSH Connection
        │
        ▼
AWS EC2 Instance
        │
        ▼
Docker Compose
        │
 ┌───────────────┐
 │ Frontend      │
 │ Next.js       │
 └───────────────┘
        │
 ┌───────────────┐
 │ Backend       │
 │ FastAPI       │
 └───────────────┘
        │
        ▼
Supabase Database
```

---

# Prerequisites

Ensure the EC2 instance has the following installed:

- Docker
- Docker Compose
- Git
- Python (optional)
- Node.js (optional)

Verify installations:

```bash
docker --version

docker compose version

git --version
```

---

# EC2 Configuration

Update the Security Group inbound rules.

| Port | Protocol | Purpose |
|-------|----------|----------|
| 22 | TCP | SSH |
| 3000 | TCP | Frontend |
| 8000 | TCP | FastAPI API |

---

# Clone Repository

```bash
git clone https://github.com/kanigai2005/IP_deploy.git

cd ProtoStruc
```

---

# Configure Environment Variables

Backend:

```env
GROQ_API_KEY=

SUPABASE_URL=

SUPABASE_KEY=

JWT_SECRET=

DATABASE_URL=
```

Frontend:

```env
NEXT_PUBLIC_API_URL=http://http://16.16.242.152:8000
```

---

# Docker Deployment

Build containers

```bash
docker compose -f docker-compose.yml build
```

Start services

```bash
docker compose -f docker-compose.yml up -d
```

Stop services

```bash
docker compose -f docker-compose.yml down
```

Restart services

```bash
docker compose -f docker-compose.yml restart
```

---

# Verify Running Containers

```bash
docker ps
```

Expected containers:

- frontend
- backend

---

# Jenkins CI/CD Pipeline

The Jenkins pipeline automates deployment whenever new code is pushed to the main branch.

Pipeline stages:

## 1. Checkout Source

Retrieve the latest source code from GitHub.

---

## 2. SSH Authentication

Authenticate securely with the AWS EC2 instance using configured SSH credentials.

---

## 3. Synchronize Project

Copy the latest project files to the EC2 deployment directory.

Example:

```
/home/ubuntu/protostruc-app
```

---

## 4. Build Containers

Execute:

```bash
docker compose -f docker-compose.yml up --build -d
```

This rebuilds only the services that have changed.

---

## 5. Deploy Updated Containers

Existing containers are replaced with the updated application automatically.

---

## 6. Cleanup

Remove unused Docker resources.

```bash
docker image prune -f
```

This helps reduce disk usage on the EC2 instance.

---

# Application URLs

Frontend

```
http://16.16.242.152:3000
```

Backend

```
http://16.16.242.152:8000
```

Swagger Documentation

```
http://16.16.242.152:8000/docs
```

---

# Monitoring

View running containers

```bash
docker ps
```

View logs

Backend

```bash
docker logs backend
```

Frontend

```bash
docker logs frontend
```

Follow logs

```bash
docker logs -f backend
```

---

# Updating the Application

Deployment is fully automated.

Developer workflow:

```text
Code Changes
      │
      ▼
Git Commit
      │
      ▼
Git Push
      │
      ▼
Jenkins Trigger
      │
      ▼
Docker Build
      │
      ▼
AWS EC2 Deployment
```

No manual deployment steps are required after pushing to the configured branch.

---

# Troubleshooting

## Container failed to start

Check logs:

```bash
docker logs <container_name>
```

---

## Restart all services

```bash
docker compose -f docker-compose.yml down

docker compose -f docker-compose.yml up --build -d
```

---

## Check Docker status

```bash
docker ps -a
```

---

## Remove unused Docker resources

```bash
docker system prune -f
```

---

# Deployment Summary

Production environment includes:

- Docker containerization
- Docker Compose orchestration
- Jenkins automated CI/CD
- AWS EC2 hosting
- FastAPI backend
- Next.js frontend
- LangGraph multi-agent orchestration
- Supabase PostgreSQL
- Groq LLM integration

This deployment architecture provides a scalable, reproducible, and production-ready workflow for continuous delivery of ProtoStruc.
