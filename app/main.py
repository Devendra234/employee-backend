from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database.database import Base, engine
from app.routes.auth import router as auth_router
from app.routes.employee import router as employee_router

app = FastAPI(title="Employee Management API")

# ✅ CORS (Production + Local)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
          "https://employee-frontend-cyan-eta.vercel.app"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ⚠️ Creates tables (OK for project, not ideal for large production apps)
Base.metadata.create_all(bind=engine)

# Routes
app.include_router(auth_router)
app.include_router(employee_router)

@app.get("/")
def home():
    return {
        "message": "Employee Management API Running"
    }