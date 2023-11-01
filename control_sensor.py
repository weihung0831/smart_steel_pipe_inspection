import time
from PySide6.QtCore import QThread, Slot


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
    
def control_sensor(action, cyl_control):
    try:
        result = None
        if action == "up":
            result = cyl_control.up()
        elif action == "down":
            result = cyl_control.down()
        else:
            print("Invalid action")
            return False
        print(result)
        # time.sleep(10)
        cyl_control.off()
        return True
    except Exception as e:
        print(e)
        return False


class CylinderController(QThread):
    def __init__(self, parent=None, modbus=None):
        super(CylinderController, self).__init__(parent)
        self.threadactive = True
        self.modbus = modbus
        self.cyl_stopper_b = Actuator(
            self.modbus,
            up_output=0,
            down_output=1,
            up_input=8,
            down_input=9,
            wait_time=3,
        )

    def control_cyl_stopper_a_up(self):
        if self.modbus.read_modbus_input_state(10):
            self.modbus.set_modbus_output_state(10, True)
        return control_sensor("up", self.cyl_stopper_b)

    def control_cyl_stopper_a_down(self):
        return control_sensor("down", self.cyl_stopper_b)

    @Slot()
    def run(self):
        while self.threadactive:
            QThread.msleep(100)

    def stop_thread(self):
        self.threadactive = False
        self.quit()
        self.wait()
        self.deleteLater()