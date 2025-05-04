from src.config import config
from mongoengine import connect


class GoogleDb():
    def __init__(self):
        self.db = None
        self.config = config.Config()

    def initialize_db(self):
        #host = self.config.get_mongo_host()
        host = "localhost"
        print(host)
        connect(
            host=host,
            port=27017,
            authentication_source='admin',
            name='gm_meet',
            alias='default'
        )

