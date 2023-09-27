import sys

sys.path.append("./backend/")
from backend import *
from configparser import ConfigParser

config = ConfigParser()
config.read("./config.ini")

try:
    IP_ADDRESS = config["Settings"]["IP_ADDRESS"]
    ON_STATE = int(config["Settings"]["ON_STATE"])
    OFF_STATE = int(config["Settings"]["OFF_STATE"])
    PLC_INPUT = [i for i in range(0, 16)]
except KeyError:
    print("Error: Missing configuration in config.ini")
    sys.exit(1)


class Cylinder:
    def __init__(self, modbus, plc_input):
        self.modbus = modbus
        self.plc_input = plc_input

    def handle(self, state):
        return self.modbus.set_modbus_output_state(
            state, self.modbus.read_modbus_input_state(self.plc_input)
        )

    def unhandle(self, state):
        return self.modbus.set_modbus_output_state(state, False)


@LoggerSetup().log_execution
class Actuator(Cylinder):
    def on(self):
        return self.handle(ON_STATE)

    def off(self):
        return self.unhandle(OFF_STATE)


@LoggerSetup().log_execution
class ControlBlock:
    def __init__(self, modbus):
        self.modbus = modbus

    def create_actuators(self, indices):
        return [Actuator(self.modbus, PLC_INPUT[i]) for i in indices]

    def a_block(self):
        actuators = self.create_actuators([0, 1, 2, 3, 6, 7, 4, 5, 8])
        # TODO: Add control script for a_block

    def b_block(self):
        actuators = self.create_actuators([0, 1, 2, 3, 6, 7, 4, 5])
        # TODO: Add control script for b_block

    def c_block(self):
        actuators = self.create_actuators([0, 1, 2, 3, 6, 7, 4, 5])
        # TODO: Add control script for c_block

    # def test_block(self):
    #     actuators = self.create_actuators([i for i in range(0, 16)])
    #     actuators[8].on()
    #     actuators[9].off()


@LoggerSetup().log_execution
def main():
    modbus = ModbusCom(IP_ADDRESS)

    try:
        while True:
            ControlBlock(modbus).a_block()
            ControlBlock(modbus).b_block()
            ControlBlock(modbus).c_block()
            # ControlBlock(modbus).test_block()
    except KeyboardInterrupt:
        modbus.clear_output()
        modbus.disconnect()
        print("Disconnected")


if __name__ == "__main__":
    main()
