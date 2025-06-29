import serial, time

PORT = '/dev/ttyUSB0'
BAUD = 256000
MOVE_CMD = bytes.fromhex('A50000000001')
READ_CMD = bytes.fromhex('A560')

def main():

    ser = serial.Serial(PORT, BAUD, timeout=1)
    time.sleep(1)
    print(f"Connected to LiDAR on {PORT} at {BAUD} baud.")
    ser.write(MOVE_CMD)
    ser.write(READ_CMD) 
    print("LiDAR spinning... Reading raw data")

    try:
        while True:
            data = ser.read(64)  # read a chunk
            print(data)           # binary dump
    except KeyboardInterrupt:
        ser.close()
        print("\nStopped reading.")
        
if __name__ == '__main__':
    main()
