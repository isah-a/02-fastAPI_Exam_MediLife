from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

from routers.patient_routers import patient_router
from routers.doctor_routers import doctor_router
from routers.appointment_routers import appointment_router

app = FastAPI()
app.include_router(router=patient_router, prefix='/patient', tags=['Patient'])
app.include_router(router=doctor_router, prefix='/doctor', tags=['Doctor'])
app.include_router(router=appointment_router, prefix='/appointment', tags=['Appointment'])

# @app.get('/')
# def home():
#     return {"success": True}

# Custom metadata for the entire API
app_title = "Medical Appointment API (MediLife)"
app_description = "API for managing medical appointments between patients and doctors."
app_version = "1.0.0"

author = "Isah Abdul-Azeez"
author_github_profile = "https://github.com/isah-a"

# Generate custom OpenAPI documentation
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title=app_title,
        version=app_version,
        description=app_description,
        routes=app.routes
    )
    openapi_schema["info"]["x-your-name"] = author
    openapi_schema["info"]["x-github-repo"] = author_github_profile
    app.openapi_schema = openapi_schema
    return app.openapi_schema

# Assign custom OpenAPI generator to FastAPI app
app.openapi = custom_openapi