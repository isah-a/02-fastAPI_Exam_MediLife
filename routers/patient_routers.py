from fastapi import APIRouter, Depends, HTTPException
from fastapi.encoders import jsonable_encoder

from schema.patient_schema import Patient, PatientCreate, PatientUpdate, patients
from services.patient_service import PatientService

patient_router = APIRouter()

######################### GET ALL PATIENTS #########################
@patient_router.get('/', status_code=200)
def get_all_patients():
    data = PatientService.get_all_patients(patients)
    return {"success":True, "data": data}

######################### CREATE PATIENTS #########################
@patient_router.post('/create', status_code=201)
def create_patient(payload: PatientCreate):
    data = PatientService.create_patient(payload)
    return {"success": True, "data": jsonable_encoder(data)}

######################### GET SINGLE PATIENTS #########################
@patient_router.get('/get_patient', status_code=200)
def get_patient_by_id(id:int):
    data = PatientService.get_patient_by_id(id)
    return {"success": True, "data": data}

######################### TOTAL UPDATE OF A SINGLE PATIENTS (PUT) #########################
@patient_router.put('/update', status_code=200)
def update_single_patient(id:int, pay:PatientCreate):
    data = PatientService.update_patient_by_id(id, pay)
    return {"success": True, "data": data}

######################### PARTIAL UPDATE OF A SINGLE PATIENT (PATCH) #########################
@patient_router.patch('/update', status_code=200)
def patch_single_patient(pay:PatientUpdate):
    data = PatientService.patch_patient_by_id(pay)
    return {"success": True, "data": data}


######################### DELETE A PATIENT #########################
@patient_router.delete('/', status_code=200)
def delete_patient_by_id(id:int):
    data = PatientService.delete_patient_by_id(id=id)
    return {"success":True, "data": data}