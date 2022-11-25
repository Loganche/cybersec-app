import os
import logging
import logging.handlers
from pathlib import PurePath

from fastapi import FastAPI, Depends
from dotenv import load_dotenv

from app.routers import auth

logging.basicConfig(
    level=logging.DEBUG,
    handlers=[
        # logging.handlers.RotatingFileHandler('errors.log', maxBytes=10485760, backupCount=10),
        logging.StreamHandler(),
    ],
    format="%(asctime)-15s %(levelname)8s %(process)6d %(name)s %(message)s",
)

# ../../.env
env_path = os.path.join(PurePath(__file__).parents[2], '.env')
if not load_dotenv(env_path):
    raise SystemError('Environment variables not loaded')

app = FastAPI(
    title='Cybersecurity Project',
    version='1.0'
)
app.include_router(auth.router)
