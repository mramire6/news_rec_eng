from datetime import datetime
from nlp_model import db

class Articles(db.Model):
     articleID = db.Column(db.Integer, primary_key=True)
     section = db.Column(db.String(20), unique=False, nullable=False)
     headline = db.Column(db.String(120), unique=False, nullable=False)
     main_text = db.Column(db.Text, unique=False, nullable=False)
     date_published = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
     word_count = db.Column(db.Integer)
     hyper_link = db.Column(db.String(200), unique=True, nullable=False)

     def __repr__(self):
        return f"Articles('{self.headline}', '{self.date_published}')"

class Authors(db.Model):
    authorID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), unique=False, nullable=False)
    position = db.Column(db.String(40), unique=False, nullable=True)
    description = db.Column(db.Text, unique=False, nullable=True)
    section = db.Column(db.String(20), unique=False, nullable=False)
    hyper_link = db.Column(db.String(200), unique=True, nullable=False)

    def __repr__(self):
        return f"Authors('{self.name}', '{self.section}')"

# class ArticlesAuthors(db.Model):
#     articleID = db.Column(db.Integer, db.ForeignKey('articles.articleID'))
#     authorID = db.Column(db.Integer, db.ForeignKey('authors.authorID'))
