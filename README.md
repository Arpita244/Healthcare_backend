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


## API Endpoints & Usage Examples

### 1. Authentication
- **POST `/api/auth/register/`**
	- Request body:
		```json
		{
			"username": "user1",
			"email": "user1@example.com",
			"password": "yourpassword"
		}
		```
- **POST `/api/auth/login/`**
	- Request body:
		```json
		{
			"username": "user1",
			"password": "yourpassword"
		}
		```
	- Response:
		```json
		{
			"refresh": "<refresh_token>",
			"access": "<access_token>"
		}
		```

### 2. Patient Management (Authenticated)
- **POST `/api/patients/`**
	- Request body:
		```json
		{
			"name": "John Doe",
			"age": 30,
			"gender": "Male",
			"medical_history": "Diabetes"
		}
		```
- **GET `/api/patients/`**
	- Returns all patients for the authenticated user.
- **GET `/api/patients/<id>/`**
	- Returns details for a specific patient.
- **PUT `/api/patients/<id>/`**
	- Update patient details (same fields as POST).
- **DELETE `/api/patients/<id>/`**
	- Deletes a patient record.

### 3. Doctor Management (Authenticated)
- **POST `/api/doctors/`**
	- Request body:
		```json
		{
			"name": "Dr. Smith",
			"specialization": "Cardiology",
			"contact_info": "smith@hospital.com"
		}
		```
- **GET `/api/doctors/`**
	- Returns all doctors.
- **GET `/api/doctors/<id>/`**
	- Returns details for a specific doctor.
- **PUT `/api/doctors/<id>/`**
	- Update doctor details (same fields as POST).
- **DELETE `/api/doctors/<id>/`**
	- Deletes a doctor record.

### 4. Patient-Doctor Mapping (Authenticated)
- **POST `/api/mappings/`**
	- Request body:
		```json
		{
			"patient": 1,
			"doctor": 2
		}
		```
- **GET `/api/mappings/`**
	- Returns all patient-doctor mappings.
- **GET `/api/mappings/<patient_id>/`**
	- Returns all mappings for a specific patient.
- **DELETE `/api/mappings/<id>/`**
	- Removes a doctor from a patient.

## License
MIT
