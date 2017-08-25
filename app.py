from flask import Flask, flash, redirect, render_template, request, session, abort, send_file, send_from_directory
from datetime import datetime
import time
import json


app = Flask(__name__)

# URL routing
## root directory:  /
@app.route("/")
def render_index():
    return render_template(
        'Index.html')

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
            
# app starts from here
if __name__ == "__main__":
    # record tool log for tracking the system
    app.run(host='0.0.0.0', port=int(sys.argv[1]))
    # close log file after finish
    log_file.close()