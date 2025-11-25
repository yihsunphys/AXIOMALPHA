from sqlmodel import SQLModel, create_engine, Session
from sqlalchemy.orm import sessionmaker
from ..config import DATABASE_URL

connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}
engine = create_engine(DATABASE_URL, echo=True, connect_args=connect_args)

# Create a SessionLocal factory with expire_on_commit=False
SessionLocal = sessionmaker(
    bind=engine,
    class_=Session,
    autoflush=False,
    autocommit=False,
    expire_on_commit=False,   # <<< FIX HERE
)


def init_db():
    SQLModel.metadata.create_all(engine)


def get_session():
    with SessionLocal() as session:
        yield session
