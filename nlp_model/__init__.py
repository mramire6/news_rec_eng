#Initialize the application

from flask import Flask, request
from config import Config, DB_Init_Data
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

#Script to Create/Drop/Seed the database
@app.cli.command('db_create')
def db_create():
    db.create_all()
    print('Database Created!')

@app.cli.command('db_drop')
def db_drop():
    db.drop_all()
    print('Database Dropped!')

@app.cli.command('db_seed')
def db_seed():
    #Add Articles 1 and 2
    db.session.add(DB_Init_Data.article1)
    db.session.add(DB_Init_Data.article2)

    #Add Authors 1 and 2
    db.session.add(DB_Init_Data.author1)
    db.session.add(DB_Init_Data.author2)

    #Add relationship between authors and articles
    DB_Init_Data.author1.pieces.append(DB_Init_Data.article1)
    DB_Init_Data.author2.pieces.append(DB_Init_Data.article1)
    DB_Init_Data.author2.pieces.append(DB_Init_Data.article2)

    db.commit()
    print('Database Seeded!')

from nlp_model import routes


