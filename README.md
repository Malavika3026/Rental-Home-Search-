## 🏠 Rental Home Search & Booking System

## Overview
Finding suitable rental accommodation can be time-consuming and inefficient without a centralized platform.
This project presents a web-based rental home search and booking system that enables users to explore properties, book rentals, and complete payments seamlessly.

The application is built using the Django framework, integrating backend logic, database management, and a responsive frontend.
It provides a complete workflow from property discovery to booking confirmation, along with an admin interface for managing listings.
---

## 🚀 Key Features

- User authentication (Registration, Login, Logout)
- Browse and explore rental properties
- View detailed property information (price, location, description)
- Booking system with check-in and check-out selection
- Automatic booking creation with database storage
- Payment workflow with booking status update (Pending → Paid)
- Admin panel to add and manage properties
- Dynamic display of booked and available properties

---

## 🧠 Model Details

- Framework: Django (MVT Architecture)
- Database: SQLite
- Task: Property Listing, Booking, and Payment Management
- Users: Regular Users & Admin (role-based access)

---
## 📊 Functional Workflow
User Login → Explore Properties → Book Property → Store Booking → Payment → Status Updated → Confirmation
The system ensures smooth data flow between frontend, backend, and database layers.

---

## 🏗️ System Architecture

The application follows a structured web architecture:
User Interface → Django Views → Django ORM → SQLite Database

- Frontend: HTML, CSS, Bootstrap
- Backend: Django
- Database: SQLite

---

## 🛠️ Tech Stack
- Python
- Django
- HTML, CSS
- Bootstrap
- SQLite
---

## 📂 Project Structure
myRent/
│
├── Home/
│   ├── models.py        → Database models (Property, Booking)
│   ├── views.py         → Application logic
│   ├── urls.py          → URL routing
│   ├── templates/       → HTML templates
│
├── db.sqlite3           → Database
├── manage.py
└── static/              → CSS, JS, Images
---

## ▶️ How to Run

### 1. Clone the Repository
git clone [https://github.com/Malavika3026/Rental-Home-Search.git]
cd Rental-Home-Search

### 2. Create Virtual Environment
python -m venv env
env\Scripts\activate   # Windows

### 3. Install Dependencies
pip install django

### 4. pip install django
python manage.py makemigrations
python manage.py migrate

### 5, Create SuperBase(Admin)
python manage.py createsuperuser

### 6. Run the Server
python manage.py runserver

### 7. python manage.py runserver
http://127.0.0.1:8000/
---

## 📌 Key Insights
- Django simplifies full-stack development using integrated components (ORM, routing, templates).
- Role-based access improves system security and usability.
- Relational databases efficiently manage user bookings and property data.
- Even simple payment simulations help demonstrate real-world application flow.

---

## 🔮 Future Improvements
- Integrate real payment gateways (Razorpay / Stripe)
- Add booking cancellation and refund system
- Implement availability calendar for properties
- Create user dashboard for booking history
- Enhance UI with modern frontend frameworks (React / Vue)

---

## 📎 Acknowledgment
This project was developed as part of academic learning in Web Development using Django, focusing on building real-world applications with complete user workflows including booking and payment systems.

---
