from sqlalchemy import Column, Integer, String, Text

from app.core.database import Base


class IOC(Base):
    __tablename__ = "iocs"

    id = Column(Integer, primary_key=True, index=True)

    ioc_type = Column(String, nullable=False)

    value = Column(String, unique=True, nullable=False)

    severity = Column(String, default="medium")

    description = Column(Text)

    source = Column(String)

    status = Column(String, default="active")
