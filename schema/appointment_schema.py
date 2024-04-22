
from pydantic import BaseModel
from datetime import datetime
from .patient_schema import Patient, patients
from .doctor_schema import Doctor, doctors

class Appointment(BaseModel):
    id: int 
    patient: Patient
    doctor: Doctor
    date: datetime = datetime(2023, 3, 1)
    status: str = "booked"
    

class AppointmentCreate(BaseModel):
    patient: Patient
    doctor: Doctor | None = None
    date: datetime = datetime(2023, 3, 1)
    status: str = "booked"
    
class AppointmentUpdate(BaseModel):
    id: int | None = None
    patient: Patient | None = None
    doctor: Doctor | None = None
    date: datetime | None = None
    status: str = "booked"


appointments: list[Appointment] = [
    Appointment(id=0, patient=patients[0], doctor=doctors[0], date=datetime(2024, 2, 15)),
    Appointment(id=1, patient=patients[1], doctor=doctors[1], date=datetime(2024, 4, 29))
] 

