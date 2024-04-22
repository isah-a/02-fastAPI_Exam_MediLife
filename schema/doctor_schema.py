from pydantic import BaseModel

class Doctor(BaseModel):
    id: int 
    name: str 
    specialization: str 
    phone: str 
    is_available: bool = True 

class DoctorCreate(BaseModel):
    name: str 
    specialization: str 
    phone: str 
    is_available: bool = True

class DoctorUpdate(BaseModel):
    id: int | None = None
    name: str | None = None
    specialization: str | None = None
    phone: str | None = None
    is_available: bool = True 

doctors: list[Doctor]  = [
    Doctor(id= 0, name= "Ben", specialization= "Surgeon", phone= "+2348000" ), 
    Doctor(id= 1, name= "Yang", specialization= "Opthamologist", phone= "+2338099" , is_available=True ),
    Doctor(id= 2, name= "Burke", specialization= "Dentist", phone= "+20591" , is_available=False )
    ]