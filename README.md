# show_ticket_booking_django
"A Django-based Ticket Booking Management System with user authentication, show listings, seat booking, and a custom admin panel."

# 🎟️ Ticket Booking Management System

## 📖 Project Overview

This is a Django-based Ticket Booking Management System that allows users to register, view available shows/events, select seats, and confirm bookings. It includes user authentication, booking history, and a custom-built admin panel for managing shows and viewing all bookings. Session-based logic is used for managing bookings without relying on Django’s admin or form system.

---

## 🚀 Setup & Run Instructions

### 🔧 Prerequisites
- Python 3.9
- Docker & Docker Compose
- Git

### 🧪 Local Setup (without Docker)
```bash
git clone https://github.com/ARES2525/show_ticket_booking_django
cd ticket-booking-system
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### 🐳 Docker Setup
```bash
# Build containers
docker-compose build

# Run containers
docker-compose up
```

> Access the app at `http://localhost:8000`

---

## 🧰 Tech Stack Used

- **Backend**: Django (Class-Based Views only)
- **Frontend**: HTML, CSS (manually created forms, no Django forms)
- **Database**: MySQL
- **Containerization**: Docker, Docker Compose
- **CI/CD**: Jenkins

---

## ⚙️ Docker & Jenkins Usage

### 🐋 Docker
- The app is containerized using Docker.
- `docker-compose.yml` sets up the `web` (Django) and `db` (MySQL) services.
- Environment variables and ports are configured within `docker-compose.yml`.

### 🔁 Jenkins
- A `Jenkinsfile` is included to automate:
  - Docker image build
  - Running migrations
  - Deploying the container
- This can be integrated into a Jenkins pipeline by connecting the GitHub repo and configuring Jenkins to use the included `Jenkinsfile`.

---
