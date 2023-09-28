import sys

from view import Ui_MainWindow

sys.path.append("../backend/")
from backend import *


@LoggerSetup().log_execution
class Controller:
    def __init__(self, MainWindow):
        self.view = Ui_MainWindow()
        self.view.setupUi(MainWindow)
        self.modbus = ModbusCom(IP_ADDRESS)
        self._initialize_connections()

    def _initialize_connections(self):
        self.view.power_btn.clicked.connect(self._handle_power_button_click)
        self.view.stop_btn.clicked.connect(self._handle_stop_button_click)

    def _handle_power_button_click(self):
        try:
            if not self.modbus.client.is_open:
                self.modbus = ModbusCom(IP_ADDRESS)

            self._update_connection_status(self.modbus.client.is_open)
            print("已連線")
            return self.modbus.client.is_open
        except Exception as e:
            self._log_and_update_status(e, "連線異常 !!!")
            return False

    def _handle_stop_button_click(self):
        try:
            self.modbus.disconnect()
            is_closed = not self.modbus.client.is_open
            if is_closed:
                print("已停止")
                self.view.power_status_label.setText("已停止")
            return is_closed
        except Exception as e:
            self._log_and_update_status(e, "停止異常 !!!")
            return False

    def _update_connection_status(self, is_connected):
        status_text = "連線成功 !!!" if is_connected else "連線失敗 !!!"
        self.view.power_status_label.setText(status_text)

