import sys
from configparser import ConfigParser
from typing import Any

from PySide6.QtWidgets import QApplication, QMainWindow
from qt_material import apply_stylesheet

from Controller.CylinderController import CylinderController

sys.path.append("../ui/")
from backend import ModbusCom, LoggerSetup
from ui.view import Ui_MainWindow

sys.path.append("../backend/")
config = ConfigParser()
config.read("./config.ini")

try:
    IP_ADDRESS = config["Settings"]["IP_ADDRESS"]
except KeyError:
    print("Error: Missing configuration in config.ini")
    sys.exit(1)


@LoggerSetup().log_execution
class MainController:
    def __init__(self, MainWindow):
        self.view = Ui_MainWindow()
        self.view.setupUi(MainWindow)
        self.modbus = ModbusCom(IP_ADDRESS)
        self.initialize_ui_connections()
        self.initialize_cylinder_connections()

    @LoggerSetup().log_execution
    def initialize_cylinder_connections(self):
        self.actuatorController = CylinderController(modbus=self.modbus)
        self.actuatorController.start()
        self.view.clean_stopper_cyl_up_btn.clicked.connect(
            self.actuatorController.control_cyl_stopper_a_up
        )
        self.view.clean_stopper_cyl_down_btn.clicked.connect(
            self.actuatorController.control_cyl_stopper_a_down
        )

    @LoggerSetup().log_execution
    def initialize_ui_connections(self):
        self.view.power_btn.clicked.connect(self.connect_to_modbus)
        self.view.stop_btn.clicked.connect(self.disconnect_modbus_on_stop_click)

    @LoggerSetup().log_execution
    def connect_to_modbus(self):
        try:
            if self.modbus.client.is_open:
                self.modbus = ModbusCom(IP_ADDRESS)
                print("已連線")
                self.view.power_status_label.setText("已連線")

                self.view.power_btn.setEnabled(False)
                self.view.stop_btn.setEnabled(True)
                self.view.manual_mode_btn.setEnabled(True)
                self.view.auto_mode_btn.setEnabled(True)
                self.view.exit_btn.setEnabled(False)
                self.view.manual_mode_btn.clicked.connect(
                    self.on_manual_mode_btn_clicked
                )
                self.view.auto_mode_btn.clicked.connect(self.on_auto_mode_btn_clicked)
                self.view.exit_btn.clicked.connect(self.exit_manual_mode_btn)
                self.view.exit_btn.clicked.connect(self.exit_auto_mode_btn)
                return True
            else:
                self.modbus = ModbusCom(IP_ADDRESS)
                print("連線失敗 !!!")
                self.view.power_status_label.setText("連線失敗 !!!")
                return False
        except Exception as e:
            self.view.power_status_label.setText("連線出錯！！！")
            return False

    @LoggerSetup().log_execution
    def action_setting_detail_btn_status(self, avtivate):
        self.view.clean_stopper_cyl_up_btn.setEnabled(avtivate)
        self.view.clean_stopper_cyl_down_btn.setEnabled(avtivate)
        self.view.clean_fixed_position_CYL_up_btn.setEnabled(avtivate)
        self.view.clean_fixed_position_CYL_down_btn.setEnabled(avtivate)
        self.view.check_stopper_cyl_up_btn.setEnabled(avtivate)
        self.view.check_stopper_cyl_down_btn.setEnabled(avtivate)
        self.view.check_fixed_position_CYL_up_btn.setEnabled(avtivate)
        self.view.check_fixed_position_CYL_down_btn.setEnabled(avtivate)
        self.view.pomp_power_open_btn.setEnabled(avtivate)
        self.view.pomp_power_close_btn.setEnabled(avtivate)
        self.view.pomp_check_CYL_open_btn.setEnabled(avtivate)
        self.view.pomp_check_CYL_close_btn.setEnabled(avtivate)
        self.view.airValue_value_open_btn.setEnabled(avtivate)
        self.view.airValue_value_close_btn.setEnabled(avtivate)
        self.view.air_value_open_btn.setEnabled(avtivate)
        self.view.air_value_close_btn.setEnabled(avtivate)

    @LoggerSetup().log_execution
    def on_manual_mode_btn_clicked(self):
        try:
            print("手動模式")
            self.view.manual_mode_btn.setEnabled(False)
            self.view.auto_mode_btn.setEnabled(False)
            self.view.exit_btn.setEnabled(True)
            self.action_setting_detail_btn_status(True)
            return True
        except Exception as e:
            self.view.power_status_label.setText("連線出錯！！！")
            return False

    @LoggerSetup().log_execution
    def on_auto_mode_btn_clicked(self):
        try:
            print("自動模式")
            self.view.manual_mode_btn.setEnabled(False)
            self.view.auto_mode_btn.setEnabled(False)
            self.view.exit_btn.setEnabled(True)
            return True
        except Exception as e:
            self.view.power_status_label.setText("連線出錯！！！")
            return False

    @LoggerSetup().log_execution
    def exit_manual_mode_btn(self):
        try:
            self.view.exit_btn.setEnabled(False)
            self.view.auto_mode_btn.setEnabled(True)
            self.action_setting_detail_btn_status(False)
        except Exception as e:
            self.view.power_status_label.setText("連線出錯！！！")
            return False

    @LoggerSetup().log_execution
    def exit_auto_mode_btn(self):
        try:
            self.view.exit_btn.setEnabled(False)
            self.view.manual_mode_btn.setEnabled(True)
            self.action_setting_detail_btn_status(False)
        except Exception as e:
            self.view.power_status_label.setText("連線出錯！！！")
            return False

    @LoggerSetup().log_execution
    def disconnect_modbus_on_stop_click(self):
        try:
            self.modbus.clear_output()
            self.modbus.disconnect()
            is_closed = not self.modbus.client.is_open
            if is_closed:
                print("已停止")
                self.view.power_status_label.setText("已停止")
                self.view.power_btn.setEnabled(True)
                self.view.stop_btn.setEnabled(False)
                self.view.manual_mode_btn.setEnabled(False)
                self.view.auto_mode_btn.setEnabled(False)
                self.view.exit_btn.setEnabled(False)
                self.action_setting_detail_btn_status(False)
            return is_closed
        except Exception as e:
            self.view.power_status_label.setText("連線出錯！！！")
            return False


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    apply_stylesheet(app, theme="dark_amber.xml", css_file="./ui/style.qss")
    controller = MainController(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
