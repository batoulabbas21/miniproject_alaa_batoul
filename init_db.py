from backend.database import engine
from backend.model.report import Base

Base.metadata.create_all(bind=engine)
print("✅ Database tables created.")
