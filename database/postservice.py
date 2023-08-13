from database.models import UserPost, Hashtag, Comments, PostPhoto

from database import get_db

def show_all_post_db(main_text, reg_data, post_id: int = 0):
    db = next(get_db())
    if post_id == 0:
        get_all_post = db.query(UserPost).filter_by(main_text=main_text, reg_data=reg_data).all()
        return get_all_post
    elif post_id == 1:
        user_post = db.query(UserPost).filter_by(post_id=post_id).all()
        return user_post

def change_post_db(new_text, post_id):
    db = next(get_db())
    edit_post = db.query(UserPost).filter_by(post_id=post_id, main_text=new_text).first()
    return edit_post

def delete_post_db(post_id):
    db = next(get_db())
    delete_exact_post = db.query(UserPost).filter_by(post_id=post_id).first()
    db.delete(delete_exact_post)
    db.commit()
    return delete_exact_post

### COMMENT ###
def get_exact_post_comments_db(post_id):
    db = next(get_db())
    all_comment = db.query(Comments).filter_by(post_id=post_id).all()
    return all_comment

def public_comment_db(post_id, user_id, text, reg_date):
    db = next(get_db())
    public_comm = Comments(post_id=post_id, user_id=user_id, text=text, reg_date=reg_date)
    db.add(public_comm)
    db.commit()
    return public_comm

def change_exact_user_comment_db(comment_id, new_comment_text):
    db = next(get_db())
    edit_comm = db.query(Comments).filter_by(id=comment_id, text=new_comment_text).first()
    db.commit()
    return edit_comm

def delete_exact_user_comment_db(comment_id):
    db = next(get_db())
    exact = db.query(Comments).filter_by(id=comment_id).first()
    db.delete(exact)
    db.commit()
    return exact

### HASHTAG ###
def get_some_hashtags_db(size: int=20):
    db = next(get_db())
    get_hashtag = db.query(Hashtag).all()
    return get_hashtag[:size]

def get_exact_hashtag_db(hashtag_name):
    db = next(get_db())
    get_ex_hashtag = db.query(Hashtag).filter_by(hashtag_name=hashtag_name).first()
    db.commit()
    return get_ex_hashtag

### PHOTO ###