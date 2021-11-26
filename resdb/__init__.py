import os
from flask import Flask
import json

app = Flask(__name__,
    static_url_path='/',
    static_folder='../static')

app.config.from_file('../config.json', json.load)

from . import api
from . import sock

sock.start_listen_process()
