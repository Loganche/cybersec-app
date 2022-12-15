import logging.handlers
import os
from pathlib import PurePath

import sentry_sdk
from dotenv import load_dotenv
from fastapi import FastAPI
from sentry_sdk.integrations.sqlalchemy import SqlalchemyIntegration

logging.basicConfig(
    level=logging.INFO,
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

sentry_sdk.init(
    dsn=os.environ['SENTRY_URL'],
    debug=bool(int(os.environ['DEBUG'])),
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production,
    traces_sample_rate=float(os.environ['SENTRY_COVERAGE']),
    integrations=[
        SqlalchemyIntegration(),
    ],
)


from app.routers import auth, invest, db

app = FastAPI(
    title='Cybersecurity Project',
    version='1.0',
)
app.include_router(auth.router)
app.include_router(invest.router)
app.include_router(db.router)
