from nlp_model import db


association = db.Table('association',
    db.Column('articleID', db.Integer, db.ForeignKey('articles.articleID')),
    db.Column('authorID', db.Integer, db.ForeignKey('authors.authorID'))
    )

class Articles(db.Model):
    __tablename__ = 'articles'
    articleID = db.Column(db.Integer, primary_key=True)
    section = db.Column(db.String(20), unique=False, nullable=False)
    headline = db.Column(db.String(120), unique=False, nullable=False)
    main_text = db.Column(db.Text, unique=False, nullable=False)
    date_published = db.Column(db.String(10), nullable=False)
    word_count = db.Column(db.Integer)
    hyper_link = db.Column(db.String(200), unique=True, nullable=False)
    piece = db.relationship('authors', secondary=association, backref=db.backref('pieces', lazy=True))

    def __repr__(self):
        return f"articles('{self.headline}', '{self.date_published}')"

class Authors(db.Model):
    __tablename__ = 'authors'
    authorID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), unique=False, nullable=False)
    position = db.Column(db.String(40), unique=False, nullable=True)
    description = db.Column(db.Text, unique=False, nullable=True)
    section = db.Column(db.String(20), unique=False, nullable=False)
    hyper_link = db.Column(db.String(200), unique=True, nullable=False)

    def __repr__(self):
        return f"authors('{self.name}', '{self.section}')"


