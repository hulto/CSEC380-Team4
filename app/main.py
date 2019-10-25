from flask import render_template, Flask
from flask_login import login_required, current_user

app = Flask(__name__)
# app = Blueprint('main', __name__, template_folder='webserver/templates')

@app.route('/')
def index():
    return render_template('template.html')


# @main.route('/profile')
# @login_required
# def profile():
#     return render_template('profile.html', name=current_user.name)

# app.register_blueprint(auth, url_prefix='/auth')

if __name__ == "__main__":
    app.run(debug=True, port=9000)