import sys

from view import Ui_MainWindow

sys.path.append("../backend/")
import time

from backend import *


@LoggerSetup().log_execution
class Controller:
    def __init__(self, MainWindow):
        self.view = Ui_MainWindow()
        self.view.setupUi(MainWindow)
        self.modbus = ModbusCom(IP_ADDRESS)
        self.initialize_ui_connections()

    def initialize_ui_connections(self):
        self.view.power_btn.clicked.connect(self.connect_to_modbus)
        self.view.stop_btn.clicked.connect(self.disconnect_modbus_on_stop_click)
        self.view.clean_stopper_cyl_up_btn.clicked.connect(
            self.initiate_control_block_testing
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

    def initiate_control_block_testing(self):
        try:
            control_block = ControlBlock(self.modbus)
            control_block.action_down()
            time.sleep(3)
            self.modbus.clear_output()
        except Exception as e:
            print(e)
            return False
