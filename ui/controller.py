import sys
import time
from configparser import ConfigParser

from view import Ui_MainWindow

sys.path.append("../backend/")
from backend import *

config = ConfigParser()
config.read("./config.ini")

try:
    IP_ADDRESS = config["Settings"]["IP_ADDRESS"]
    UP_OUTPUT = int(config["Settings"]["UP_OUTPUT"])
    DOWN_OUTPUT = int(config["Settings"]["DOWN_OUTPUT"])
    CYL_STOPPER_B_UP = int(config["Settings"]["CYL_STOPPER_B_UP"])
    CYL_STOPPER_B_DOWN = int(config["Settings"]["CYL_STOPPER_B_DOWN"])
    WAIT_TIME = int(config["Settings"]["WAIT_TIME"])
except KeyError:
    print("Error: Missing configuration in config.ini")
    sys.exit(1)


@LoggerSetup().log_execution
class Controller:
    def __init__(self, MainWindow):
        self.view = Ui_MainWindow()
        self.view.setupUi(MainWindow)
        self.modbus = ModbusCom(IP_ADDRESS)
        self.initialize_ui_connections()
        self.cyl_stopper_b = Actuator(self.modbus, UP_OUTPUT, DOWN_OUTPUT, CYL_STOPPER_B_UP, CYL_STOPPER_B_DOWN,WAIT_TIME)

    def initialize_ui_connections(self):
        self.view.power_btn.clicked.connect(self.connect_to_modbus)
        self.view.stop_btn.clicked.connect(self.disconnect_modbus_on_stop_click)
        self.view.clean_stopper_cyl_up_btn.clicked.connect(
            self.control_cyl_stopper_a_up
        )
        self.view.clean_stopper_cyl_down_btn.clicked.connect(
            self.control_cyl_stopper_a_down
        )

    def connect_to_modbus(self):
        try:
            if not self.modbus.client.is_open:
                self.modbus = ModbusCom(IP_ADDRESS)

            self.refresh_connection_status(self.modbus.client.is_open)
            print("已連線")
            return self.modbus.client.is_open
        except Exception as e:
            self._log_and_update_status(e, "連線異常 !!!")
            return False

    def disconnect_modbus_on_stop_click(self):
        try:
            self.modbus.clear_output()
            self.modbus.disconnect()
            is_closed = not self.modbus.client.is_open
            if is_closed:
                print("已停止")
                self.view.power_status_label.setText("已停止")
            return is_closed
        except Exception as e:
            self._log_and_update_status(e, "停止異常 !!!")
            return False

    def refresh_connection_status(self, is_connected):
        status_text = "連線成功 !!!" if is_connected else "連線失敗 !!!"
        self.view.power_status_label.setText(status_text)

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
