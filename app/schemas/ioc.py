from pydantic import BaseModel


class IOCCreate(BaseModel):
    ioc_type: str
    value: str
    severity: str
    description: str
    source: str


class IOCResponse(BaseModel):
    id: int
    ioc_type: str
    value: str
    severity: str
    description: str
    source: str
    status: str

    class Config:
        from_attributes = True
