from flask import render_template, Flask
from flask_login import login_required, current_user

from webserver.auth import auth

app = Flask(__name__, template_folder='webserver/templates')
app.register_blueprint(auth)

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True, port=9000)