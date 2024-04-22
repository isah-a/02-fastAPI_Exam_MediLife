from fastapi import FastAPI
from pydantic import BaseModel

# "C:\Users\user\Desktop\Software-dev\AltSchool\secondSeemester\Assignments\A2\a2-env-fastapi\Scripts\activate"

from schema.patient_schema import Patient
from schema.doctor_schema import Doctor
from schema.appointment_schema import Appointment

from routers.patient_routers import patient_router
from routers.doctor_routers import doctor_router
from routers.appointment_routers import appointment_router

app = FastAPI()
app.include_router(router=patient_router, prefix='/patient', tags=['Patient'])
app.include_router(router=doctor_router, prefix='/doctor', tags=['Doctor'])
app.include_router(router=appointment_router, prefix='/appointment', tags=['Appointment'])

@app.get('/')
def home():
    return {"success": True}
