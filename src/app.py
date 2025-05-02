# main.py

from fastapi import FastAPI
import uvicorn
from handlers import handlers
from src.database.db import GoogleDb


class GMApp:
    def __init__(self, port: int):
        self.port = port
        self.app = FastAPI(
            title="GM Base API",
            description="A modular FastAPI app with home and health check endpoints.",
            version="1.0.0",
        )
        self.db = None
        self._include_routes()
        #self._init_mongo()


    def _include_routes(self):
        for route in handlers:
            self.app.include_router(route)

    def _init_mongo(self):
        """Initialize MongoDB and other connections."""
        google_mongo = GoogleDb()
        google_mongo.initialize_db()
        self.db = google_mongo.db

    def run_server(self):
        uvicorn.run(self.app, host="0.0.0.0", port=self.port)

if __name__ == "__main__":
    app = GMApp(port=8000)
    app.run_server()
