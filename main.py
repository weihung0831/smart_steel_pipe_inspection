import time
import sys

sys.path.append("./backend/")
from backend import ModbusCom

IP_ADDRESS = "192.168.3.5"
UP_STATE = 1
DOWN_STATE = 0
PLC_INPUT = [i for i in range(0, 16)]


def handle_stopper_cyl(modbus, plc_input, state):
    return modbus.set_modbus_output_state(
        state, modbus.read_modbus_input_state(plc_input)
    )


def main():
    modbus = ModbusCom(IP_ADDRESS)

    try:
        while True:
            handle_stopper_cyl(modbus, PLC_INPUT[8], UP_STATE)
            handle_stopper_cyl(modbus, PLC_INPUT[9], DOWN_STATE)

    except KeyboardInterrupt:
        modbus.clear_output()
        modbus.disconnect()
        print("Disconnected")


if __name__ == "__main__":
    main()
