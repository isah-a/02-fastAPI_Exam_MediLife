from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder

from schema.doctor_schema import DoctorCreate, Doctor, DoctorUpdate, doctors
from services.doctor_service import DoctorService

doctor_router = APIRouter()

######################### GET ALL DOCTORS #########################
@doctor_router.get('/', status_code=200)
def get_all_doctors():
    data = DoctorService.get_all_doctors(doctors)
    return {"success": True, "data": data}


######################### GET ALL AVAILABLE DOCTORS #########################
@doctor_router.get('/avaliable', status_code=200)
def get_available_docs():
    data = DoctorService.get_available_doctors(doctors)
    return {"data": data}


######################### CREATE DOCTORS #########################
@doctor_router.post('/create', status_code=201)
def create_doctor(payload: DoctorCreate):
    data = DoctorService.create_doctor(payload)
    return {"success": True, "data": jsonable_encoder(data)}

######################### GET SINGLE DOCTORS #########################
@doctor_router.get('/get_doctor/{id}', status_code=200)
def get_doctor_by_id(id:int):
    data = DoctorService.get_doctor_by_id(id)
    return {"success": True, "data": data}

######################### TOTAL UPDATE OF A SINGLE PATIENTS (PUT) #########################
@doctor_router.put('/update/{id}', status_code=200)
def update_single_doctor(id:int, pay:DoctorCreate):
    data = DoctorService.update_doctor_by_id(id, pay)
    return {"success": True, "data": data}

######################### PARTIAL UPDATE OF A SINGLE PATIENT (PATCH) #########################
@doctor_router.patch('/update/', status_code=200)
def patch_single_doctor(pay:DoctorUpdate):
    data = DoctorService.patch_doctor_by_id(pay)
    return {"success": True, "data": data}


######################### DELETE A PATIENT #########################
@doctor_router.delete('/{id}', status_code=200)
def delete_doctor_by_id(id:int):
    data = DoctorService.delete_doctor_by_id(id=id)
    return {"success":True, "data": data}