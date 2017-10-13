#SqliteAdapter.py
import sqlite3
import datetime

class SqliteAdapter():

    def __init__(self):
        pass

    def connect(self):
        con = sqlite3.connect('data/aqms_db')
        return con
    def store(self, frameID, sensorName, sensorValue, sensorTimeStamp):
        date = datetime.datetime.now()
        con = self.connect()
        cursor =  con.cursor()
        cursor.execute('''INSERT INTO sensorValues(frameID,sensorName,sensorValue,timeStamp,date)
                          VALUES(?,?,?,?,?)''',(frameID,sensorName, sensorValue,sensorTimeStamp,date))
        lastrowid = con.commit()
        self.close(con)

        return lastrowid

    def get_all(self):
        pass

    def close(self,db):
        db.close()
