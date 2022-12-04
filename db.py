import sqlite3

conn = sqlite3.connect("model/data/users.sqlite")
cursor = conn.cursor()
sql_query = """ Create table if not exists users (
    id integer primary key AUTOINCREMENT NOT NULL,
    email text NOT NULL,
    password text NOT NULL,
    mobile integer NOT NULL,
    selected_genres text,
    selected_cast text 
) """
cursor.execute(sql_query)