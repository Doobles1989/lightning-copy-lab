from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/status")
def check_status():
    return JSONResponse(content={"status": "Lightning Copy Lab is online"})
