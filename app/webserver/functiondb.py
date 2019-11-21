#import initdb as db
import hashlib
from flask_login import login_required, current_user, login_manager, LoginManager
from datetime import datetime

from .initdb import User, session, Video


def load_user(userid):
    try:
        return session.query(User).filter(User.id == userid).first()
    except Exception as e :
        return None


"""
Given a username and a password check it against the database
"""
def check_password(username, password):
    print("check_password(%s, %s)" % (username, password))
    res = None
    query = session.query(User)
    try:
        tmp = query.filter(User.uname==username).one()
    except Exception as e:
        print("check_password failed")
        return None

    real_password = tmp.passwd
    check_password = hashlib.sha512(password.encode()).hexdigest()
    if real_password == check_password:
        res = tmp

    return res

"""
Get all the users in the database and return their orm objects in a list
"""
def get_all_users():
    query = db.session.query(db.User)
    instance = query.all()

    res = []
    for i in instance:
        res.append(i)

    return res

def add_video(userid, path, title, desc):
    newvid = Video(title=title, content=path, description=desc, timestamp=datetime.utcnow(), owner=userid, views=0)
    print("Adding video")
    session.add(newvid)
    session.commit()

def get_all_videos():
    videos = session.query(Video).all()
    return videos

## TESTING
if __name__ == "__main__":
    print(check_password('hulto', 'password123'))