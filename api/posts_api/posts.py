from api import app

@app.get('/api/post')
async def get_all_or_exact_post(post_id: int = 0):
    pass

@app.put('/api/post')
async def change_user_post(request):
    pass

@app.delete('/api/post')
async def delete_user_post():
    pass
