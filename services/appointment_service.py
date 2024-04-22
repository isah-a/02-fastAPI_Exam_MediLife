from fastapi import HTTPException
from schema. appointment_schema import Appointment, AppointmentCreate, AppointmentUpdate, Patient, Doctor, appointments, patients, doctors
from datetime import datetime

class AppointmentService:
    @staticmethod
    def get_all_appointments(appointment_db):
        return appointment_db
    
    @staticmethod
    def create_appointment(pay:AppointmentCreate):
        pat = [p_ids for p_ids in patients if pay.patient.id == p_ids.id]
        if len(pat) != 0:
            docs_ids =  [docs for docs in doctors if docs.is_available]
            if len(docs_ids) !=0:
                return pay
            else:
                raise HTTPException(status_code=400, detail='No available doctors at the moment.')
        else:
            raise HTTPException(status_code=400, detail='Patient is not registered.')
        

    @staticmethod
    def update_appointment(id:int):
        app_ids = [app_id for app_id in appointments if id == app_id.id]
        return id
    

    # def create_appointment(pat_id:int, app_date:datetime = datetime(2023, 3, 1)):
    #     app_id = len(appointments)
    #     pat = [p_ids for p_ids in patients if pat_id == p_ids.id]
    #     if len(pat)  != 0:
    #         docs = [docs for docs in doctors if docs.is_available]
    #         app = AppointmentCreate(id=app_id, patient=pat[0], doctor=docs[0], date=app_date)

    #         return app
    #     else:
    
    #     # data = Appointment(id=app_id, **payload.model_dump())
    #         return "no available doctor"