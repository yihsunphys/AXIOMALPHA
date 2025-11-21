# check_db.py
from sqlmodel import Session, select, SQLModel, create_engine
from config import DATABASE_URL
from db.models import Paper
import json

# SQLite connect args
connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}
engine = create_engine(DATABASE_URL, echo=False, connect_args=connect_args)

# Ensure tables exist
SQLModel.metadata.create_all(engine)

# Start a session
with Session(engine) as session:
    stmt = select(Paper)
    papers = session.exec(stmt).all()

    if not papers:
        print("No papers found in the database.")
    else:
        print("Saved papers:")
        for p in papers:
            authors = json.loads(p.authors or "[]")
            print(f"{p.paper_id} — {p.title} — Authors: {', '.join(authors)} — Year: {p.year}")
