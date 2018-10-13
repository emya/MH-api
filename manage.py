import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask import Flask, current_app
from config import Config

from app import app, db

with app.app_context():
    print(current_app.config, type(current_app.config))
    print(current_app.config.__dict__, type(current_app.config))

app.config.from_object(os.environ['APP_SETTINGS'])
#print(app.__dict__['SQLALCHEMY_DATABASE_URI'])

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()