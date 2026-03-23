import firebase_admin
from firebase_admin import credentials, firestore
from config.config import setting

cred = credentials.Certificate(setting.firebase_db_url)
default_app = firebase_admin.initialize_app(cred)

db = firestore.client()