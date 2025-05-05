from src.config import config
from mongoengine import connect


class GoogleDb():
    def __init__(self):
        self.db = None
        self.config = config.Config()

    def initialize_db(self):
        connect(
            host=self.config.get_mongo_host(),
            port=self.config.get_mongo_port(),
            authentication_source='admin',
            name=self.config.get_mongo_name(),
            alias='default'
        )

