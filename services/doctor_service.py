from schema.doctor_schema import Doctor, DoctorCreate, DoctorUpdate, doctors

# db = {}
class DoctorService:
    @staticmethod
    def get_all_doctors(doctor_db):
        return doctor_db
    
    @staticmethod
    def get_available_doctors(doctor_db):
        return [ val for val in doctor_db if val.is_available]
    

    ######################### CREATE A DOCTOR #########################
    @staticmethod
    def create_doctor(payload:DoctorCreate):
        doc_id = len(doctors)
        doctors_db = Doctor(id=doc_id, **payload.model_dump())
        doctors.append(doctors_db)
        return doctors
    
    ######################### GET SPECIFIC DOCTOR BY ID #########################
    @staticmethod
    def get_doctor_by_id(id:int):
        for doc in doctors:
            if doc.id == id: 
                return doc.model_dump() # I also noticed that this line still correctly returned the pydantic instance (as a dictionary) even without using model_dump(). 
        else:
            return "does not exist"
            
    ######################### TOTAL UPDATE ALL INFO FOR A SINGLE DOCTOR (PUT) #########################
    @staticmethod
    def update_doctor_by_id(doc_id:int, payload:DoctorCreate):
        for doc in doctors:
            if doc.id == doc_id:
                doctors[doc_id] = Doctor(id=doc_id, **payload.model_dump())
                return doctors[doc_id]
        else:
            return "id does not exist to update"
            
    ######################### PARTIAL UPDATE OF A SINGLE DOCTOR (PATCH) #########################
    @staticmethod
    def patch_doctor_by_id(payload:DoctorUpdate):
        doctor = payload.model_dump(exclude_unset=True)
        for doc in doctors:
            if doc.id == payload.id:
                indx_model = doctors[doc.id]
                new_dict = indx_model.model_copy(update=doctor)
                return new_dict
        else:
            return "id does not exist to update"
            
    ######################### DELETE A DOCTOR #########################
    @staticmethod
    def delete_doctor_by_id(id:int):
        for doc in doctors:
            if doc.id == id:
                del doctors[doc.id] 
                return doctors
            else:
                return "id does not exist"