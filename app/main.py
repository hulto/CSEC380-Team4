from flask import render_template, Flask
from flask_login import login_required, current_user, login_manager, LoginManager

from webserver.auth import auth
from webserver.videos import videos

from webserver import functiondb as db

import os

app = Flask(__name__, template_folder='webserver/templates', static_folder='webserver/static')
app.register_blueprint(auth)
app.register_blueprint(videos)

app.config['UPLOAD_FOLDER'] = "./app/webserver/static/uploads"

app.secret_key = 'UntilOneDayWhenTheFireNationAttacked'
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user_main(userid):
    try:
        return db.load_user(userid)
    except Exception as e :
        return None

@app.route('/')
def index():
    print(os.getcwd())
    username = None
    if current_user.is_authenticated:
        username = current_user.get_uname()
    vids = db.get_all_videos()
    return render_template('index.html', user=username, videos=vids)

@app.route('/profile')
def profile():
    print("Profile is authed? %s" % (str(current_user.is_authenticated)))
    print(current_user.get_uname())
    return render_template('profile.html', name=current_user.get_uname())


@app.route('/search/')
def search_plain():
    username = None
    if current_user.is_authenticated:
        username = current_user.get_uname()
    vids = db.get_all_videos()
    return render_template('index.html', user=username, videos=vids)


@app.route('/search/<term>')
def search(term):
    username = None
    if current_user.is_authenticated:
        username = current_user.get_uname()
    vids = db.search_video(term)
    return render_template('index.html', user=username, videos=vids)

@app.route('/search2/<term>')
def search2(term):
    username = None
    if current_user.is_authenticated:
        username = current_user.get_uname()
    vids = db.search_video2(term)
    return render_template('index.html', user=username, videos=vids)


if __name__ == "__main__":
    app.run(debug=True, port=9000, host='0.0.0.0')
