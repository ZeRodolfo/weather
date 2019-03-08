from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

# settings database
adapter = os.getenv('DB_ADAPTER')
username = os.getenv('DB_USER')
password = os.getenv('DB_PASS')
hostname = os.getenv('DB_HOST')
database = os.getenv('DB_DATABASE')

data_engine = '%s://%s:%s@%s/%s' % (adapter, username, password, hostname, database)

engine = create_engine(data_engine, convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    import models
    Base.metadata.create_all(bind=engine)