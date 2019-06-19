import serial

ser = serial.Serial(
    port='/dev/ttyAMA0',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)

counter=0

print("Serial is open: " + str(ser.isOpen()))
print("Now Writing")
ser.write(b'This is a test')
print("Did write, now read")
x=ser.readline()
print("got '" + str(x) + "'" )
ser.close()
