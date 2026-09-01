from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import csv, io, uuid, hashlib
import utils
from database import SessionLocal
from models import Employee

app = FastAPI(title="Alpha IB Project")

@app.get("/")
def read_root():
    return {"message": "Привет, Альфа!"}

@app.post("/employees/upload")
async def upload_employees(file: UploadFile = File(...)):
    content = await file.read()
    text = content.decode("utf-8")
    reader = csv.reader(io.StringIO(text))
    emails = []
    for row in reader:
        if row:
            emails.append(row[0])
    return {"emails": emails}   