import docker
from flask import request, jsonify
import subprocess as sp

from resdb.docker import docker_client
from resdb import app
from resdb.utils import deploy_config


def get_docker_compose_template(clients=1, replicas=4):
    template = \
"""{0}{1}:
    image: resilientdb/res-machine
    container_name: {0}{1}
    volumes:
        - ./:/home/expo/resilientdb
    restart: always
"""
    ret = ""
    for r in range(replicas + 1):
        ret += template.format('c', r)

    for c in range(clients + 1):
        ret += template.format('c', c)

    return ret


@app.route('/hello')
def hello():
    return 'Hello, World!'


# @app.route('/replicas')
# def get_replicas():
#     docker_client.containers.list()


@app.route('/alive', methods=['GET'])
def get_alive_status():
    ret = [ {
        "id": a.id,
        "short-id": a.short_id,
        "type": "client" if 'c' in a.name else 'replica',
        "status": a.status,
        "name": a.name
    } for a in docker_client.containers.list() ]

    return jsonify(ret)


@app.route('/deploy', methods=['POST'])
def deploy_resdb():

    def check_post(data):
        errors = []
        if "replicas" not in data:
            errors.append("Number of replicas not specified")
        if "clients" not in data:
            errors.append("Number of clients not specified")

        if len(errors) == 0:
            return True, errors
        else:
            return False, errors

    post_data = request.json
    res, errors = check_post(post_data)

    if res:
        output = deploy_config(post_data["replicas"], post_data["clients"])
        return jsonify(status = "ok", data = output)
    else:
        return jsonify(errors = errors), 400

    deploy_config()
    # run the teardown, then the build script


# @app.route('/stop', ['POST'])
# def stop_resdb():
#     pass
#     # Run the take-down script


@app.route('/pause/<id>',  methods=['PATCH'])
def pause_container(id):
    try:
        docker_client.containers.get(id).pause()
        return jsonify({
            "status": "paused"
        })
    except docker.errors.APIError:
        return jsonify({
            "status": "error",
            "message": "Container already paused or stopped"
        }), 400


@app.route('/resume/<id>',  methods=['PATCH'])
def resume_container(id):
    try:
        docker_client.containers.get(id).unpause()
        return jsonify(status="running")
    except docker.errors.APIError:
        return jsonify(
            status = "error",
            message = "Container already running or stopped"
        ), 400
