import os
from sqlalchemy.engine.url import URL

host = os.environ.get('POSTGRES_HOST')
password = os.environ.get('POSTGRES_PASSWORD')

postgres_db = {'drivername': 'postgres',
                   'username': 'root',
                   'password': password,
                   'database': 'postgres',
                   'host': host,
                   'port': 5432}

conn_string = "postgresql://%s:%s@%s/%s" % ('root', password, host, 'postgres')

class Config(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = conn_string
    #SQLALCHEMY_DATABASE_URI = URL(**postgres_db)
