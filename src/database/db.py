from mongoengine import connect


class GoogleDb():
    def __init__(self):
        self.db = None

    def initialize_db(self):
        connect(
            host='localhost',
            port=27017,
            authentication_source='admin',
            name='gm_meet',
            alias='default'
        )

