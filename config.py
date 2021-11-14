from os import environ
from os import urandom
import os.path

from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, ".env"))


class Config:
    """Flask base config"""
    SECRET_KEY = environ.get("SECRET_KEY") or urandom(24)
    SQLALCHEMY_DATABASE_URI = \
        os.environ.get("DATABASE_URL") or \
        f"sqlite:///{os.path.join(basedir, 'app/data.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
