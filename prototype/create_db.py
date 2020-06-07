import sqlite3
import db_config

def create_connection(db_filename):
    conn = sqlite3.connect(db_filename)
    print('connection to sqlite established')
    return conn

def create_table(conn, create_table_sql):
    c = conn.cursor()
    print('cursor object created')
    c.execute(create_table_sql)
    print('Empty table has been created in database')

if __name__ == "__main__":
    conn = create_connection(db_config.db_filename)
    create_table(conn, db_config.articles_table)
    create_table(conn, db_config.authors_table)
    create_table(conn, db_config.articleauthors_table)

