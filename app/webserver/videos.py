from flask import Blueprint, render_template, request, url_for, redirect, flash
from flask_login import login_user, login_manager, logout_user, current_user
from webserver import functiondb as db


videos = Blueprint('videos', 'videos', template_folder='webserver/templates')


@videos.route('/upload')
def upload():
    if(not current_user.is_authenticated):
        return redirect('/login')
    return render_template('upload.html')
