#!/usr/bin/python3

from flask import Flask, request, url_for, render_template, redirect
from flask import Blueprint

app = Flask(__name__, template_folder='.', static_url_path='/static')

@app.route('/')
def xss():
    return render_template("index.html")


if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True, port=5000)
