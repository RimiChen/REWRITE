import sys
import os
from flask import Flask, flash, redirect, render_template, request, session, abort, send_file, send_from_directory
from datetime import datetime
import time
import json
from extract_demo import *

app = Flask(__name__)

# URL routing
## root directory:  /
@app.route("/")
def render_index():
    return render_template(
        'Index.html')

@app.route("/story_editing")
def render_story_editing_page():
    return render_template(
        'story_editing.html')
    
# root folder path
@app.route("/<path:path>")
def root_folder_file(path):
    return send_from_directory('/', path)

# story file path
@app.route("/Storys/<path:path>")
def send_story_file(path):
    return send_from_directory('Storys', path)    
    
# image file path
@app.route("/Materials/<path:path>")
def send_image_file(path):
    return send_from_directory('Materials', path)

'''
post functions
'''
@app.route('/post_rensa', methods = ['POST'])
def get_post_rensa():
    jsdata = request.form['javascript_data']
    #print("RENSA: "+str(jsdata))
    rensa_test(jsdata)
    return jsdata 

# app starts from here
if __name__ == "__main__":
    # record tool log for tracking the system
    app.run(host='0.0.0.0', port=int(sys.argv[1]))



