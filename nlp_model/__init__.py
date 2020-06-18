#Initialize the application using Application Factory

from flask import Flask
from config import DevConfig
from flask_sqlalchemy import SQLAlchemy

# Globally accessible libraries
db = SQLAlchemy()

def create_app(config_class=DevConfig):
    """Initialize the core application"""

    app = Flask(__name__)
    #Using the development configuration
    app.config.from_object(config_class)

    #Initialize Plugins
    db.init_app(app)

    from nlp_model.home.routes import main_bp
    from nlp_model.news.routes import news_bp
    from nlp_model.nlp_pred_model.routes import nlp_pred_model_bp
    from nlp_model.scrape_analytics.routes import nlp_pred_model_analytics_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(news_bp)
    app.register_blueprint(nlp_pred_model_bp)
    app.register_blueprint(nlp_pred_model_analytics_bp)

    return app


#Script to Create/Drop/Seed the database
# @app.cli.command('db_create')
# def db_create():
#     db.create_all()
#     print('Database Created!')

# @app.cli.command('db_drop')
# def db_drop():
#     db.drop_all()
#     print('Database Dropped!')

# @app.cli.command('db_seed')
# def db_seed():
#     #Add Articles 1 and 2
#     db.session.add(DB_Init_Data.article1)
#     db.session.add(DB_Init_Data.article2)

#     #Add Authors 1 and 2
#     db.session.add(DB_Init_Data.author1)
#     db.session.add(DB_Init_Data.author2)

#     #Add relationship between authors and articles
#     DB_Init_Data.author1.pieces.append(DB_Init_Data.article1)
#     DB_Init_Data.author2.pieces.append(DB_Init_Data.article1)
#     DB_Init_Data.author2.pieces.append(DB_Init_Data.article2)

#     db.commit()
#     print('Database Seeded!')


