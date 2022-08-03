
import io
import serial



ser = serial.Serial("/dev/ttyUSB2", 115200, timeout=1)
# sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser))
ser.write(b'AT+CMGS="865841107"\r')
ser.write(b'\r')
ser.write(b'TEKSTAssss\x1a\r')






# sio.flush() # it is buffering. required to get the data out *n
    
at_value = ser.readlines()

# respons = at_value[-1].strip(".\n")
print(type(at_value))