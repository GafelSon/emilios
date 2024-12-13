from pydantic import BaseModel, Field, constr

class SMSRequestSchema(BaseModel):
    phone_number: constr(pattern=r'^\d{10}$') = Field(
        ...,
        description="Phone number (10 digits)"
    )
    attempts: int = Field(default=20, ge=1, le=50)
    offline: bool = Field(default=True)

class SMSResponseSchema(BaseModel):
    success: bool
    message: str
    details: list[dict] = []