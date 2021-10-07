from app import app
from flask import render_template
from flask import request, redirect, flash, url_for
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = 'static\img'
ALLOWED_EXTENSIONS = set(['csv', 'xml', 'xlsm'])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/howto")
def about():
    return render_template("howto.html")

#C:\Users\codyk\Documents\Avionics Solutions\FastWire\app\static\img
#app.config["IMAGE_UPLOADS"] = "/C:/Users/codyk/Documents/Avionics Solutions/FastWire/app/static/img/uploads"

@app.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('download_file', name=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''


# REFERENCE
# @app.route("/upload", methods=["GET", "POST"])
# def upload():
#     def upload():

#         if request.method == "POST":

#             if request.files:

#                 image = request.files["image"]

#                 image.save(os.path.join(app.config["IMAGE_UPLOADS"], image.filename))

#                 print("Image saved")

#                 return redirect(request.url)

#     return render_template("upload.html")

# stackoverflow template 
# @app.route('/upload/',methods = ['GET','POST'])
# def upload_file():
#     if request.method =='POST':
#         file = request.files['file[]']
#         if file:
#             filename = secure_filename(file.filename)
#             file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
#             return
#     return render_template('upload.html')
