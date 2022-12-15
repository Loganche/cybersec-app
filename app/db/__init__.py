import os

import databases
import sqlalchemy

database = databases.Database(os.environ['SQLITE_DB_URL'])

metadata = sqlalchemy.MetaData()


engine = sqlalchemy.create_engine(
    os.environ['SQLITE_DB_URL'], connect_args={'check_same_thread': False},
)

metadata.create_all(engine)
