import json
from typing import Union
from database.db_connection import DatabaseConnection
from constants.database_objects import COLLECTION_NAME_PPLANNINGS
from constants.logger_messages import (
    GET_ALL_PPLANNING_LOGGER_MSG,
    GET_PPLANNING_FOR_ID_LOGGER_MSG
    )
from shared.logger import logger

class ProjectPlanning_repository:

    def __init__(self, db_connection: DatabaseConnection):
        self.db_connection = db_connection
        self.collection = db_connection.get_collection(COLLECTION_NAME_PPLANNINGS)
    
    @logger(GET_ALL_PPLANNING_LOGGER_MSG)
    def get_all_pplaning(self) -> Union[list, str]:
        response: object
        try:
            response = list(self.collection.find())
        except Exception as e:
            response = json.loads({"Erro": str(e)})
        return response

    @logger(GET_PPLANNING_FOR_ID_LOGGER_MSG)
    def get_pplanning_for_id(self, id: str):
        response: dict
        try:
            response = json.dumps(self.collection.find_one({'planning_id': id}), indent=3)
        except Exception as e:
            response = json.dumps({"Erro": str(e)})
        return response