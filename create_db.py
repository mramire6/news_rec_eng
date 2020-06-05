import sqlite3

conn = sqlite3.connect('axios_news.db')
c = conn.cursor()

#Create table - Articles
articles_table = """CREATE TABLE IF NOT EXISTS Articles
                    (
                    Section STRING,
                    Hyperlink STRING,
                    ArticleID INTEGER PRIMARY KEY,
                    MainText STRING,
                    Headline STRING,
                    PubDate STRING,
                    WordCount INTEGER
                    );"""
c.execute(articles_table)

#Create table - Authors
authors_table = """CREATE TABLE IF NOT EXISTS Authors
                    (
                    Name STRING,
                    Section STRING,
                    Position STRING,
                    Description STRING,
                    Hyperlink STRING,
                    AuthorID INTEGER PRIMARY KEY,
                    ArticleID INTEGER,
                    FOREIGN KEY(ArticleID) REFERENCES Articles(ArticleID)
                    );"""
c.execute(authors_table)

#Create table - ArticleAuthors
articleauthors_table = """CREATE TABLE IF NOT EXISTS ArticleAuthors
                          (
                          ArticleID INTEGER,
                          AuthorID INTEGER
                          );"""
c.execute(articleauthors_table)

