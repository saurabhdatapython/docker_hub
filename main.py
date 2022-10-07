#!/usr/bin/env python

from wsgiref import simple_server
from flask import Flask, request, render_template
from flask import Response
#from flask_cors import CORS, cross_origin
import os



app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def home():
    return "hi this is flask"


port = int(os.getenv("PORT", 5000))
if __name__ == "__main__":
    host = '0.0.0.0'
    # port = 5000
    httpd = simple_server.make_server(host, port, app)
    # print("Serving on %s %d" % (host, port))
    httpd.serve_forever()
