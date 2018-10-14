import os

host = os.environ.get('POSTGRES_HOST')
password = os.environ.get('POSTGRES_PASSWORD')

conn_string = "postgresql://%s:%s@%s/%s" % ('root', password, host, 'postgres')

class Config(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = conn_string
