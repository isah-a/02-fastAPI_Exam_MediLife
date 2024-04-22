from pydantic import BaseModel

class Patient(BaseModel):
    id: int
    name: str
    age: int
    sex: str
    weight: float
    height: int
    phone: str

class PatientCreate(BaseModel):
    name: str
    age: int
    sex: str
    weight: float
    height: int
    phone: str

class PatientUpdate(BaseModel):
    id: int| None = None
    name: str | None = None
    age: int | None = None
    sex: str | None = None
    weight: float| None = None
    height: int | None = None
    phone: str| None = None

patients: list[Patient]  = [
    Patient(id=0, name="Marcus", age=27, sex="Male", weight=45.2, height=183, phone="+447813"),
    Patient(id=1, name="Joe", age=30, sex="Male", weight=41.05, height=171, phone="+4479000")
]