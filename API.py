from flask import request
import os
import json
from flask import Flask
from subprocess import Popen, PIPE

os.path.dirname(os.path.realpath(__file__))
app = Flask(__name__)


@app.route('/api/rpc/', methods=['POST'])
def rpc():
    request_body = [elem[0] for elem in request.form.items()][0]
    request_json = json.loads(request_body)

    method = request_json.get("method")

    if method == "handle_folder_read":
        path = request_json.get("folder")

        command_output = folder_read(path)

        return json.dumps({'output': command_output})


def folder_read(path):
    if os.name == 'nt':
        command = ['cmd', '/c', 'dir']
    else:
        command = ['la', '-al']

    process = Popen(command, cwd=path, stdout=PIPE, stderr=PIPE)
    stdout, stderr = process.communicate()

    if process.returncode != 0:
        raise RuntimeError(f"Folder '{path}' read failed with cmd '{command}': STDOUT: {stdout} STDERR: {stderr}")

    return stdout.decode("ascii")
