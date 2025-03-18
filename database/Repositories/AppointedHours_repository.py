import json
from bson import ObjectId
from typing import Union
from shared.logger import logger
from database.db_connection import DatabaseConnection
from constants.database_objects import COLLECTION_NAME_APPOINTMENTS
from constants.logger_messages import (
    GET_ALL_APPOINTED_HOURS_LOGGER_MSG,
    GET_APPOINTED_FOR_ID_LOGGER_MSG
)

class AppointedHours_repository:
    
    def __init__(self, db_connection: DatabaseConnection):
        self.db_connection =  db_connection
        self.collection = self.db_connection.get_collection(COLLECTION_NAME_APPOINTMENTS)
    
    @logger(GET_ALL_APPOINTED_HOURS_LOGGER_MSG)
    def get_all_appointed_hours(self) -> Union[list, str]:
        response: object
        try:
            response = list(self.collection.find())
        except Exception as e:
            response = json.dumps({"Erro": str(e)})
        return response
    
    @logger(GET_APPOINTED_FOR_ID_LOGGER_MSG)
    def get_appointed_for_id(self, id: str):
        response: dict
        try:
            response = json.dumps(self.collection.find_one({'_id': ObjectId(id)}), indent=3, default = str)
        except Exception as e:
            response = json.dumps({"Erro": str(e)})
        return response