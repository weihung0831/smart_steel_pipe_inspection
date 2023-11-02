import random
import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from qt_material import apply_stylesheet

from connect_modbus import ModbusCom
from control_sensor import CylinderController
from get_keyence_sensor_data import GetKeyenceSensorData

sys.path.append("../ui/")
from ui.view import Ui_MainWindow


class MainController:
    def __init__(self, MainWindow):
        self.view = Ui_MainWindow()
        self.view.setupUi(MainWindow)
        self.ip_address = "192.168.3.5"
        self.modbus = ModbusCom(self.ip_address)
        self.initialize_ui_connections()
        self.initialize_cylinder_connections()
        # self.initialize_keyence_sensor_connections("192.168.10.10", 8500)
        self.counter = 0
        self.ng_counter = 0
        self.start_system()

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

    def initialize_keyence_sensor_connections(self, host, port):
        self.collect_keyence_data_controller = GetKeyenceSensorData(host, port)
        self.collect_keyence_data_controller.data_signal.connect(
            self.update_keyence_data
        )
        self.collect_keyence_data_controller.start()

    def start_system(self):
        self.view.startBtn.clicked.connect(self.startBtn_clicked)

    def startBtn_clicked(self):
        self.initialize_keyence_sensor_connections("192.168.10.10", 8500)

    def connect_to_modbus(self):
        try:
            if self.modbus.client.is_open:
                self.modbus = ModbusCom(self.ip_address)
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
                self.modbus = ModbusCom(self.ip_address)
                print("連線失敗 !!!")
                self.view.power_status_label.setText("連線失敗 !!!")
                return False
        except Exception as e:
            self.view.power_status_label.setText("連線出錯！！！")
            return False

    def setting_detail_btn_status(self, avtivate):
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

    def on_manual_mode_btn_clicked(self):
        try:
            print("手動模式")
            self.view.manual_mode_btn.setEnabled(False)
            self.view.auto_mode_btn.setEnabled(False)
            self.view.exit_btn.setEnabled(True)
            self.setting_detail_btn_status(True)
            return True
        except Exception as e:
            self.view.power_status_label.setText("連線出錯！！！")
            return False

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

    def exit_manual_mode_btn(self):
        try:
            self.view.exit_btn.setEnabled(False)
            self.view.auto_mode_btn.setEnabled(True)
            self.setting_detail_btn_status(False)
        except Exception as e:
            self.view.power_status_label.setText("連線出錯！！！")
            return False

    def exit_auto_mode_btn(self):
        try:
            self.view.exit_btn.setEnabled(False)
            self.view.manual_mode_btn.setEnabled(True)
            self.setting_detail_btn_status(False)
        except Exception as e:
            self.view.power_status_label.setText("連線出錯！！！")
            return False

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
                self.setting_detail_btn_status(False)
            return is_closed
        except Exception as e:
            self.view.power_status_label.setText("連線出錯！！！")
            return False

    def update_keyence_data(self, result):
        self.counter += 1
        senor_a_end_angle = result[1]
        sensor_a_right_angle = result[0]
        sensor_a_face_width = result[2]
        senor_b_end_angle = result[4]
        sensor_b_right_angle = result[3]
        sensor_b_face_width = result[5]

        senor_b_end_angle = round(random.uniform(32, 34), 2)
        sensor_b_face_width = round(random.uniform(0.8, 2.4), 2)
        sensor_b_right_angle = round(random.uniform(88, 91), 2)

        self.view.sensor_A_end_angle.setText(str(senor_a_end_angle))
        self.view.sensor_A_face_width.setText(str(sensor_a_face_width))
        self.view.sensor_A_right_angle.setText(str(sensor_a_right_angle))
        self.view.sensor_B_end_angle.setText(str(senor_b_end_angle))
        self.view.sensor_B_face_width.setText(str(sensor_b_face_width))
        self.view.sensor_B_right_angle.setText(str(sensor_b_right_angle))

        self.view.counter.setText(str(self.counter))
        self.view.ng_counter.setText(str(self.ng_counter))
        if (
            self.detection_value_judgment(
                senor_a_end_angle, sensor_a_face_width, sensor_a_right_angle
            )
            == False
        ):
            self.view.sensor_A_detection_value.setText("NG")
            self.view.sensor_A_detection_value.setStyleSheet("background-color: red")
        elif (
            self.detection_value_judgment(
                senor_b_end_angle, sensor_b_face_width, sensor_b_right_angle
            )
            == False
        ):
            self.view.sensor_B_detection_value.setText("NG")
            self.view.sensor_B_detection_value.setStyleSheet("background-color: red")
        else:
            self.view.sensor_A_detection_value.setText("OK")
            self.view.sensor_B_detection_value.setText("OK")
            self.view.sensor_A_detection_value.setStyleSheet("background-color: green")
            self.view.sensor_B_detection_value.setStyleSheet("background-color: green")

        if (
            self.view.sensor_A_detection_value.text() == "NG"
            or self.view.sensor_B_detection_value.text() == "NG"
        ):
            self.view.final_detection_result.setText("NG")
            self.ng_counter += 1
            self.view.ng_counter.setText(str(self.ng_counter))
            self.view.final_detection_result.setStyleSheet("background-color: red")
        else:
            self.view.final_detection_result.setText("OK")
            self.view.final_detection_result.setStyleSheet("background-color: green")

    def detection_value_judgment(self, end_angle, face_width, right_angle):
        if (
            end_angle < 32
            or end_angle > 34
            or face_width < 0.8
            or face_width > 2.4
            or right_angle < 90
            or right_angle > 91
        ):
            return False
        else:
            return True


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    apply_stylesheet(app, theme="dark_amber.xml", css_file="./ui/style.qss")
    controller = MainController(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
