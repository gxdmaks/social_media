from fastapi import FastAPI
from database import base, engine

# Создание таблицы в базе данных
base.metadata.create_all(bind=engine)



app = FastAPI()

from api.comments_api import comments
from api.hashtag_api import hashtag
from api.photo_api import photos
from api.posts_api import posts
from api.users_api import users
