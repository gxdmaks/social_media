from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:909411216MAx@localhost/social_media'
engine = create_engine(SQLALCHEMY_DATABASE_URI)
sessionlocal = sessionmaker(bind=engine)
base = declarative_base()

from database.models import *

def get_db():
    db = sessionlocal()
    try:
        yield db
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()