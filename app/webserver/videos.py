from flask import Blueprint, render_template, request, url_for, redirect, flash
from flask_login import login_user, login_manager, logout_user, current_user
from webserver import functiondb as db
from werkzeug.utils import secure_filename
from os.path import join as ospathjoin
videos = Blueprint('videos', 'videos', template_folder='webserver/templates')


@videos.route('/upload',methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            print("No file part")
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            file.save(ospathjoin("/tmp/", filename))
            return redirect('/')
    return render_template('upload.html')
    
@videos.route('/delete', methods=['POST'])
def delete():
    video_id = request.form['id']
    return render_template('/profile')
