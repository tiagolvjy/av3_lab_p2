import sqlite3

conn = sqlite3.connect("SorrisoSkins.db")
c = conn.cursor()

c.execute("""
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        username VARCHAR(150) UNIQUE,
        password VARCHAR(150)
    )
    """)
c.execute("""
    CREATE TABLE IF NOT EXISTS cart (
        skin_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        skin_name VARCHAR(150),
        price FLOAT,
        FOREIGN KEY (user_id) REFERENCES users(id)
    )
    """)

conn.commit()
conn.close()