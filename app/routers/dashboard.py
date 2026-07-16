from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.ioc import IOC
from app.models.user import User
from app.routers.user import get_current_user
from app.schemas.dashboard import DashboardResponse

router = APIRouter()


@router.get("/dashboard", response_model=DashboardResponse)
def get_dashboard(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    total_iocs = db.query(IOC).count()

    active_iocs = db.query(IOC).filter(
        IOC.status == "active"
    ).count()

    inactive_iocs = db.query(IOC).filter(
        IOC.status == "inactive"
    ).count()

    critical = db.query(IOC).filter(
        IOC.severity == "critical"
    ).count()

    high = db.query(IOC).filter(
        IOC.severity == "high"
    ).count()

    medium = db.query(IOC).filter(
        IOC.severity == "medium"
    ).count()

    low = db.query(IOC).filter(
        IOC.severity == "low"
    ).count()

    return {
        "total_iocs": total_iocs,
        "active_iocs": active_iocs,
        "inactive_iocs": inactive_iocs,
        "critical": critical,
        "high": high,
        "medium": medium,
        "low": low
    }
