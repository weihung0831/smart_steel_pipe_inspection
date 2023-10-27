import functools
import logging
import time
from pathlib import Path

from pyModbusTCP.client import ModbusClient


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


class ModbusCom:
    def __init__(self, ip):
        self.ip = ip
        self.client = ModbusClient(self.ip, 502, unit_id=1, timeout=1)
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
            else:
                self.current_state &= ~(1 << reverse_value)

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
            # boolean_state = [bool(int(bit)) for bit in combined_list]
            # return boolean_state[value]
            return state[value]
        else:
            print("Client not open")
            return None

    def disconnect(self):
        self.client.close()


@LoggerSetup().log_execution
# The `Actuator` class represents an actuator that can be controlled using Modbus communication
# protocol, with methods to move the actuator up, down, and turn it off.
class Actuator:
    def __init__(
        self, modbus, up_output, down_output, up_input, down_input, wait_time=0.5
    ):
        self.modbus = modbus
        self.up_output = up_output
        self.down_output = down_output
        self.up_input = up_input
        self.down_input = down_input
        self.wait_time = wait_time

    def up(self):
        success = self.modbus.set_modbus_output_state(self.up_output, True)
        if success:
            check = self.check_success(self.up_input)
        return success and check

    def check_success(self, pin):
        start = time.perf_counter()
        success = False
        while True:
            sensor = self.modbus.read_modbus_input_state(pin)
            if sensor:
                success = True
                break
            if (time.perf_counter() - start) > self.wait_time:
                break
            time.sleep(self.wait_time / 10)
        return success

    def off(self):
        state = self.modbus.set_modbus_output_state(self.up_output, False)
        state &= self.modbus.set_modbus_output_state(self.down_output, False)
        return state

    def down(self):
        success = self.modbus.set_modbus_output_state(self.down_output, True)
        if success:
            check = self.check_success(self.down_input)
        return success and check
