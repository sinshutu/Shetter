import sqlite3
import json
from flask import Flask, g, request, render_template

DATABASE = 'shetter.db'

app = Flask(__name__)
app.config.from_object(__name__)

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

@app.route('/test')
def test():
    l=["hello","world"]
    return str(l)

@app.route('/test2')
def test2():
    d={"a":1,"b":"c"}
    return json.dumps(d)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profiles/<int:Id>')
def profile(Id):
    prof = {}
    sql = "select * from profile where id={0}".format(Id)
    cur = g.db.execute(sql)
    data = cur.fetchone()
    prof["id"] = data[0]
    prof["name"] = data[1]
    prof["address"] = data[2]
    prof["lat"] = data[3]
    prof["lng"] = data[4]
    return json.dumps(data)
    #return render_template('index.html',data=data)
    
@app.route('/search')
def search():
    return "search"

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    g.db.close()

if "__main__" == __name__:
    app.run()

                     
