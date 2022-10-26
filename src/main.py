import random
import string

from typing import Optional, Tuple
from fastapi import FastAPI, APIRouter
from environs import Env
import uvicorn
import pydantic
from pydantic import UUID4


env = Env()


class Config:
    server_port = env.int("SERVER_PORT", 8080)
    server_ip = env("SERVER_BIND_IP", "0.0.0.0")
    base_path = env("API_BASE_PATH", "/")


app = FastAPI(openapi_url="/api/openapi.json",
              docs_url="/api/docs", redoc_url="/api/redoc")


class User(pydantic.BaseModel):
    id: pydantic.UUID4
    first_name: str
    last_name: str


@app.get("/")
async def read_root():
    return {"Hello": "World"}


def random_string(size: int) -> str:
    return "".join(random.choices(string.ascii_lowercase, k=size))


def generate_name(user_id: UUID4) -> Tuple[str, str]:
    random.seed(str(user_id))
    return random_string(8).capitalize(), \
        random_string(8).capitalize()


users = APIRouter()


@users.get("/{user_id}", response_model=Optional[User])
async def get_user(user_id: UUID4) -> Optional[User]:
    first_name, last_name = generate_name(user_id)
    return User(id=user_id, first_name=first_name, last_name=last_name)


app.include_router(users, prefix="/api/v0/users")

if __name__ == "__main__":
    uvicorn.run("main:app", host=Config.server_ip, port=Config.server_port,
                log_level="info", root_path=Config.base_path)
