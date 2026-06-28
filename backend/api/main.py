from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .prediction_routes import router
from .resume_routes import router as resume_router
from .github_routes import router as github_router
from .skill_routes import router as skill_router
from .roadmap_routes import router as roadmap_router
from .interview_routes import router as interview_router
from .future_routes import router as future_router
from .digital_routes import router as digital_router
from .full_routes import router as full_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# routes
app.include_router(router)
app.include_router(resume_router)
app.include_router(github_router)
app.include_router(skill_router)
app.include_router(roadmap_router)
app.include_router(interview_router)
app.include_router(future_router)
app.include_router(digital_router)
app.include_router(full_router)

@app.get("/")
def home():
    return {"message": "Backend running"}