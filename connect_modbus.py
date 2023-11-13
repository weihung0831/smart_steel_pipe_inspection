from pyModbusTCP.client import ModbusClient


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

    def connect(self):
        self.client.open()

    def stop(self):
        self.client.close()
