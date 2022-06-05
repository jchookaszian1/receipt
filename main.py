import json
from fileinput import filename

import PIL
import cv2
import numpy
from PIL import Image
from flask import Flask, request, flash, url_for
from werkzeug.utils import redirect

from pytesseract_main import read_image

app = Flask(__name__)
app.secret_key = 'super secret key'

i = 0


@app.route("/upload", methods=["POST"])
def hello_world():
    global i
    print(request.method)
    if request.method == 'POST':
        filestr = request.files['files'].read()
        # convert string data to numpy array
        npimg = numpy.fromstring(filestr, numpy.uint8)
        # convert numpy array to image
        img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)
        cv2.imwrite('C:\\Users\\JOE\\source\\repos\\receipt-parser\\test\\test' + str(i) + ".png", img)
        read_image(img)

        i = i + 1
        return 'file uploaded successfully'

    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}
