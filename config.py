import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = (os.environ.get('SQLALCHEMY_DATABASE_URI')
        or 'sqlite:///axios.db')

class Defaults(object):
    section_default = ['politics-policy',
                       'technology',
                       'economy-business',
                       'health',
                       'world',
                       'energy-environment',
                       'science',
                       'sports']
