from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime, Boolean, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from config import DATABASE_URL

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    telegram_id = Column(Integer, unique=True, nullable=False)
    username = Column(String(100))
    first_name = Column(String(100))
    last_name = Column(String(100))
    is_premium = Column(Boolean, default=False)
    total_requests = Column(Integer, default=0)
    daily_requests = Column(Integer, default=0)
    tokens_used = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)
    last_active = Column(DateTime, default=datetime.utcnow)

class CodeHistory(Base):
    __tablename__ = 'code_history'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    prompt = Column(Text, nullable=False)
    response = Column(Text, nullable=False)
    language = Column(String(50))
    tokens_used = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)

# إنشاء قاعدة البيانات
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)
SessionLocal = sessionmaker(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        return db
    finally:
        db.close()
