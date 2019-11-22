from flask import Blueprint, render_template, request, url_for, redirect, flash
from flask_login import login_user, login_manager, logout_user, current_user
from webserver import functiondb as db
from werkzeug.utils import secure_filename
from os.path import join as ospathjoin
from os.path import exists as ospathexists
from os import mkdir
import os
import hashlib
from webserver.functiondb import add_video

hasher = hashlib.md5()

videos = Blueprint('videos', 'videos', template_folder='webserver/templates')

UPLOAD_FOLDER = "./app/webserver/static/uploads/"

@videos.route('/upload',methods=['GET', 'POST'])
def upload():
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
            print(os.getcwd())
            filename = secure_filename(file.filename)
            print("User %s uploaded file %s" % (current_user.get_id(), filename))
            if(not ospathexists(UPLOAD_FOLDER+str(current_user.get_id()))):
                print("Making dir %s" % (str(UPLOAD_FOLDER+str(current_user.get_id()))))
                mkdir(UPLOAD_FOLDER+str(current_user.get_id()))
            file.save(ospathjoin(UPLOAD_FOLDER+str(current_user.get_id()), filename))

            add_video(current_user.get_id(), ospathjoin(UPLOAD_FOLDER+str(current_user.get_id()), filename), filename, "Lorem Ipsum")
            return redirect('/')
    username = None
    if current_user.is_authenticated:
        username = current_user.get_uname()
    return render_template('upload.html', user=username)
    
@videos.route('/delete/<id>', methods=['GET'])
def delete(id):
    print("Trying to delete video %d" % (int(id)))
    if( db.is_owner(id, current_user.id) ):
        db.delete_video(id)
    return redirect('/')



@videos.route('/watch/<id>')
def watch(id):
    print(id)
    video = db.get_video(int(id))
    vid = {}
    vid['title'] = video.title
    vid['content'] = "/" + "/".join(video.content.split('/')[3:])
    vid['id'] = video.id
    print("Video title %s is at %s" % (video.title, video.content))
    username = None
    if current_user.is_authenticated:
        username = current_user.get_uname()
    return render_template('watch.html', vid=vid, user=username)