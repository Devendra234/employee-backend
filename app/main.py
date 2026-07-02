from fastapi import FastAPI

from app.database.database import Base, engine

app = FastAPI(title="Employee Management API")

Base.metadata.create_all(bind=engine)


@app.get("/")
def home():
    return {"message": "Employee Management API Running"}