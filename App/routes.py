from flask import Flask
from flask import render_template, url_for
from App import app


@app.route('/')
def index():
    return render_template('index.html')

