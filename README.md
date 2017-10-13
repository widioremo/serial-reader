# serial-reader

#Competed in June 2017


This applications were my part of my final year project for my Degree in Computer Technology (JKUAT).
The Arduino code is not included in this repo, although I will tru and upload it ASAP


#The Project


I created a wireless sensor network for monitoring the air with gas sensors arduino and XBee series 2c. 

The data was then visualised on a web page with chart.js(I think) or C3.js.

The Challenge was to visualize the data in real time. I managed to do this with generators in python.

src/readSerial.py is a small server which listens to the serial port on the computer and 
receives the sensor data sent by the arduino.

src/frameParser.py parsed the data stream as a frame and sent it to an sqlite database.

 I use flask framework to build the web app for visualizing.
 
 
 #Improvement
 
 
 There is a lot of space for improvement
 I realise my structure and quality of code needs to improve. 


