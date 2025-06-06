class Config:
    def __init__(self):
        self.mongo_host = "localhost"
        self.mongo_port = int(27017)
        self.mongo_name = "gm_meet"

    def get_mongo_host(self):
        return self.mongo_host

    def get_mongo_port(self):
        return self.mongo_port

    def get_mongo_name(self):
        return self.mongo_name
