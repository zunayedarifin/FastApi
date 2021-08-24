from fastapi import APIRouter
from config.db import conn
from models.index import users
from schemas.user import User

user = APIRouter()


@user.get("/")
async def read_data():
    return conn.execute(users.select()).fetchall()


@user.post("/write")
async def write_data(user: User):
    conn.execute(users.insert().values(
        name=user.name,
        email=user.email,
        password=user.password
    ))

    # return conn.execute(users.select()).fetchall()
    return True
