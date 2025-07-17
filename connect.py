from sqlalchemy import create_engine

# Replace with your actual info
url = "postgresql://postgres:bat1234@localhost:5432/medical_reports"

try:
    engine = create_engine(url)
    conn = engine.connect()
    print("✅ Connection successful!")
except Exception as e:
    print("❌ Connection failed:")
    print(e)
