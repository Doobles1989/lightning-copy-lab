from fastapi import FastAPI
from api.routes.generate import router as generate_router

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Lightning Copy Lab is running"}

@app.get("/status")
def check_status():
    return {"status": "Lightning Copy Lab is online"}

# This line is required!
app.include_router(generate_router)
