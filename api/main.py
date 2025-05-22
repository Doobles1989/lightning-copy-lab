from fastapi import FastAPI
from api.routes import generate

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Lightning Copy Lab is running"}

@app.get("/status")
def status():
    return {"status": "Lightning Copy Lab is online"}

app.include_router(generate.router, prefix="")
