from api import app
from database.postservice import get_some_hashtags_db

# поулчить несколько хештегов


@app.get('/api/hashtag')
async def get_hashtags(size: int = 20, page: int = 1):
    pass
# получить фото из определеноого хештега
@app.get('/api/hashtag/<str:hashtag_name>')
async def get_hashtag(hashtag_name: str):
    if hashtag_name:
        exact_hashtag = get_some_hashtags_db(hashtag_name)
        return {'status': 1, 'message': exact_hashtag}
    return {'status': 0, 'message': 'неверные данные'}