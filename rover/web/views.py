from rover.web import web
from flask import render_template

@web.route('/')
@web.route('/index')
def index():
    return render_template('index.html')
