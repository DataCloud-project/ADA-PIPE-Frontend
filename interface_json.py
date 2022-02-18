import json
from typing import List
from copy import copy, deepcopy
import json_exceptions
from flask import jsonify

from interface_constants import *


number_of_decimals: int = 5


class JobDataContainer():

    def __init__(self, job_dict: dict) -> None:
        if not self._is_valid_job_dictionary(job_dict):
            raise json_exceptions.KeyNotInJSON()
        self._job_dict: dict = job_dict

    def to_json(self) -> str:
        return jsonify(self._job_dict)

    def get_resource(self) -> str:
        if JOB_RESOURCE not in self._job_dict:
            raise json_exceptions.KeyNotInJSON()

        return copy(self._job_dict[JOB_RESOURCE])

    def get_requirements(self) -> dict:
        if JOB_REQUIREMENTS not in self._job_dict:
            raise json_exceptions.KeyNotInJSON()

        return deepcopy(self._job_dict[JOB_REQUIREMENTS])

    def get_job_health_check(self) -> dict:
        if JOB_HEALTH_CHECK not in self._job_dict:
            raise json_exceptions.KeyNotInJSON()

        return deepcopy(self._job_dict[JOB_HEALTH_CHECK])

    def get_job_health_check_(self) -> dict:
        if JOB_HEALTH_CHECK not in self._job_dict:
            raise json_exceptions.KeyNotInJSON()

        return self._job_dict[JOB_HEALTH_CHECK]

    def get_job_termination_check(self) -> dict:
        if JOB_TERMINATION_CHECK not in self._job_dict:
            raise json_exceptions.KeyNotInJSON(JOB_TERMINATION_CHECK)

        return deepcopy(self._job_dict[TERMINATION_CHECK])


    def get_job_termination_check_(self) -> dict:
        if JOB_TERMINATION_CHECK not in self._job_dict:
            raise json_exceptions.KeyNotInJSON(JOB_TERMINATION_CHECK)

        return self._job_dict[TERMINATION_CHECK]

    def _is_valid_job_dictionary(self, job_dict: dict) -> bool:
        # TODO
        return True


class PipelineDataContainer():

    def __init__(self, template_path: str = 'template.json') -> None:
        self.__template_path: str = template_path
        self.__json_template = self.__load_template_json_file(self.__template_path)

    def __load_template_json_file(self, template_path: str):
        '''Loading the template json file to provide the structure for the JSON object'''
        with open(template_path, 'r') as json_file:
            template = json.load(json_file)
            return template

    def get_json_dict(self) -> dict:
        return deepcopy(self.__json_template)

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

    def get_step_name(self) -> str:
        return copy(self.__json_template[STEP_NAME])

    def set_step_name(self, step_name: str) -> None:
        if step_name is None or not type(step_name) == str:
            raise json_exceptions.InvalidParameter()
        self.__json_template[STEP_NAME] = step_name

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
        time_elem[TERMINATION_TIME] = round(
            est_start_time + est_finish_time, number_of_decimals)

    def get_jobs(self) -> List[JobDataContainer]:
        job_list = self.__json_template[JOB]
        job_list = [JobDataContainer(job) for job in job_list]
        return job_list


    def get_jobs_as_json(self) -> str:
        jobs: List[JobDataContainer] = self.get_jobs()
        jobs = [job._job_dict for job in jobs]

        return json.dumps({'job': jobs})

    


pt = PipelineDataContainer()
# print(pt.get_jobs_as_json())

# job = pt.get_jobs().pop()
# print(job.get_job_health_check())
