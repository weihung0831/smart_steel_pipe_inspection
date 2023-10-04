import functools
import logging
import sys
from configparser import ConfigParser
from pathlib import Path

from pyModbusTCP.client import ModbusClient

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


class LoggerSetup:
    def __init__(self, log_path: str = "../logs/app.log"):
        self.log_path = log_path
        self._setup_directory()
        self._setup_logging()

    def _setup_directory(self):
        directory_path = Path(self.log_path).parent
        directory_path.mkdir(parents=True, exist_ok=True)

    def _setup_logging(self):
        # Setup logging configuration
        logging.basicConfig(
            filename=self.log_path,
            level=logging.INFO,
            format="[%(asctime)s] [%(levelname)s] %(message)s (%(filename)s:%(lineno)d)",
            datefmt="%Y-%m-%d %H:%M:%S",
        )

    @staticmethod
    def log_execution(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                logging.info(f"Starting {func.__name__} execution")
                return func(*args, **kwargs)
            except KeyboardInterrupt as e:
                logging.exception(e)
                raise e
            except Exception as e:
                logging.exception(e)
                raise e
            finally:
                logging.info(f"Finished {func.__name__} execution")

        return wrapper


"""
The `ModbusCom` class is a Python class that provides methods for interacting with a Modbus communication protocol, 
including setting output states, clearing outputs, reading input states, and disconnecting from the Modbus client.
"""


@LoggerSetup().log_execution
class ModbusCom:
    def __init__(self, ip):
        self.ip = ip
        self.client = ModbusClient(self.ip, 502, unit_id=1)
        self.client.open()
        self.current_state = 0

    def set_modbus_output_state(self, value, activate=True):
        reverse_value = 0
        if self.client.is_open:
            if 0 <= value < 8:
                reverse_value = value + 8
            elif 8 <= value < 16:
                reverse_value = value - 8
            else:
                print("Value out of range")
                return False

            if activate:
                self.current_state |= 1 << reverse_value
                # print(self.current_state)
            else:
                self.current_state &= ~(1 << reverse_value)
                # print(self.current_state)

            # print(self.client.write_single_register(0, self.current_state))
            return self.client.write_single_register(0, self.current_state)
        else:
            print("Client not connected")
        return False

    def clear_output(self):
        if self.client.is_open:
            return self.client.write_single_register(0, 0)
        else:
            print("Client not open")
            return False

    def read_modbus_input_state(self, value):
        if self.client.is_open:
            register_value = self.client.read_input_registers(0, 1)[0]
            # to 16 bit binary
            binary_representation = bin(register_value)[2:].zfill(16)
            # to list
            binary_list = list(binary_representation)
            upper_half, lower_half = binary_list[:8], binary_list[8:]
            upper_half.reverse()
            lower_half.reverse()
            combined_list = upper_half + lower_half
            state = [int(bit) for bit in combined_list]
            # print(boolean_state[value])
            # boolean_state = [bool(int(bit)) for bit in combined_list]
            # return boolean_state[value]
            return state[value]
        else:
            print("Client not open")
            return None

    def disconnect(self):
        self.client.close()


# The `Cylinder` class handles the state of a cylinder using Modbus communication.
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
# The Actuator class is a subclass of the Cylinder class and has methods to turn on and off the actuator.
class Actuator(Cylinder):
    def up(self):
        return self.handle(ON_STATE)

    def off(self):
        return self.unhandle(OFF_STATE)
    
    def down(self):
        return self.handle(OFF_STATE)


@LoggerSetup().log_execution
# The ControlBlock class creates actuators and defines control scripts for different blocks.
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

    def action_down(self):
        actuators = self.create_actuators([i for i in range(0, 16)])
        actuators[8].down()
        return self.modbus.read_modbus_input_state(PLC_INPUT[8])
        # actuators[9].on()
