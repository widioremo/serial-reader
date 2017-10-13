#frameParser.py
import readSerial
from SqliteAdapter import SqliteAdapter


#starts a serial session
#assumes only one device is connected to the usb ports
#if
def startSession(serial_port=" "):

    #if no port is passed, assume one port is connected
    #search for it
    if(serial_port==" "):
        ser = readSerial.readSerial()
        portsList = ser.getPorts()
        port = ""
    for item in portsList:
        print(item)
        port = item

    ser.openSerial(port)

    return ser

#parses a frame from a list of individual byte characters
#to a list of the actual values needed to store in the db
def parseFrame(session_obj):

    #readSerial is generator function
    #it returns an object that can be iterated to read
    #  the next value
    frame = session_obj.readSerial()
    print("frame1")
    # print(next(frame1))

    #we use next() to read the next value of the genetator object
    # i.e generator iterator
    #the list of chars is joined to a string with .join()
    #we then strip the start and end characters of the frame
    #and split the frame into a list of the values we need with split()

    frame_string = '' .join(next(frame))
    frame_string = frame_string.strip("[")
    frame_string = frame_string.strip("]")
    frame_data = frame_string.split(":")


    print("list")
    print(frame_data)
    return frame_data


#store frame to MYSQL
#pass list data type with the frame data
#frame data is frame id, sensor name, sensor value, sensor timestamp in milliseconds
def storeFrame(frame_data):
    if len(frame_data) > 0 :
        frame_id = int(str(frame_data[0]))
        sensor_name = str(frame_data[1])
        sensor_value = int(str(frame_data[2]))
        timestamp = int(str(frame_data[3]))
        db = SqliteAdapter()
        row_id = db.store(frame_id,sensor_name,sensor_value,timestamp)
        # insert frame returns ID of inserted row
        if(row_id):
            print("Suceessful insert of frame %d",row_id)
            return row_id

        #void return
        return None


#main function that runs when file is executed
def main():
    #start serial session
    session = startSession()

    #read serial data
    #read x frames
    x = 10
    i =0
    while(i <= x):
        frame_data = parseFrame(session)
        #store frame
        storeFrame(frame_data)



if __name__ == '__main__':
    main()