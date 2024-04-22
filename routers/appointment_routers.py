from fastapi import APIRouter, Depends, HTTPException
from schema.appointment_schema import Appointment, Patient, Doctor, appointments,doctors, datetime
from services.appointment_service import AppointmentService, AppointmentCreate, AppointmentUpdate

appointment_router = APIRouter()

@appointment_router.get('/all')
def get_appointments():
    data = AppointmentService.get_all_appointments(appointments)
    return {"message": data}

@appointment_router.post('/create')
def create_appointment(payload:AppointmentCreate = Depends(AppointmentService.create_appointment)):
    app_id = len(appointments)
    docs_ids =  [docs for docs in doctors if docs.is_available]
    docs_ids[0].is_available=False
    data = AppointmentCreate(id=app_id, patient=payload.patient, doctor=docs_ids[0], date=payload.date)
    return {"success":True, "data": data}

@appointment_router.patch('/complete')
def complete_appointment_by_id(app_id:int = Depends(AppointmentService.update_appointment)):
    app_id = AppointmentService.update_appointment(app_id)
    for app in appointments:
        if app_id == app.id:
            if (app.status == "booked") | (app.status != "cancelled"):
                app.status = "completed"
                app.doctor.is_available=True
                return {"data": app}
            else:
                raise HTTPException(status_code=400, detail="Appointment has alreasdy been completed")
            

@appointment_router.patch('/cancel/')
def cancel_appointment_by_id(app_id:int = Depends(AppointmentService.update_appointment)):
    app_id = AppointmentService.update_appointment(app_id)
    for app in appointments:
        if app_id == app.id:
            if (app.status == "booked") | (app.status != "completed"):
                app.status = "cancelled"
                app.doctor.is_available=True
                return {"data": app}
            else:
                raise HTTPException(status_code=400, detail="Appointment has already been cancelled")