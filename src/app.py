# main.py

from fastapi import FastAPI
import uvicorn
from routes import routers
from src.models.transcript import Transcript

class GMApp:
    def __init__(self, port: int):
        self.port = port
        self.app = FastAPI(
            title="GM Base API",
            description="A modular FastAPI app with home and health check endpoints.",
            version="1.0.0",
        )
        self.setup_events()
        self.include_routes()

    def setup_events(self):
        @self.app.on_event("startup")
        async def startup_event():
            Transcript.init_table()

    def include_routes(self):
        for route in routers:
            self.app.include_router(route)

    def run_server(self):
        uvicorn.run(self.app, host="0.0.0.0", port=self.port)

if __name__ == "__main__":
    app = GMApp(port=8000)
    app.run_server()
