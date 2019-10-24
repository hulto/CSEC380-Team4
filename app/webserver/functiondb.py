import initdb as db
import hashlib

"""
Given a username and a password check it against the database
"""
def check_password(username, password):
    res = False
    query = db.session.query(db.User)
    query = query.filter(db.User.uname==username).one()

    real_password = query.passwd
    check_password = hashlib.sha512(password.encode()).hexdigest()
    if real_password == check_password:
        res = True

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