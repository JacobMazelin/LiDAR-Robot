import serial, time

PORT = '/dev/ttyUSB0'
BAUD = 115200
START_CMD = bytes.fromhex('A50000000001')

def main():
    print("Starting LIDAR...")
    ser = serial.Serial(port = PORT, baudrate= BAUD, timeout=1)
    time.sleep(5)

    ser.write(START_CMD)
    print("Sent start command; waiting for motor...")

    time.sleep(5)
    resp = ser.read(ser.in_waiting or 1)
    print("Response:", resp)

    ser.close()

if __name__ == '__main__':
    main()
