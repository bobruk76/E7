import os
from flask import Flask
import os
SECRET_KEY = os.urandom(32)


port = int(os.environ.get("PORT", 5000))
app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

from api import routes