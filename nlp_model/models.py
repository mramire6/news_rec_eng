from nlp_model import db

association = db.Table('association',
    db.Column('articleID', db.Integer, db.ForeignKey('articles.articleID')),
    db.Column('authorID', db.Integer, db.ForeignKey('authors.authorID'))
    )

class Articles(db.Model):
     articleID = db.Column(db.Integer, primary_key=True)
     section = db.Column(db.String(20), unique=False, nullable=False)
     headline = db.Column(db.String(120), unique=False, nullable=False)
     main_text = db.Column(db.Text, unique=False, nullable=False)
     date_published = db.Column(db.String(10), nullable=False)
     word_count = db.Column(db.Integer)
     hyper_link = db.Column(db.String(200), unique=True, nullable=False)
     piece = db.relationship('Authors', secondary=association, backref=db.backref('pieces', lazy=True))

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


###### Dummy data for validation

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

