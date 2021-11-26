import os
from flask import Flask
from flask_cors import CORS, cross_origin
import json

app = Flask(__name__,
    static_url_path='/',
    static_folder='../static')

cors = CORS(app, resources={r"/*": {"origins": "*"}})

app.config.from_file('../config.json', json.load)

from . import api
from . import sock

sock.start_listen_process()
