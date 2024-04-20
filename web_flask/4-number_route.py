#!/usr/bin/python3
"""
script starts Flask web app

listen on 0.0.0.0, port 5000

Routes:
        /: display "Hello HBNB!"
        /hbnb: display "HBNB"
        /c/<text>: display "C (text)"
        /python/(<text>): display "Python (text)"
        /number/<n>: display "n is a number" if n is an integer
"""

from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """display text"""
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """display text"""
    return "HBNB"


@app.route('/c/<text>')
def c(text):
    """display text"""
    return ("C {}".format(text.replace("_", " ")))


@app.route('/python/')
@app.route('/python/<text>')
def python(text="is cool"):
    """display text"""
    return ("Python {}".format(text.replace("_", " ")))


@app.route('/number/<int:n>')
def number(n):
    """display number"""
    return ("{} is a number".format(n))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
