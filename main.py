from fastapi import FastAPI

app = FastAPI(title="Alpha IB Project")

@app.get("/")
def read_root():
    return {"message": "Привет, Альфа!"}