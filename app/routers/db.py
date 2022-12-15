from fastapi import APIRouter

from app.db import database

router = APIRouter(
    prefix='/auth',
    tags=['auth'],
)


@router.on_event('startup')
async def startup():
    await database.connect()


@router.on_event('shutdown')
async def shutdown():
    await database.disconnect()
