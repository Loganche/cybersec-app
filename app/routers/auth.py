import os
from datetime import timedelta

import sentry_sdk
from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from fastapi.security import OAuth2PasswordRequestForm

from app.auth import authenticate_user
from app.auth import create_access_token
from app.auth import get_current_active_user
from app.db import fake_users_db
from app.models.auth import Token
from app.models.auth import User

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
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Incorrect username or password',
            headers={'WWW-Authenticate': 'Bearer'},
        )
    access_token_expires = timedelta(minutes=float(os.environ['ACCESS_TOKEN_EXPIRE_MINUTES']))
    access_token = create_access_token(
        data={'sub': user.username}, expires_delta=access_token_expires,
    )
    return {'access_token': access_token, 'token_type': 'bearer'}


@router.get(
    '/user',
    response_model=User,
    status_code=status.HTTP_200_OK,
)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user
