import sqlite3

conn = sqlite3.connect("postgres://umskvhjcqkyctz:aa08618da326a858e0f066afa824bdbd84330a158d9647e82b950e123c3d8899@ec2-54-211-255-161.compute-1.amazonaws.com:5432/d5rhim06g4g2p1")
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