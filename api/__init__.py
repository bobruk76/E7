import os
from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

redis_host = str(os.environ.get("REDIS_HOST", "localhost"))
redis_port = int(os.environ.get("REDIS_PORT", 6379))

app = Flask(__name__)
app.config.from_object(Config)
# app.config['SECRET_KEY'] = SECRET_KEY

from api import routes