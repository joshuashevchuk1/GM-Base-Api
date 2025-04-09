from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
import uvicorn

class CommonApp:
    def __init__(self, port: int):
        self.port = port
        self.app = FastAPI()
        self.add_routes()

    def home(self):
        return PlainTextResponse("ok", status_code=200)

    def health_check(self):
        return PlainTextResponse("healthcheck", status_code=200)

    def add_routes(self):
        self.app.get("/", response_class=PlainTextResponse)(self.home)
        self.app.get("/healthCheck", response_class=PlainTextResponse)(self.health_check)

    def run_server(self):
        uvicorn.run(self.app, host="0.0.0.0", port=self.port)

# Example usage
if __name__ == "__main__":
    app = CommonApp(port=8000)
    app.run_server()
