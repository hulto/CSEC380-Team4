#import initdb as db
import hashlib
from flask_login import login_required, current_user, login_manager, LoginManager


from .initdb import User, session


def load_user(userid):
    try:
        print("Login manager managing")
        print(session.query(User).filter(User.id == userid).first())
        print("Yoinks")
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
    tmp = query.filter(User.uname==username).one()

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

## TESTING
if __name__ == "__main__":
    print(check_password('hulto', 'password123'))