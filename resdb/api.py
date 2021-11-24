import docker
from resdb.docker import docker_client
from flask import app, request, jsonify
import subprocess as sp

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

@app.route('/replicas', ['GET'])
def get_replicas():
    all_containers = docker_client.containers.list()


@app.route('/alive', ['GET'])
def get_alive_status():
    ret = [ {
        "id": a.id,
        "type": "client" if 'c' in a.name else 'replica',
        "status": a.status,
        "name": a.name
    } for a in docker_client.containers.list() ]

    return jsonify(ret)

@app.route('/deploy', ['POST'])
def deploy_resdb():
    # Run the build-up script

@app.route('/stop', ['POST'])
def stop_resdb():
    # Run the take-down script

@app.route('/pause/<id>', ['PATCH'])
def pause_container(id):
    try:
        docker_client.containers.get(id).pause()
        return jsonify({
            "status": "Paused"
        })
    except docker.errors.APIError:
        return jsonify({
            "status": "error",
            "message": "Container already paused or stopped"
        })

@app.route('/resume/<id>', ['PATCH'])
def resume_container(id):
    try:
        docker_client.containers.get(id).unpause()
        return jsonify({
            "status": "running"
        })
    except docker.errors.APIError:
        return jsonify({
            "status": "error",
            "message": "Container already running or stopped"
        })
