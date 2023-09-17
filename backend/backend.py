from pyModbusTCP.client import ModbusClient
import functools
import logging
from pathlib import Path


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


@LoggerSetup().log_execution
class ModbusCom:
    def __init__(self, ip, fake_data=False):
        self.ip = ip
        self.client = ModbusClient(self.ip, 502, unit_id=1)
        self.client.open()
        self.current_state = 0
        self.fake_data = fake_data

    def set_output_state(self, value, activate=True):
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

    def get_input_state(self, value):
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
            boolean_state = [bool(int(bit)) for bit in combined_list]
            return boolean_state[value]
        else:
            print("Client not open")
            return None

    def disconnect(self):
        self.client.close()
