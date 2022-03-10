from itsdangerous import json
from flask_restful import Resource
from pipeline_state import PipelineState
from flask import Response, request, abort, jsonify
import json

from interface_json import PipelineDataContainer

pipeline_state: PipelineState = PipelineState(add_dummy_data=True)

class PipelineREST(Resource):

    def get(self):
        pipelines = {'pipelines': [pipeline.get_outgoing_dict() for pipeline in pipeline_state.get_pipelines_()]}

        return Response(json.dumps(pipelines), mimetype='application/json')

    def post(self):
        if not request.json or not 'pipeline_name' in request.json:
            abort(400)

        name = request.json['pipeline_name']
        pdc = PipelineDataContainer()
        pdc.set_pipeline_name(name)
        pipeline_state.add_pipeline_container(pdc)

        return jsonify(pdc.get_outgoing_dict()), 201