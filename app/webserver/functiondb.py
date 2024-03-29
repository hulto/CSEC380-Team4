#import initdb as db
import hashlib
from flask_login import login_required, current_user, login_manager, LoginManager
from datetime import datetime
from os import remove as os_rm
import subprocess
from .initdb import User, session, Video, engine


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

def add_user(first, user, password, role):
    newuser = User(fname=first,
                  uname=user,
                  passwd=hashlib.sha512(password.encode()).hexdigest(),
                  role=0)
    print("Adding user %s %s" % (user, password))
    session.add(newuser)
    session.commit()


def get_all_videos():
    videos = session.query(Video).all()
    return videos

def get_video(v_id):
    video = session.query(Video).filter_by(id = int(v_id)).one()
    return video

def is_owner(v_id, o_id):
    video = get_video(v_id)
    if(video.owner == o_id):
        return True
    return False

def delete_video(v_id):
    os_rm(session.query(Video).filter_by(id=v_id).one().content)
    session.query(Video).filter_by(id=v_id).delete()
    session.commit()

#Vulnerable version
def search_video(search_term):
    # result = session.execute(
    #         "SELECT * FROM video WHERE title LIKE '%s'" % (search_term)                # {"param":v_id}
    #     ) 
    # print(result.fetchall())
    # session.commit()
    # videos = result.fetchall()
    # videos = session.query(Video).filter(Videos.title="{}".format(search_term)).all()
    videos = session.query(Video).filter(Video.title.like("%%%s%%" % search_term))
    return videos

#Command injection 
# http://localhost:9000/search2/test*%22;%20ping%20-c%205%208.8.8.8;%20%22
def search_video2(search_term):
    result=subprocess.getoutput('find ./app/webserver/static/uploads/* -name "%s"' % (search_term))
    videos = []
    for i in result.split('\n'):
        v_title = i.split("/")[-1]
        v_user = i.split("/")[-2]
        newvid = Video(id=0, title=v_title, content=i, description="Lorem ipsum", timestamp=datetime.utcnow(), owner=v_user, views=0)
        videos.append(newvid)
    return videos

#Classic sqli http://localhost:9000/sqli/testvid1'%20OR%201=1;%20--
#Blind sqli http://localhost:9000/sqli/testvid';%20pg_sleep(5);%20--
def sqli(term):
    con = engine.connect()
    # rs = con.execute("SELECT * FROM video WHERE title LIKE '"+term+"'")
    qstr = "SELECT * FROM video WHERE title LIKE '"+term+"'"
    rs = con.execute(qstr)
    #print(rs)
    res = rs.fetchall()
    print(res)
    con.close()
    return res

## TESTING
if __name__ == "__main__":
    print(check_password('hulto', 'password123'))


'''
password123_hash = "bed4efa1d4fdbd954bd3705d6a2a78270ec9a52ecfbfb010c61862af5c76af1761ffeb1aef6aca1bf5d02b3781aa854fabd2b69c790de74e17ecfec3cb6ac4bf"
user_hulto = User(fname='Jack McKenna',
                  uname='hulto',
                  passwd=password123_hash,
                  role=0)

check_password = hashlib.sha512(password.encode()).hexdigest()
'''