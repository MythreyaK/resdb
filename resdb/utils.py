import os
import subprocess as sp
from resdb import app
import functools

# def compile_resdb(replicas, clients):
#     sources = app.config["RESDB_SOURCE_PATH"]
#     output = sp.check_output([ f"{sources}/scripts/create_config.sh", f"{replicas}", f"{clients}" ]).decode("utf8")
#     print(output)

def in_dir(path):
    def dir_arg_wraper(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            pushd = os.getcwd()
            os.chdir(path)
            func(*args, **kwargs)
            os.chdir(pushd)
        return wrapper
    return dir_arg_wraper


@in_dir(app.config["RESDB_SOURCE_PATH"])
def deploy_config(replicas, clients):
    sources = app.config["RESDB_SOURCE_PATH"]
    output = sp.check_output([ f"{sources}/resilientDB-docker", f"--replicas={replicas}", f"--clients={clients}" ]).decode("utf8")
    return output
