import sqlite3
from backend.app.db.base import init_db,engine

print(engine.url)
'''
init_db()
print("Database initialized with all tables.")


db_path = "C:/Users/andrew/Desktop/aarn/backend/app.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute("SELECT paper_id, title FROM paper")
rows = cursor.fetchall()

print("Saved papers:")
for r in rows:
    print(r)

conn.close()
'''