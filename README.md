# Healthcare Django Project

This is a Healthcare Management System built with Django and Django REST Framework.

## Features
- User registration and login (JWT authentication)
- Patient and doctor management
- Patient-doctor mapping
- RESTful API endpoints

## Setup
1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Configure your `.env` file for secrets and database
4. Run migrations: `python manage.py migrate`
5. Start the server: `python manage.py runserver`

## API Endpoints
- `/api/auth/register/` - Register a new user
- `/api/auth/login/` - Login and get JWT token
- `/api/patients/` - List and create patients
- `/api/doctors/` - List and create doctors
- `/api/mappings/` - Manage patient-doctor mappings

## License
MIT
