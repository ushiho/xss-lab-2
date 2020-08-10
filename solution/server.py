#!/usr/bin/python3
from flask import Flask, request, url_for, render_template, redirect
from flask import Blueprint
from datetime import datetime
import sqlite3, os

app = Flask(__name__, template_folder='.', static_url_path='/static')

comments = [] # This is our database of messages

@app.route('/', methods=['GET', 'POST'])
def xss():
    global comments

    if request.method == 'GET':
        return render_template("index.html", comments=comments)
    else:
        print("hello")
        content = html_decode(request.form['content'])
        current = datetime.now().strftime('%A %B %d %Y %H:%M:%S')
        comments.append({
            'content': content,
            'saved_at': current
        })
        print("Records created successfully")

        return redirect('/')

@app.route('/clear')
def clear():
    global comments
    comments = []
    return redirect('/')

def html_decode(message):
    """
    Returns the ASCII decoded version of the given HTML string. This does
    NOT remove normal HTML tags like <p>.
    """
    decoded = ""
    htmlCodes = (
            ("'", '&#39;'),
            ('"', '&quot;'),
            ('>', '&gt;'),
            ('<', '&lt;'),
            ('&', '&amp;')
        )
    for char in message:
      for code in htmlCodes:
        if char in code:
          char = char.replace(char, code[1])
      decoded += char
    print("decoded string is", decoded)
    return decoded

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5000)