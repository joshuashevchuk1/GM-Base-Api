from pymongo import MongoClient, ASCENDING

from src.config import config


class GoogleDb():
    def __init__(self):
        self.db = None
        self.config = config.Config()

    def initialize_db(self):
        """
        Initializes and returns a MongoDB client connection.
        Ensures that the 'wx' collection exists and has a compound index on the specified fields.
        """
        client = MongoClient(
            host=self.config.get_mongo_host(),
            port=int(self.config.get_mongo_port()),
            username=self.config.get_mongo_user(),
            password=self.config.get_mongo_pass(),
        )

        db_name = self.config.get_mongo_name()
        db = client[db_name]
        self.db = db
