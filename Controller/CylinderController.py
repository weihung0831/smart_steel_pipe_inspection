import sys
from configparser import ConfigParser

sys.path.append("../backend/")
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


class CylinderController:
    def __init__(self, view, modbus):
        self.view = view
        self.modbus = modbus
        self.cyl_stopper_b = Actuator(
            self.modbus,
            UP_OUTPUT,
            DOWN_OUTPUT,
            CYL_STOPPER_B_UP,
            CYL_STOPPER_B_DOWN,
            WAIT_TIME,
        )
        self.initialize_ui_connections()

    def initialize_ui_connections(self):
        self.view.clean_stopper_cyl_up_btn.clicked.connect(
            self.control_cyl_stopper_a_up
        )
        self.view.clean_stopper_cyl_down_btn.clicked.connect(
            self.control_cyl_stopper_a_down
        )

    def control_sensor(self, action, cyl_control):
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
            time.sleep(10)
            cyl_control.off()
            return True
        except Exception as e:
            print(e)
            return False

    def control_cyl_stopper_a_up(self):
        return self.control_sensor("up", self.cyl_stopper_b)

    def control_cyl_stopper_a_down(self):
        return self.control_sensor("down", self.cyl_stopper_b)
