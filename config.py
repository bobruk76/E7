import os

class Config:
    # SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    # SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASK_APP = 'api/app.py'
    SECRET_KEY = os.urandom(32)
    PORT = 5000
