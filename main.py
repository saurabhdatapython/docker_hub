from wsgiref import simple_server
from flask import Flask, request, render_template
from flask import Response
from best_model_finder.tuner import Model_Finder
import os
from flask_cors import CORS, cross_origin

import json
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    file = open("sav.txt",'a+')
    message = "hi "
    obj  = Model_Finder(file,message)
    x = "path"
    y = "sath"
    obj.get_best_params_for_random_forest(x,y)

    return "flask app is running change"

port = int(os.getenv("PORT", 5000))
if __name__ == "__main__":
    host = '0.0.0.0'
    # port = 5000
    httpd = simple_server.make_server(host, port, app)
    # print("Serving on %s %d" % (host, port))
    httpd.serve_forever()
