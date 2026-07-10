# ProtoStruc: Professional Engineering Design Platform

ProtoStruc is an enterprise-grade, AI-assisted product development ecosystem designed to streamline and automate hardware and software engineering methodologies. By leveraging cutting-edge multi-agent systems via LangGraph, ProtoStruc performs Functional Decomposition, Morphological Analysis, and Risk Mitigation through an intuitive engineering dashboard.

---

## 🌐 Live Application

- **Frontend:** https://http://16.16.242.152:3000
- **Backend API:** http://http://16.16.242.152:8000
---

# 🚀 Features

- AI-assisted engineering workflow automation
- Functional Decomposition
- Morphological Analysis
- Engineering Risk Mitigation
- Multi-agent orchestration using LangGraph
- Secure JWT Authentication
- Supabase integration
- Responsive Next.js dashboard
- Automated CI/CD deployment using Jenkins
- Dockerized production environment
- AWS EC2 deployment

---

# ⚡ Technology Stack

## Frontend

- Next.js (App Router)
- React
- Tailwind CSS
- shadcn/ui
- Lucide React
- Framer Motion

## Backend

- FastAPI
- Python
- LangGraph
- Groq API
- Pydantic
- Supabase (PostgreSQL)

## DevOps

- Docker
- Docker Compose
- Jenkins
- AWS EC2
- GitHub

---

# 📁 Repository Structure

```text
IP_Deployment/
│
├── frontend/
│   ├── src/
│   │   ├── app/
│   │   ├── components/
│   │   └── lib/
│   ├── Dockerfile
│   └── package.json
│
├── backend/
│   ├── app/
│   │   ├── ai/
│   │   ├── api/
│   │   ├── models/
│   │   └── main.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── docker-compose.prod.yml
├── Jenkinsfile
├── ARCHITECTURE.md
├── DEPLOYMENT.md
└── README.md
```

---

# 🛠 Local Development

## 1. Clone Repository

```bash
git clone https://github.com/kanigai2005/ProtoStruc.git

cd ProtoStruc
```

---

## 2. Backend Setup

```bash
cd backend

python -m venv venv

# Windows
venv\Scripts\activate

# Linux/macOS
source venv/bin/activate

pip install -r requirements.txt

uvicorn app.main:app --reload
```

Backend runs on

```
http://localhost:8000
```

Swagger UI

```
http://localhost:8000/docs
```

---

## 3. Frontend Setup

```bash
cd frontend

npm install

npm run dev
```

Frontend runs on

```
http://localhost:3000
```

---

# 🐳 Running with Docker

Build and start both frontend and backend containers:

```bash
docker compose -f docker-compose.yml up --build
```

Run in detached mode

```bash
docker compose -f docker-compose.yml up --build -d
```

Stop containers

```bash
docker compose -f docker-compose.yml down
```

---

# ☁️ Production Deployment

ProtoStruc is deployed on an AWS EC2 instance using Docker containers and an automated Jenkins CI/CD pipeline.

The deployment pipeline performs:

- Repository checkout
- Docker image build
- Container deployment
- Automatic application restart
- Removal of unused Docker images
- Continuous deployment on every push to the main branch


# 👨‍💻 Author

Developed as an AI-assisted engineering platform demonstrating modern software architecture, multi-agent AI orchestration, containerized deployment, and automated CI/CD practices.
