import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:1234@178.154.229.18/gis'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + \
    #     os.path.join(basedir, '../app.sqlite3')
