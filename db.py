import sqlite3

conn = sqlite3.connect("postgres://uqtpxryhwlcazx:c0b39d30a1b2f9415b7aa7777277f7ecd9ad495c0859296ea63cdd1823b1d197@ec2-34-231-221-151.compute-1.amazonaws.com:5432/dc18lg9t4rf23o")
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