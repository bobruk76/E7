import os
from flask import Flask

port = int(os.environ.get("PORT", 5000))
app = Flask(__name__)

from api import routes