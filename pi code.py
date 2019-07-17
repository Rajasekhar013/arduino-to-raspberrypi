int_encode = b'2'
float_encode = b'42.3'
string1 = "Hello!"
string1_encode = string1.encode()
int1 = 5
int1_encode = b'%d' %int1
import serial
ser = serial.Serial('/dev/ttyUSB0', 9600)
ser.write(b'3')
ser.write(b'5')
ser.write(b'7')
