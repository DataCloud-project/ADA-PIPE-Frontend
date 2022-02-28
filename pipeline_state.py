from typing import List
from interface_json import PipelineDataContainer, JobDataContainer
from copy import copy, deepcopy


class PipelineState():
    
    def __init__(self) -> None:
        self.__pipelines: List[PipelineDataContainer] = []

    def add_pipeline_container(self, pipeline: PipelineDataContainer):
        self.__pipelines.append(pipeline)

    def get_pipelines(self) -> List[PipelineDataContainer]:
        return deepcopy(self.get_pipelines)

    def get_pipelines_(self) -> List[PipelineDataContainer]:
        return self.__pipelines

    def __get__(self, idx) -> PipelineDataContainer:
        return self.__pipelines[idx]

