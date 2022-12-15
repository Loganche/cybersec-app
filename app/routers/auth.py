import os
from datetime import timedelta
from typing import List

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Security
from fastapi import status
from fastapi.responses import RedirectResponse
from fastapi.security import OAuth2PasswordRequestForm

from app.auth import authenticate_user
from app.auth import create_access_token
from app.auth import get_current_active_user
from app.auth import get_password_hash
from app.db import database
from app.db.auth import users
from app.models.auth import Token
from app.models.auth import User
from app.models.auth import UserCreate

router = APIRouter(
    prefix='/auth',
    tags=['auth'],
)


@router.post(
    '/token',
    response_model=Token,
    status_code=status.HTTP_202_ACCEPTED,
)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Incorrect username or password',
            headers={'WWW-Authenticate': 'Bearer'},
        )
    access_token_expires = timedelta(minutes=float(os.environ['ACCESS_TOKEN_EXPIRE_MINUTES']))
    access_token = create_access_token(
        data={'sub': user.username, 'scopes': form_data.scopes}, expires_delta=access_token_expires,
    )
    return {'access_token': access_token, 'token_type': 'bearer'}


@router.get(
    '/user',
    response_class=RedirectResponse,
    status_code=status.HTTP_302_FOUND,
)
async def read_users_me(current_user: User = Security(get_current_active_user)):
    return f'/auth/users/{current_user.id}/'


@router.post(
    '/users/',
    response_class=RedirectResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_user(user: UserCreate):
    query = users.insert().values(
        username=user.username,
        email=user.email,
        password=get_password_hash(user.password),
        disabled=False,
    )
    id = await database.execute(query)
    return f'/auth/users/{id}/'


@router.get(
    '/users/{id}',
    response_model=User,
    response_model_exclude={'password', 'id'},
    status_code=status.HTTP_200_OK,
)
async def get_user(id: int):
    query = users.select().where(users.columns.id == id)
    return await database.fetch_one(query)


@router.get(
    '/users/',
    response_model=List[User],
    response_model_exclude={'password'},
    status_code=status.HTTP_200_OK,
)
async def list_users():
    query = users.select()
    return await database.fetch_all(query)
