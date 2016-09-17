import sqlite3
import json
from flask import Flask, g, request

api = Flask(__name__)
api.config.from_object(__name__)

@api.route('/test')
def test():
    l=["hello","world"]
    return str(l)

if "__main__" == __name__:
    api.run()

                     
