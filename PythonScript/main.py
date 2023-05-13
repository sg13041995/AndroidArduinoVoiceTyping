""" 
+++++++++++++++++++++++++++++++++++++++++++++++++++++
Module Imports
+++++++++++++++++++++++++++++++++++++++++++++++++++++ 
"""
from serial import Serial
from pyautogui import typewrite

""" 
+++++++++++++++++++++++++++++++++++++++++++++++++++++
Body
+++++++++++++++++++++++++++++++++++++++++++++++++++++ 
"""

port = "COM4"
baudrate = 9600
arduino_port = None
arduino_baudrate = None
termination_code = "999"

arduino_port = input(">>> Enter the arduino port (Example: COM4)\n>>>>")
if (arduino_port):
    port = arduino_port
print(f">>>Arduino port is set to: {port}")

try:
    arduino_baudrate = input(">>> Enter the arduino baudrate (Example: 9600)\n>>>>")
    if (arduino_baudrate):
        baudrate = int(arduino_baudrate)
except Exception:
    print("Something wen't wrong.\nProgram will exit\n")
    exit(0)
print(f">>>Arduino baudrate is set to: {baudrate}")

print(">>>Default Termination Code is: '999'")

try:
    ser = Serial(port, baudrate)
except Exception:
    print(">>>Something Went Wrong!!!")
    print(">>>Program will be terminated")
    input("Enter a key to exit...")
    exit()

while True:
    # Read a line of data from the serial port
    line = ser.readline().decode().strip()

    if (line == "999"):
        print("Program Terminated")
        input()
        exit()

    if line:
        typewrite(line)
        typewrite(" ")
