from sqlalchemy import Column, Integer, String, Text
from app.database import Base

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)

class EncryptedData(Base):
    __tablename__ = 'encrypted_data'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    data = Column(Text)  # Encrypted data stored as text
