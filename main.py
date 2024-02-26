import sqlite3

# Database Connection
conn = sqlite3.connect('orders.db')

# Cursor Object
cur = conn.cursor()

# Create Table if none exists
cur.execute("""CREATE TABLE IF NOT EXISTS recorder(
            recorder_id INT PRIMARY KEY,
            month DATE,
            day INT,
            year INT,
            hours REAL,
            aldi TEXT,
            afton TEXT);
""")

conn.commit()