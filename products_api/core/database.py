from pymongo import MongoClient
from pymongo.database import Database
from pymongo.collection import Collection

from products_api.core.settings import settings


class MongoDB:
    def __init__(self, host, port, user, password):
        self._host = host
        self._port = port
        self._user = user
        self._password = password

        self._MAX_POOL_SIZE = 10
        self._HEARTBEAT_FREQUENCY_MS = 1000
        self._IMMEDIATELY_BEGIN_MONGO_CONN = True

    @property
    def sync_client(self):
        return MongoClient(
            host=self._host,
            port=self._port,
            username=self._user,
            password=self._password,
            maxPoolSize=self._MAX_POOL_SIZE,
            heartbeatFrequencyMS=self._HEARTBEAT_FREQUENCY_MS,
            connect=self._IMMEDIATELY_BEGIN_MONGO_CONN,
        )
    
    @property
    def async_client(self):
        raise NotImplementedError

    def get_db_session(self, database_name: str) -> Database:
        return self.sync_client.get_database(database_name)
    
    def get_db_collection(self, database_name: str, collection_name: str) -> Collection:
        return self.get_db_session(database_name).get_collection(collection_name)
    
    def get_async_db_session(self, database_name: str):
        raise NotImplementedError

mongodb = MongoDB(
    host=settings.MONGODB_HOST,
    port=settings.MONGODB_PORT,
    user=settings.MONGODB_USER,
    password=settings.MONGODB_PASSWORD,
)
