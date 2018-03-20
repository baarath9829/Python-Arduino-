import serial

arduino =serial.Serial('com3',9600)
while True:
    if arduino.inWaiting()==0:
        pass
    else:
        print arduino.readline()
        
