import sqlite3
import json
from flask import Flask, g, request, render_template

DATABASE = 'shetter.db'
DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

@app.route('/test')
def test():
    l=["hello","world"]
    return str(l)

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
    return render_template('profile.html',prof=prof)
    
@app.route('/search',methods=["POST"])
def search():
    data=[]
    date = request.form["date"]
    start_hour = request.form["start_hour"]
    end_hour = request.form["end_hour"]
    
    sql = 'select id from schedules where date = {0} and ({1} <= start_hour and {2} >= end_hour);'.format(date, start_hour, end_hour)
    cur = g.db.execute(sql)
    result_ids = [record[0] for record in cur.fetchall()]
    
    sql = 'select * from profile where id in ('
    place_holder = '?,'*len(result_ids)
    sql = sql + place_holder[:-1] + ')'
    cur = g.db.execute(sql, result_ids)
    for row in cur.fetchall():
        prof={}
        prof["id"] = row[0]
        prof["name"] = row[1]
        prof["address"] = row[2]
        prof["lat"] = row[3]
        prof["lng"] = row[4]
        data.append(prof)
        
    return json.dumps(data)

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    g.db.close()

if "__main__" == __name__:
    app.run()
                     
