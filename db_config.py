db_filename = 'axios_news.db'

articles_table = """CREATE TABLE IF NOT EXISTS Articles (
                    Section STRING,
                    Hyperlink STRING,
                    ArticleID INTEGER PRIMARY KEY,
                    MainText STRING,
                    Headline STRING,
                    PubDate STRING,
                    WordCount INTEGER);"""

authors_table = """CREATE TABLE IF NOT EXISTS Authors (
                    Name STRING,
                    Section STRING,
                    Position STRING,
                    Description STRING,
                    Hyperlink STRING,
                    AuthorID INTEGER PRIMARY KEY,
                    ArticleID INTEGER,
                    FOREIGN KEY(ArticleID) REFERENCES Articles(ArticleID));"""

articleauthors_table = """CREATE TABLE IF NOT EXISTS ArticleAuthors (
                    ArticleID INTEGER,
                    AuthorID INTEGER);"""
