#MySQL_db.py
import mysql.connector
from mysql.connector import Error

class MySQL_db():

    def __init__(self):
        pass

    def connect(self):
        """ Connect to MySQL database """
        try:
            conn = mysql.connector.connect(host='localhost',
                                           database='aqms_db',
                                           user='root',
                                           password='panda2016')
            if conn.is_connected():
                print('Connected to MySQL database')
                return conn

        except Error as e:
            print(e)

        finally:
            conn.close()


    def insert_frame(self,connection, frameID, sensorName,sensorValue,timeStamp):
        query = "INSERT INTO books(frameID,sensorName,sensorValue,sensorTimeStamp) " \
                "VALUES(%d,%s,%d,%d)"
        args = (frameID,sensorName,sensorValue,timeStamp)

        try:
            conn = connection
            cursor = conn.cursor()
            cursor.execute(query, args)

            if cursor.lastrowid:
                print('last insert id', cursor.lastrowid)
                return cursor.lastrowid
            else:
                print('last insert id not found')

            conn.commit()
        except Error as error:
            print(error)

        finally:
            cursor.close()
            conn.close()
