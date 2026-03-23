from cryptography.fernet import Fernet
import os


KEY = os.getenv("APP_SECRET_KEY", "uN_M4Y-security-key=")
cipher_suite = Fernet(KEY.encode())

def excrypt(plain_id: str) -> str:
    """Converts 'Asset_123' -> 'gAAAAABl...' (Safe for QR)"""
    return cipher_suite.encrypt(plain_id.encode()).decode()

def decrypt(encrypted_id: str) -> str:
    """Converts 'gAAAAABl...' -> 'Asset_123'"""
    return cipher_suite.decrypt(encrypted_id.encode()).decode()