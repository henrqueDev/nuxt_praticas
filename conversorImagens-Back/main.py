from flask import Flask
from flask_cors import CORS 

from flask import request, send_file
from werkzeug.utils import secure_filename
from PIL import Image
import os

app = Flask(__name__)
CORS(app)

app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000
app.config['UPLOAD_FOLDER'] = './uploads/'

@app.route('/')
def index():

    return 'Ola mundo'

@app.route('/converterImagemPng', methods = ['POST'])
def post():
        file = request.files['file']
        filename = secure_filename(file.filename)             

        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        im = Image.open(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        #filename =  "converted.png"
        #im.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return send_file(os.path.join(app.config['UPLOAD_FOLDER'], filename ), as_attachment=True)

if __name__ == '__main__':
    app.run()