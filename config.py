import os
from models import Articles, Authors, association

class Config(object):
    """ Set Flask Configuration from .flaskenv File"""

    # General config
    SECRET_KEY = os.environ.get('SECRET_KEY')
    FLASK_APP = os.environ.get('FLASK_APP')
    FLASK_ENV = os.environ.get('FLASK_ENV')

    # Database config
    SQLALCHEMY_DATABASE_URI = (os.environ.get('SQLALCHEMY_DATABASE_URI')
    or 'sqlite:///axios.db')
    SQLALCHEMY_ECHO = False #True will log database activity to stderr


class Defaults(object):
    section_default = ['',
                       'politics-policy',
                       'technology',
                       'economy-business',
                       'health',
                       'world',
                       'energy-environment',
                       'science',
                       'sports']
    main_url = 'https://www.axios.com/'

class DB_Init_Data():
    """ Dummy data to initialize database with """
    article1 = Articles(section='health',
                        headline='Hello World',
                        main_text='This is the first article',
                        date_published='06/11/2020',
                        word_count=100,
                        hyper_link='article1_link')

    article2 = Articles(section='technology',
                        headline='Hello World',
                        main_text='This is a second article',
                        date_published='06/11/2020',
                        word_count=100,
                        hyper_link='article2_link')

    author1 = Authors(name='Jane Doe',
                      position='Superstar Journalist',
                      description='Super awesome journalist',
                      section='health',
                      hyper_link='author1_link')

    author2 = Authors(name='John Doe',
                      position='Novastar Journalist',
                      description='Gets better scoops than ice cream',
                      section='health',
                      hyper_link='author2_link')


