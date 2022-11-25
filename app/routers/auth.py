import os
from datetime import timedelta

from fastapi import Depends, APIRouter, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from app.models.auth import Token, User
from app.auth import authenticate_user, create_access_token, get_current_active_user
from app.db import fake_users_db

router = APIRouter(
    prefix='/auth',
    tags=['auth'],
)


@router.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=float(os.environ['ACCESS_TOKEN_EXPIRE_MINUTES']))
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/user", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user
