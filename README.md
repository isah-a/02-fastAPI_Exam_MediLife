# Medical Appointment API (MediLife)

## Description
Medical Appointment API is a FastAPI-based application designed to facilitate appointment bookings between patients and doctors. It allows patients to create appointments with available doctors, manage their own information, and cancel appointments if necessary. Doctors can manage their availability status and view their scheduled appointments.

## Features
- CRUD operations for Patients
- CRUD operations for Doctors
- Appointment creation, completion, and cancellation
- Set availability status for Doctors

## Installation
1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/your-repo.git
    ```
2. **Navigate to the project directory:**
    ```bash
    cd your-repo
    ```
3. **Create and activate a virtual environment (optional but recommended):**
    ```bash
    python -m venv env
    source env/bin/activate  # For Linux/Mac
    .\env\Scripts\activate   # For Windows
    ```
4. **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage
1. **Run the FastAPI server:**
    ```bash
    uvicorn main:app --reload
    ```
2. **Access the Swagger documentation at** `http://127.0.0.1:8000/docs` **in your web browser.**
3. **Use the API endpoints to perform CRUD operations on Patients, Doctors, and Appointments.**

## API Endpoints
- **Patients**: CRUD operations for patients
  - GET `/patient/`: Get all patients
  - POST `/patient/create`: Create a new patient
  - GET `/patient/{id}`: Get patient by ID
  - PUT `/patient/{id}`: Update patient by ID
  - PATCH `/patient/{id}`: Partial update of patient by ID
  - DELETE `/patient/{id}`: Delete patient by ID

- **Doctors**: CRUD operations for doctors
  - GET `/doctor/`: Get all doctors
  - POST `/doctor/create`: Create a new doctor
  - GET `/doctor/{id}`: Get doctor by ID
  - PUT `/doctor/{id}`: Update doctor by ID
  - PATCH `/doctor/{id}`: Partial update of doctor by ID
  - DELETE `/doctor/{id}`: Delete doctor by ID

- **Appointments**: Operations related to appointments
  - GET `/appointment/all`: Get all appointments
  - POST `/appointment/create`: Create a new appointment
  - PATCH `/appointment/complete/{id}`: Complete appointment by ID
  - PATCH `/appointment/cancel/{id}`: Cancel appointment by ID

## Contributing
Contributions are welcome! If you find any bugs or have suggestions for improvement, please open an issue or submit a pull request.

## License
This project is licensed under the [MIT License](LICENSE).

## Author
- Isah Abdul-Azeez
  - GitHub: [isah-a](https://github.com/isah-a)
