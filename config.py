import os

class Config:
    SECRET_KEY = os.urandom(32)
    PORT = os.getenv('PORT', 5000)
    DB_NAME = os.getenv('DB_NAME', 'e7')
