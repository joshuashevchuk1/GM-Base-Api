# main.py

from fastapi import FastAPI
import uvicorn
from routes import routers

class GMApp:
    def __init__(self, port: int):
        self.port = port
        self.app = FastAPI(
            title="GM Base API",
            description="A modular FastAPI app with home and health check endpoints.",
            version="1.0.0",
            contact={
                "name": "Your Name",
                "url": "https://your-site.com",
                "email": "you@example.com",
            },
        )
        self.include_routes()

    def include_routes(self):
        for route in routers:
            self.app.include_router(route)

    def run_server(self):
        uvicorn.run(self.app, host="0.0.0.0", port=self.port)

if __name__ == "__main__":
    app = GMApp(port=8000)
    app.run_server()
