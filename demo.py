from interface_json import PipelineDataContainer
from flask import Flask, render_template, Response
import os
import json
# Create a new Flask application
app = Flask(__name__)


FILE_PATH = 'D:\\00Research\\matching\\scheduler\\Demo\\encode_20000.json'

pdc = PipelineDataContainer()


@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template("./index.html")


'''@app.route('/')
def example():
    command = str.encode(os.popen("C:/Users/narmehran/AppData/Local/Programs/Python/Python39/python.exe "+"D:\\00Research\\matching\\scheduler\\Demo\\scheduling.py "+"[encode_20000,frame_20000,hightrain,inference,package]"+" [] "+" [vm-bg-small,vm-vie-med,vm-vie-lg,egs,lenovo,jetson,rpi4,rpi3]").read())
    with open('D:\\00Research\\matching\\scheduler\\Demo\\encode_20000.json', 'r') as openfile:
        json_object = json.load(openfile)
        openfile.close
    return json_object'''


@app.route('/time')
def get_time():
    estimated_time = json.dumps(pdc.get_estimated_time())
    return Response(estimated_time, mimetype='application/json')


@app.route('/job/requirement')
def get_req():
    job_requirement = json.dumps(pdc.get_steps().pop().get_requirements())
    return Response(job_requirement, mimetype='application/json')


@app.route('/job/resource')
def get_res():
    job_resource = json.dumps(pdc.get_steps().pop().get_resource())
    return Response(job_resource, mimetype='application/json')


if __name__ == '__main__':
    app.run(debug=True)
