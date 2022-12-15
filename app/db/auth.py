import sqlalchemy
from fastapi.datastructures import Default

from app.db import engine
from app.db import metadata

users = sqlalchemy.Table(
    'users',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True, index=True),
    sqlalchemy.Column('username', sqlalchemy.String, unique=True, index=True),
    sqlalchemy.Column('email', sqlalchemy.String, index=True),
    sqlalchemy.Column('password', sqlalchemy.String),  # hashed
    sqlalchemy.Column('disabled', sqlalchemy.Boolean, default=False),
)

metadata.create_all(engine)
