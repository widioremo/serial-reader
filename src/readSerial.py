#readSerial.py
import serial
import serial.tools.list_ports as PortInfo

class readSerial():



    def __init__(self):
        self.serialSession = None

    def getPorts(self):
        deviceList = []
        for item in PortInfo.comports():
            # print(item.device)
            deviceList.append(item.device)
        return deviceList

    def openSerial(self, device):
        print("opening port"+ device)
        self.serialSession = serial.Serial(device ,9600, timeout=1)

    def readSerial(self):
        print("reading serial")
        frameList = []
        while (self.serialSession.isOpen()):
            byte = self.serialSession.read()
            if (byte==b'['):
                while(byte != b']'):
                    print(str(byte))
                    frameList.append(byte.decode('utf8'))
                    byte = self.serialSession.read()
                frameList.append(byte.decode('utf8'))
                print("framelist" + str(len(frameList)))
                yield frameList

                #     serial.close()
                #     return frameList
        print("Serial is Unavailable")


    def closeSerial(self):

        self.serialSession.close()






