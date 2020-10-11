from contextlib import contextmanager

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///db.db', convert_unicode=True)
session_factory = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


class SessionWrapper:
    def __init__(self):
        self._session_factory = session_factory
        self._session_handle = None

    @contextmanager
    def session(self):
        try:
            yield self._session
            self._session.commit()
        except:
            self._session.rollback()
            raise

    @property
    def _session(self):
        if self._session_handle is None:
            self._session_handle = self._session_factory()
        return self._session_handle

    def teardown(self):
        if self._session_handle is not None:
            self._session_handle.close()


Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False, unique=True)
    passwordhash = Column(String, nullable=False)


def init_db():
    Base.metadata.create_all(bind=engine)
