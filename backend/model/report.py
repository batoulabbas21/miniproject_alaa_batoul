from sqlalchemy import Column, Integer, String, Text
from backend.database import Base

class Report(Base):
    __tablename__ = "reports"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, nullable=False)  

    summary = Column(Text)
    risks = Column(Text)
