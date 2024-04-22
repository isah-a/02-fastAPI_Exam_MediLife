from fastapi import HTTPException
from schema.patient_schema import Patient, PatientCreate, PatientUpdate, patients

db = []
class PatientService:
    ######################### GET ALL PATIENTS #########################
    @staticmethod
    def get_all_patients(patient_db):
        return patient_db
    
    ######################### CREATE A PATIENT #########################
    @staticmethod
    def create_patient(payload:PatientCreate):
        p_id = len(patients)
        patients_db = Patient(id=p_id, **payload.model_dump())
        patients.append(patients_db)
        return patients
    
    ######################### GET SINGLE PATIENTS #########################
    @staticmethod
    def get_patient_by_id(id:int):
        for pat in patients:
            if pat.id == id: 
                return pat.model_dump() # I also noticed that this line still correctly returned the pydantic instance (as a dictionary) even without using model_dump(). 
        else:
            raise HTTPException(status_code=400, detail="id does not exist to query.")
            
    ######################### TOTAL UPDATE OF A SINGLE PATIENTS (PUT) #########################
    @staticmethod
    def update_patient_by_id(p_id:int, payload:PatientCreate):
        for pat in patients:
            if pat.id == p_id:
                patients[p_id] = Patient(id=p_id, **payload.model_dump())
                return patients[p_id]
        else:
            raise HTTPException(status_code=400, detail="id does not exist to update")
            
    ######################### PARTIAL UPDATE OF A SINGLE PATIENT (PATCH) #########################
    @staticmethod
    def patch_patient_by_id(payload:PatientUpdate):
        patient = payload.model_dump(exclude_unset=True)
        for pat in patients:
            if pat.id == payload.id:
                indx_model = patients[pat.id]
                print (f"index is: {indx_model}")
                new_dict = indx_model.model_copy(update=patient)
                return new_dict
        else:
            raise HTTPException(status_code=400, detail="id does not exist to update")
            
    ######################### DELETE A PATIENT #########################
    @staticmethod
    def delete_patient_by_id(id:int):
        for pat in patients:
            if pat.id == id:
                del patients[pat.id] 
                return patients
            else:
                raise HTTPException(status_code=400, detail='Patient does not exist.')