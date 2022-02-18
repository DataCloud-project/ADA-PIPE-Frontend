#!/usr/bin/env python3

# source: https://towardsdatascience.com/a-python-api-for-background-requests-based-on-flask-and-multi-processing-187d0e3049c9
from cgitb import html
from pickle import GET
from turtle import pd
from flask import Flask, render_template, Response
from waitress import serve
from flask_cors import CORS

import json

from interface_json import PipelineDataContainer

DEBUG_MODE: bool = True
PORT_NUMBER: int = 5000

pdc = PipelineDataContainer()
pdc2 = PipelineDataContainer()
pdc.set_pipeline_name('first pipeline')
pdc2.set_pipeline_name('second pipeline')


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


@app.route('/pipelines', methods=[REST_GET])
def get_pipelines():

    pipelines = {'pipelines': [
        pdc.get_json_dict(), pdc2.get_json_dict()]}

    return Response(json.dumps(pipelines), mimetype='application/json')


@app.route('/pipeline_names', methods=[REST_GET])
def get_pipeline_names():
    return {'pipelines': [pdc.get_pipeline_name(), pdc2.get_pipeline_name()]}


if __name__ == '__main__':

    print(f'Port: {PORT_NUMBER}')
    if DEBUG_MODE:
        # debug mode
        app.run(port=PORT_NUMBER, debug=True)

    else:
        # production mode
        serve(app, port=PORT_NUMBER)
