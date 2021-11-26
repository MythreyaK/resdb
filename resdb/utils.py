import os
import subprocess as sp
from resdb import app
import functools

# def compile_resdb(replicas, clients):
#     sources = app.config["RESDB_SOURCE_PATH"]
#     output = sp.check_output([ f"{sources}/scripts/create_config.sh", f"{replicas}", f"{clients}" ]).decode("utf8")
#     print(output)

def in_dir(path):
    """
    Wrapper so that the function cd's to the dir before executing
    Ideal whe calling os-scripts
    """
    def dir_arg_wraper(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            pushd = os.getcwd()
            os.chdir(path)
            ret = func(*args, **kwargs)
            os.chdir(pushd)
            return ret
        return wrapper
    return dir_arg_wraper


def deploy_config(replicas, clients):

    # https://stackoverflow.com/questions/18421757/live-output-from-subprocess-command
    output = sp.Popen(
        [ "./resilientDB-docker", f"--replicas={replicas}", f"--clients={clients}" ],
        cwd = app.config["RESDB_SOURCE_PATH"],
        stderr = sp.STDOUT, # redirect to stdout
        stdout = sp.PIPE,   # Pipe this, can livestream
    )

    for line in iter(output.stdout.readline, b''):
        # sys.stdout.write(line.decode("utf8"))
        yield line.decode("utf8")
