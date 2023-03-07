#!/usr/bin/python3
''' Start a Flask web aplication '''
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def greeting():
    ''' Display a message '''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def greeting_hbnb():
    ''' Display a 'HBNB' '''
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def variable_text(text):
    ''' Display 'C' followed by the value of text'''
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/', strict_slashes=False, defaults={'text': 'is cool'})
@app.route('/python/<text>', strict_slashes=False)
def variable_text_default(text):
    '''
    Display 'Python' followed by the value of text
    '''
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def only_int(n):
    ''' Display is a number '''
    return '{} is a number'.format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
