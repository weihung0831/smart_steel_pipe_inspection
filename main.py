import sys
from configparser import ConfigParser
from typing import Any

from PySide6.QtWidgets import QApplication, QMainWindow
from qt_material import apply_stylesheet

from Controller.CylinderController import CylinderController

sys.path.append("../ui/")
from backend import ModbusCom
from ui.view import Ui_MainWindow

sys.path.append("../backend/")
config = ConfigParser()
config.read("./config.ini")

try:
    IP_ADDRESS = config["Settings"]["IP_ADDRESS"]
except KeyError:
    print("Error: Missing configuration in config.ini")
    sys.exit(1)


class MainController:
    def __init__(self, MainWindow):
        self.view = Ui_MainWindow()
        self.view.setupUi(MainWindow)
        self.modbus = ModbusCom(IP_ADDRESS)
        self.initialize_ui_connections()
        self.initialize_cylinder_connections()

    def initialize_cylinder_connections(self):
        self.actuatorController = CylinderController(modbus=self.modbus)
        self.actuatorController.start()
        self.view.clean_stopper_cyl_up_btn.clicked.connect(
            self.actuatorController.control_cyl_stopper_a_up
        )
        self.view.clean_stopper_cyl_down_btn.clicked.connect(
            self.actuatorController.control_cyl_stopper_a_down
        )

    def initialize_ui_connections(self):
        self.view.power_btn.clicked.connect(self.connect_to_modbus)
        self.view.stop_btn.clicked.connect(self.disconnect_modbus_on_stop_click)

    def connect_to_modbus(self):
        try:
            if not self.modbus.client.is_open:
                self.modbus = ModbusCom(IP_ADDRESS)

            self.refresh_connection_status(self.modbus.client.is_open)
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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    apply_stylesheet(app, theme="dark_amber.xml", css_file="./ui/style.qss")
    controller = MainController(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
