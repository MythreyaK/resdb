import sqlite3

import click, docker
from flask import current_app, g
from flask.cli import with_appcontext

docker_client = None
if docker_client is None:
    docker_client = docker.from_env()

def get_docker_client():
    if 'docker_client' not in g:
        g.docker = docker.from_env()
    return g.docker

def close_docker_client():
    dc = g.get('docker_client', None)

    if dc is not None:
        g.docker.close()


def init_app(app):
    app.teardown_appcontext(close_docker_client)
