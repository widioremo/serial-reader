#test_readSerial.py
import readSerial
#testing readSerial
#the following code was used to write frameParser.py
#refer to frameParser.py for explanations
ser = readSerial.readSerial()
portsList = ser.getPorts()
port=""
for item in portsList:
    print(item)
    port = item

session = ser.openSerial(port)
frame1 = ser.readSerial()
print("frame1")
# print(next(frame1))

frameString = '' .join(next(frame1))
frameString = frameString.strip("[")
frameString = frameString.strip("]")

list = frameString.split(":")

print("list")
print(list)

print("frameid" + str(list[0]))
print("sensorName" + str(list[1]))
print("sensorValue" + str(list[2]))
print("Timestamp (ms)" + str(list[3]))
print(list)



frame2 = ser.readSerial()
print("frame2")
print(next(frame2))