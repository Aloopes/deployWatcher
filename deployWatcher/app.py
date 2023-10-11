# begin prod import compatibility
import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
# end prod import compatibility
import deployWatcher.Resources as rsc
from deployWatcher.database import db

from typing import Dict
from flask import Flask
from flask_restful import Api


def add_resources(api_var: Api):
    api_var.add_resource(rsc.Transitions, '/transitions')

def create_app(config_filename: Dict = None) -> Flask:
    created_app = Flask(__name__)
    api = Api(created_app)

    add_resources(api)

    if config_filename is not None:
        created_app.config.from_mapping(config_filename)
    else: 
        created_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        created_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        created_app.config['PROPAGATE_EXCEPTIONS'] = True
        created_app.secret_key = os.environ.get('DEPLOYWATCHER_KEY')

    db.init_app(created_app)
    db.app = created_app

    if os.environ.get('DEPLOYWATCHER_CONNSTRING') == 'sqlite://':
        with db.app.app_context():
            db.create_all()
            db.session.commit()

    return created_app


def create_app(config_filename: Dict = None) -> Flask:
    created_app = Flask(__name__)
    api = Api(created_app)

    add_resources(api)

    if config_filename is not None:
        created_app.config.from_mapping(config_filename)
    else:  # default config
        created_app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DEPLOYWATCHER_CONNSTRING')
        created_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        created_app.config['PROPAGATE_EXCEPTIONS'] = True
        created_app.secret_key = os.environ.get('DEPLOYWATCHER_KEY')

    db.init_app(created_app)
    db.app = created_app

    if os.environ.get('DEPLOYWATCHER_CONNSTRING') == 'sqlite://':
        db.create_all()
        db.session.commit()

    return created_app


app = create_app()

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0')
