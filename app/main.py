from flask import render_template, Flask
from flask_login import login_required, current_user, login_manager, LoginManager

from webserver.auth import auth
from webserver import functiondb as db

app = Flask(__name__, template_folder='webserver/templates')
app.register_blueprint(auth)

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
    username = None
    if current_user.is_authenticated:
        username = current_user.get_uname()
    return render_template('index.html', user=username)

@app.route('/profile')
def profile():
    print("Profile is authed? %s" % (str(current_user.is_authenticated)))
    print(current_user.get_uname())
    return render_template('profile.html', name=current_user.get_uname())

if __name__ == "__main__":
    app.run(debug=True, port=9000)