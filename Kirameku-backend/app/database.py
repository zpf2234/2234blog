from sqlmodel import SQLModel, create_engine, Session
from app.config import DATABASE_URL

is_sqlite = DATABASE_URL.startswith("sqlite")
connect_args = {"check_same_thread": False} if is_sqlite else {}
pool_kwargs = {} if is_sqlite else {"pool_pre_ping": True}

engine = create_engine(DATABASE_URL, echo=False, connect_args=connect_args, **pool_kwargs)


def init_db():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session

