from cryptography.fernet import Fernet
from jose import JWTError, jwt
from passlib.context import CryptContext

SECRET_KEY = "supersecretkey"  # Replace with environment variable in production
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
fernet = Fernet(Fernet.generate_key())  # Replace with a securely stored key

def get_password_hash(password):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def encrypt_data(data):
    return fernet.encrypt(data.encode()).decode()

def decrypt_data(encrypted_data):
    return fernet.decrypt(encrypted_data.encode()).decode()

def create_access_token(data: dict):
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
