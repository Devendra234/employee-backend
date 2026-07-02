from fastapi import FastAPI
from app.database.database import Base, engine
from app.auth.security import hash_password

app = FastAPI(title="Employee Management API")

Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {"message": "Employee Management API Running"}

@app.get("/test")
def test():
    return {
        "password": hash_password("admin123")
        
    }