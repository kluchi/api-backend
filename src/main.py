from fastapi import FastAPI
from environs import Env
import uvicorn
env = Env()


class Config:
    server_port = env.int("SERVER_PORT", 8080)
    server_ip = env("SERVER_BIND_IP", "0.0.0.0")
    base_path = env("API_BASE_PATH", "/")


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


if __name__ == "__main__":
    uvicorn.run("main:app", host=Config.server_ip, port=Config.server_port,
                log_level="info", root_path=Config.base_path)
