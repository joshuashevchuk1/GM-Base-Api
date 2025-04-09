from fastapi import FastAPI, Header, HTTPException, status
from fastapi.responses import PlainTextResponse, JSONResponse
from pydantic import BaseModel
import uvicorn

class HealthStatus(BaseModel):
    status: str
    version: str

class CommonApp:
    def __init__(self, port: int):
        self.port = port
        self.app = FastAPI(
            title="CommonApp API",
            description="A simple FastAPI app with home and health check endpoints.",
            version="1.0.0",
            contact={
                "name": "Your Name",
                "url": "https://your-site.com",
                "email": "you@example.com",
            },
        )
        self.add_routes()

    def home(self):
        return PlainTextResponse("ok", status_code=200)

    def health_check(self):
        return HealthStatus(status="healthy", version="1.0.0")

    def secure_data(self, token: str = Header(..., description="Bearer token")):
        if token != "Bearer mysecrettoken":
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
        return {"data": "Secure info", "user": "authorized"}

    def add_routes(self):
        self.app.get(
            "/",
            response_class=PlainTextResponse,
            tags=["Root"],
            summary="Home endpoint",
            description="Simple health probe for root access.",
            responses={200: {"description": "Service is up"}},
        )(self.home)

        self.app.get(
            "/healthCheck",
            response_model=HealthStatus,
            tags=["Health"],
            summary="Health check endpoint",
            description="Returns the current health status and app version.",
            responses={
                200: {"description": "Service health status"},
                500: {"description": "Internal server error"},
            },
        )(self.health_check)

    def run_server(self):
        uvicorn.run(self.app, host="0.0.0.0", port=self.port)

# Example usage
if __name__ == "__main__":
    app = CommonApp(port=8000)
    app.run_server()
