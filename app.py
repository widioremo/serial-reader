#app.py
from flask import Flask, render_template,request,g
import sqlite3
import json
import datetime

app = Flask(__name__)

#path to database
DATABASE = 'data/aqms_db'
#


#load the home page
@app.route("/")
def main():
    sensorData = get_data()
    # return render_template('index.html',xValues = sensorData['x'],
    #                                     yValues = sensorData['y'])


    return render_template('home.html',xValues = sensorData[0],
                                        yValues = sensorData[1])
    # return('Welcome')

#run suery function with sql to pull data
def get_data():
    query= '''SELECT * from sensorValues'''
    data = query_db(query)

    xValues=["x"]
    # xValues[0] = xValues[0].encode('ascii')
    yValues=["CO"]

    columnsList = []

    for dict in data:
        # strftime("%Y-%m-%d %H:%M")
        time = datetime.datetime.strptime(dict['date'],"%Y-%m-%d %H:%M:%S.%f")
        date = time.strftime("%Y-%m-%d %H:%M")
        xValues.append(date)
        yValues.append(dict['sensorValue'])


    columnsList = [xValues,yValues]

    print(columnsList)

    return columnsList



def connect_db():
    return sqlite3.connect(DATABASE)

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    if hasattr(g, 'db'):
        g.db.close()

#query database
def query_db(query, args=(), one=False):
    cur = g.db.execute(query, args)
    rv = [dict((cur.description[idx][0], value)
               for idx, value in enumerate(row)) for row in cur.fetchall()]
    return (rv[0] if rv else None) if one else rv



if __name__ == "__main__":
    app.run()


