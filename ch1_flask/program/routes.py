from program import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    return render_template('/index.html')

@app.route('/post')
def post():
    return render_template('/blog.html')

@app.route('/test')
def testing():
    return render_template('/testing.html')
