from pydantic import BaseModel


class DashboardResponse(BaseModel):
    total_iocs: int
    active_iocs: int
    inactive_iocs: int
    critical: int
    high: int
    medium: int
    low: int
