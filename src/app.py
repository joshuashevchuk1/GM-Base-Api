from fastapi import FastAPI
from contextlib import asynccontextmanager
import uvicorn
from handlers import handlers
from src.database.db import GoogleDb


class GMApp:
    def __init__(self, port: int):
        self.port = port

        @asynccontextmanager
        async def lifespan(app: FastAPI):
            # Startup: connect to Mongo
            mongo = GoogleDb()
            mongo.initialize_db()
            yield
            # Shutdown: clean-up here if needed (e.g., mongo.disconnect() if implemented)

        self.app = FastAPI(
            title="GM Base API",
            description="A modular FastAPI app with home and health check endpoints.",
            version="1.0.0",
            lifespan=lifespan,
        )

        self._include_routes()

    def _include_routes(self):
        for route in handlers:
            self.app.include_router(route)

    def run_server(self):
        uvicorn.run(self.app, host="0.0.0.0", port=self.port)


if __name__ == "__main__":
    app = GMApp(port=8000)
    app.run_server()
