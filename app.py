import os
from flask import Flask
from flask_restful import Api
from sqlalchemy.engine.url import URL
from models import db
from resources import CommunityPostList 

def get_postgres_parameters():
    host = os.environ.get('POSTGRES_HOST')
    password = os.environ.get('POSTGRES_PASSWORD')

    postgres_db = {'drivername': 'postgres',
                   'username': 'root',
                   'password': password,
                   'database': 'postgres',
                   'host': host,
                   'port': 5432}
    return postgres_db


def create_app():
    app = Flask(__name__)
    app.config['DEBUG'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    postgres_db = get_postgres_parameters()
    app.config['SQLALCHEMY_DATABASE_URI'] = URL(**postgres_db)

    db.init_app(app)
    api = Api(app)
    add_resource(api)

    return app


def run_app():
    try:
        app = create_app()
        logging.info(f'MH API starts running')
        app.run(host='0.0.0.0', threaded=True)
    except Exception as e:
    	raise('Error', e)


def add_resource(api):
    api.add_resource(
        CommunityPostList,
        '/community_post/<string:uid>'
    )


if __name__ == '__main__':
    run_app()