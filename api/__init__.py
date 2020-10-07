import os
from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)



port = int(os.environ.get("PORT", 5000))

app = Flask(__name__)
app.config.from_object(Config)
# app.config['SECRET_KEY'] = SECRET_KEY

from api import routes