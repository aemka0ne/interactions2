import serial


ser= serial.Serial("COM3", 9600)
serin=ser.read()
ser.write(b'1')
while ser.read()== '1':
    ser.read()
ser.close()

