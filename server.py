#!/usr/bin/env python3

# source: https://towardsdatascience.com/a-python-api-for-background-requests-based-on-flask-and-multi-processing-187d0e3049c9
from flask import Flask, render_template, Response, request
from waitress import serve
from flask_cors import CORS


import json

from interface_json import PipelineDataContainer
from pipeline_state import PipelineState

DEBUG_MODE: bool = True
HOST_NUMBER: str = '0.0.0.0'
PORT_NUMBER: int = 5000

pdc = PipelineDataContainer()
pdc2 = PipelineDataContainer()
pdc.set_pipeline_name('first pipeline')
pdc2.set_pipeline_name('second pipeline')

pipeline_state: PipelineState = PipelineState()
pipeline_state.add_pipeline_container(pdc)
pipeline_state.add_pipeline_container(pdc2)


REST_GET: str = 'GET'
REST_POST: str = 'POST'

# Create a new Flask application
app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/', methods=[REST_GET])
def get_homepage():
    text = 'Hello World'
    return render_template('index.html', html_page_text=text)


@app.route('/jobs', methods=[REST_GET])
def get_jobs():
    jobs = {'job': [job._job_dict for job in pdc.get_jobs()]}
    return Response(json.dumps(jobs), mimetype='application/json')


@app.route('/job/requirement')
def get_req():
    job_requirement = json.dumps(pdc.get_jobs().pop().get_requirements())
    return Response(job_requirement, mimetype='application/json')


@app.route('/pipelines', methods=[REST_GET])
def get_pipelines():

    pipelines = {'pipelines': [
        pdc.get_outgoing_dict(), pdc2.get_outgoing_dict()]}

    return Response(json.dumps(pipelines), mimetype='application/json')


@app.route('/pipeline_names', methods=[REST_GET])
def get_pipeline_names():
    # return {'pipelines': [pdc.get_pipeline_name(), pdc2.get_pipeline_name()]}
    return {'pipelines': [pipeline.get_pipeline_name() for pipeline in pipeline_state.get_pipelines_()]}


@app.route('/pipelines/<uuid:pipeline_name>', methods=[REST_POST])
def get_pipeline(pipeline_name):
    body_pipeline_id = request.json.get('pipeline_name')
    

    pipeline = None


if __name__ == '__main__':

    print(f'Port: {PORT_NUMBER}')
    if DEBUG_MODE:
        # debug mode
        app.run(host=HOST_NUMBER, port=PORT_NUMBER, debug=True)

    else:
        # production mode
        serve(app, port=PORT_NUMBER)
