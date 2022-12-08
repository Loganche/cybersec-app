import logging.handlers
import os
from pathlib import PurePath

from dotenv import load_dotenv
from fastapi import Depends
from fastapi import FastAPI
from pprint import pprint

logging.basicConfig(
    level=logging.DEBUG,
    handlers=[
        # logging.handlers.RotatingFileHandler('errors.log', maxBytes=10485760, backupCount=10),
        logging.StreamHandler(),
    ],
    format='%(asctime)-15s %(levelname)8s %(process)6d %(name)s %(message)s',
)

# ../../.env
env_path = os.path.join(PurePath(__file__).parents[2], '.env')
if not load_dotenv(env_path):
    raise SystemError('Environment variables not loaded')

from app.routers import auth, invest

app = FastAPI(
    title='Cybersecurity Project',
    version='1.0',
)
app.include_router(auth.router)
app.include_router(invest.router)
