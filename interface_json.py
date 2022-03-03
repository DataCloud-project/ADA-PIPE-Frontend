import json
from typing import List
from copy import copy, deepcopy
import json_exceptions
from flask import jsonify

from interface_constants import *


number_of_decimals: int = 5


class StepsDataContainer():

    def __init__(self, job_dict: dict) -> None:
        if not self._is_valid_steps_dictionary(job_dict):
            raise json_exceptions.KeyNotInJSON()
        self._job_dict: dict = job_dict

    def to_json(self) -> str:
        return jsonify(self._job_dict)

    def get_resource(self) -> str:
        if STEPS_RESOURCE not in self._job_dict:
            raise json_exceptions.KeyNotInJSON()

        return copy(self._job_dict[STEPS_RESOURCE])

    def get_requirements(self) -> dict:
        if STEPS_REQUIREMENTS not in self._job_dict:
            raise json_exceptions.KeyNotInJSON()

        return deepcopy(self._job_dict[STEPS_REQUIREMENTS])

    def get_steps_health_check(self) -> dict:
        if STEPS_HEALTH_CHECK not in self._job_dict:
            raise json_exceptions.KeyNotInJSON()

        return deepcopy(self._job_dict[STEPS_HEALTH_CHECK])

    def get_steps_health_check_(self) -> dict:
        if STEPS_HEALTH_CHECK not in self._job_dict:
            raise json_exceptions.KeyNotInJSON()

        return self._job_dict[STEPS_HEALTH_CHECK]

    def get_steps_termination_check(self) -> dict:
        if STEPS_TERMINATION_CHECK not in self._job_dict:
            raise json_exceptions.KeyNotInJSON(STEPS_TERMINATION_CHECK)

        return deepcopy(self._job_dict[TERMINATION_CHECK])


    def get_steps_termination_check_(self) -> dict:
        if STEPS_TERMINATION_CHECK not in self._job_dict:
            raise json_exceptions.KeyNotInJSON(STEPS_TERMINATION_CHECK)

        return self._job_dict[TERMINATION_CHECK]

    def _is_valid_steps_dictionary(self, job_dict: dict) -> bool:
        # TODO
        return True


class PipelineDataContainer():

    def __init__(self, template_path: str = 'internal_template.json') -> None:
        self.__template_path: str = template_path
        self.__json_template = self.__load_template_json_file(self.__template_path)

    def __load_template_json_file(self, template_path: str):
        '''Loading the template json file to provide the structure for the JSON object'''
        with open(template_path, 'r') as json_file:
            template = json.load(json_file)
            return template

    def get_json_dict(self) -> dict:
        return deepcopy(self.__json_template)

    def get_outgoing_dict(self) -> dict:
        outgoing_dict: dict = deepcopy(self.__json_template)
        outgoing_dict.pop(TIME)
        return outgoing_dict

    def get_json_as_string(self) -> str:
        json_string = json.dumps(self.__json_template)
        return json_string

    def set_pipeline_data(self, pipeline_data: dict):
        if pipeline_data is None:
            raise json_exceptions.InvalidParameter()
        # TODO Check if the dictionary keys are valid
        # For now assume they are
        self.__json_template = pipeline_data

    def get_pipeline_name(self) -> str:
        return copy(self.__json_template['pipelineName'])

    def set_pipeline_name(self, pipeline_name: str) -> None:
        if pipeline_name is None or not type(pipeline_name) == str:
            raise json_exceptions.InvalidParameter(
                'Invalid pipeline_name parameter')
        self.__json_template[PIPELINE_NAME] = pipeline_name

    def get_pipeline_type(self) -> str:
        return copy(self.__json_template[PIPELINE_TYPE])

    def set_pipeline_type(self, pipeline_type: str):
        if pipeline_type is None or not type(pipeline_type) == str:
            raise json_exceptions.InvalidParameter()
        self.__json_template[PIPELINE_TYPE] = pipeline_type

    def get_chunk_name(self) -> str:
        return copy(self.__json_template[CHUNK_NAME])

    def set_chunk_name(self, step_name: str) -> None:
        if step_name is None or not type(step_name) == str:
            raise json_exceptions.InvalidParameter()
        self.__json_template[CHUNK_NAME] = step_name

    def get_termination_check(self) -> dict:
        termination_check = self.__json_template[TERMINATION_CHECK]
        return deepcopy(termination_check)

    def set_termination_check(self, termination_check: dict) -> None:
        self.__json_template[TERMINATION_CHECK] = termination_check

    def get_estimated_time(self) -> dict:
        time_dict = self.__json_template[TIME]
        return deepcopy(time_dict)

    def set_estimated_time(self, est_start_time: float, est_finish_time: float):
        time_elem = self.__json_template[TIME]
        time_elem[ESTIMATED_START_TIME] = est_start_time
        time_elem[ESTIMATED_FINISH_TIME] = est_finish_time

    def get_steps(self) -> List[StepsDataContainer]:
        steps_list = self.__json_template[STEPS_LIST_KEY]
        steps_list = [StepsDataContainer(step) for step in steps_list]
        return steps_list


    def get_steps_as_json(self) -> str:
        steps: List[StepsDataContainer] = self.get_steps()
        steps = [step._job_dict for step in steps]

        return json.dumps({STEPS_LIST_KEY: steps})

    


pt = PipelineDataContainer()
print(pt.get_steps_as_json())

# job = pt.get_steps().pop()
# print(job.get_steps_health_check())
