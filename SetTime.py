import serial.tools.list_ports

def flush_serial():
    Serial.flushInput()
    Serial.flushOutput()

ports = serial.tools.list_ports.comports()
PortCount = 0

print("SetTime - CMD")

for port in ports:
    print(str(PortCount) + ": " + port.device)
    PortCount += 1

Count = int(input("\nChoose: "))

print("connect to: " + ports[Count].device)
Serial = serial.Serial(ports[Count].device)


while True:

    Timeinput = input("Time in ms: ")

    Serial.write(Timeinput.encode())
    flush_serial()

    print(Serial.readline().decode().replace('\n',''))
    print(Serial.readline().decode().replace('\n',''))

    if input("Again? [y][n]") == "y":
        continue
    else:
        break

    flush_serial()


