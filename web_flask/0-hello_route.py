#!/usr/bin/python3
''' Start a Flask web '''

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def greeting():
        ''' Display a message to user '''
            return 'Hello HBNB!'


        if __name__ == '__main__':
                app.run(host='0.0.0.0', port=5000)
