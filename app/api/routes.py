from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas, security
from app.database import get_db

router = APIRouter()

@router.post("/users/", response_model=schemas.UserCreate)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    hashed_password = security.get_password_hash(user.password)
    db_user = models.User(username=user.username, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.post("/token", response_model=schemas.Token)
def login_for_access_token(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.username == user.username).first()
    if not db_user or not security.verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    access_token = security.create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/encrypt_data/")
def encrypt_and_store_data(data: schemas.DataCreate, db: Session = Depends(get_db)):
    encrypted_data = security.encrypt_data(data.data)
    db_data = models.EncryptedData(user_id=1, data=encrypted_data)  # replace 1 with actual user_id
    db.add(db_data)
    db.commit()
    return {"encrypted_data": encrypted_data}

@router.get("/decrypt_data/{data_id}")
def decrypt_stored_data(data_id: int, db: Session = Depends(get_db)):
    db_data = db.query(models.EncryptedData).filter(models.EncryptedData.id == data_id).first()
    if not db_data:
        raise HTTPException(status_code=404, detail="Data not found")
    decrypted_data = security.decrypt_data(db_data.data)
    return {"decrypted_data": decrypted_data}
