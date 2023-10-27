import sys
from configparser import ConfigParser

from PySide6.QtCore import QThread, Slot

from backend import *

config = ConfigParser()
config.read("./config.ini")

try:
    UP_OUTPUT = int(config["Settings"]["UP_OUTPUT"])
    DOWN_OUTPUT = int(config["Settings"]["DOWN_OUTPUT"])
    CYL_STOPPER_B_UP = int(config["Settings"]["CYL_STOPPER_B_UP"])
    CYL_STOPPER_B_DOWN = int(config["Settings"]["CYL_STOPPER_B_DOWN"])
    WAIT_TIME = int(config["Settings"]["WAIT_TIME"])
except KeyError:
    print("Error: Missing configuration in config.ini")
    sys.exit(1)


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
            UP_OUTPUT,
            DOWN_OUTPUT,
            CYL_STOPPER_B_UP,
            CYL_STOPPER_B_DOWN,
            WAIT_TIME,
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
