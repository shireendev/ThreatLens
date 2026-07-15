from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.ioc import IOC
from app.schemas.ioc import IOCCreate, IOCResponse
from app.routers.user import get_current_user
from app.models.user import User

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
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return db.query(IOC).all()
