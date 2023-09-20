import time
import sys

sys.path.append("../backend/")
from backend import ModbusCom, LoggerSetup

ip = "192.168.3.5"
modbus = ModbusCom(ip)

start_time = None

red_light = 0
orange_light = 1
green_light = 2

try:
    while True:
        if modbus.read_modbus_input_state(8):
            modbus.set_modbus_output_state(green_light, True)
        else:
            modbus.set_modbus_output_state(green_light, False)

        if modbus.read_modbus_input_state(9):
            if start_time == None:
                start_time = time.time()
            elif time.time() - start_time >= 0.5:
                modbus.set_modbus_output_state(orange_light, True)
        else:
            start_time = None
            modbus.set_modbus_output_state(orange_light, False)

except KeyboardInterrupt:
    modbus.clear_output()
    modbus.disconnect()
    print("Disconnected")
