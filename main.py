from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os
from services.sms import SMSService
from schemas import SMSRequestSchema, SMSResponseSchema

app = FastAPI(
    title="Emilios SMS Service",
    description="SMS Sending Service",
    version="0.1.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[""],
    allow_credentials=True,
    allow_methods=[""],
    allow_headers=["*"],
)
app.mount("/assets", StaticFiles(directory="interface/assets"), name="assets")
app.mount("/interfave", StaticFiles(directory="interface"), name="interface")
sms_service = SMSService()
@app.post("/send-sms", response_model=SMSResponseSchema)
async def send_sms(request: SMSRequestSchema):
    try:
        result = sms_service.send_sms(
            phone_number=request.phone_number,
            attempts=request.attempts,
            offline=request.offline
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
@app.get("/health")
async def health_check():
    return {"status": "healthy"}
@app.get("/")
async def serve_index():
    return FileResponse('interface/index.html')