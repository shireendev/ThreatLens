from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.ioc import IOC
from app.models.user import User
from app.schemas.ioc import IOCCreate, IOCResponse
from app.routers.user import get_current_user

router = APIRouter()


@router.post("/iocs", response_model=IOCResponse)
def create_ioc(
    ioc: IOCCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    new_ioc = IOC(
        ioc_type=ioc.ioc_type,
        value=ioc.value,
        severity=ioc.severity,
        description=ioc.description,
        source=ioc.source
    )

    db.add(new_ioc)
    db.commit()
    db.refresh(new_ioc)

    return new_ioc


@router.get("/iocs", response_model=list[IOCResponse])
def get_iocs(
    severity: str | None = None,
    ioc_type: str | None = None,
    value: str | None = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    query = db.query(IOC)

    if severity:
        query = query.filter(IOC.severity == severity)

    if ioc_type:
        query = query.filter(IOC.ioc_type == ioc_type)

    if value:
        query = query.filter(IOC.value == value)

    return query.all()
