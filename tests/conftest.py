import os

from alembic import command
from alembic.config import Config
from flask import Flask
import pytest

import routes
from sqlalchemy.testing import db


def run_migrations():
    alembic_cfg = Config("alembic.ini")
    alembic_cfg.attributes['sqlalchemy.url'] = os.environ.get('DATABASE_URL_TEST')
    command.upgrade(alembic_cfg, "head")


@pytest.fixture(scope='session')
def app():
    app = Flask(__name__, template_folder='../templates')
    print('\n===========================================')

    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL_TEST')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = '@##&6cweafhv3426445'
    app.config['REMEMBER_COOKIE_HTTPONLY'] = False
    app.config['SESSION_COOKIE_HTTPONLY'] = False
    app.url_map.strict_slashes = False

    db.init_app(app)

    app.app_context().push()

    run_migrations()

    routes.install_routes()

    print('\n===========================================')

