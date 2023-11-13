import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from qt_material import apply_stylesheet

from connect_modbus import ModbusCom
from get_keyence_sensor_data import GetKeyenceSensorData

sys.path.append("./ui")
import time

from auto_control import AutoControl
from ui.view import Ui_MainWindow
from PySide6.QtCore import QThread


class MainController:
    def __init__(self, MainWindow):
        self.view = Ui_MainWindow()
        self.view.setupUi(MainWindow)
        self.modbusA = ModbusCom("192.168.3.2")
        self.modbusB = ModbusCom("192.168.3.1")

        self.modbusA.clear_output()
        self.modbusB.clear_output()

        self.sucess_connect_msg = "已連線"
        self.fail_connect_msg = "未連線"
        self.counter = 0
        self.ng_counter = 0
        self.start_system()
        self.stop_system()

    def start_system(self):
        self.start_keyence_sensor_system()
        self.start_io_connect()
        self.start_manual_control_system()
        self.auto_control_system()

    def stop_system(self):
        self.view.stopBtn.clicked.connect(self.stopBtn_clicked)

    def start_keyence_sensor_system(self):
        self.view.startBtn.clicked.connect(self.keyence_sensor_connections)

    def start_io_connect(self):
        self.view.startBtn.clicked.connect(self.connect_io)

    def start_manual_control_system(self):
        self.view.manual_startBtn.clicked.connect(self.manual_control_on)
        self.view.manual_stopBtn.clicked.connect(self.manual_control_off)

    def auto_control_system(self):
        self.view.auto_control_btn.clicked.connect(self.auto_control)

    def wash_process(self):
        wash = 0
        # 檢查 Position A 是否在下方, 是的話 Position A up
        if (
            self.modbusA.read_modbus_input_state(11) == 1
            and self.modbusB.read_modbus_input_state(11) == 1
        ):
            QThread.sleep(2)
            self.manual_control_up(self.modbusA, 6, 7)
            self.manual_control_up(self.modbusB, 7, 6)
        # 檢查 Stopper B 是否在下方, 是的話 Stopper B up
        if (
            self.modbusA.read_modbus_input_state(3) == 1
            and self.modbusB.read_modbus_input_state(3) == 1
        ):
            QThread.sleep(2)
            self.manual_control_up(self.modbusA, 0, 1)
            self.manual_control_up(self.modbusB, 0, 1)
        # 檢查 Stopper A 是否在上方, 是的話 Stopper A down
        if (
            self.modbusA.read_modbus_input_state(8) == 1
            and self.modbusB.read_modbus_input_state(8) == 1
        ):
            QThread.sleep(2)
            self.manual_control_down(self.modbusA, 5, 4)
            self.manual_control_down(self.modbusB, 5, 4)
            wash += 1
        # Todo: 改沖水流程
        # 檢查是否有沖水，是的話 Position A down
        if wash == 1:
            QThread.sleep(3)
            self.manual_control_down(self.modbusA, 7, 6)
            self.manual_control_down(self.modbusB, 6, 7)

    def check_process(self):
        # 檢查 Position B 是否在下方, 是的話 Position B up
        if (
            self.modbusA.read_modbus_input_state(5) == 1
            and self.modbusB.read_modbus_input_state(5) == 1
        ):
            QThread.sleep(2)
            self.manual_control_up(self.modbusA, 2, 3)
            self.manual_control_up(self.modbusB, 2, 3)
        # 檢查 Stopper B 是否在上方, 是的話 Stopper B down
        if (
            self.modbusA.read_modbus_input_state(2) == 1
            and self.modbusB.read_modbus_input_state(2) == 1
        ):
            QThread.sleep(2)
            self.manual_control_down(self.modbusA, 1, 0)
            self.manual_control_down(self.modbusB, 1, 0)

    def auto_control(self):
        # 檢查 Stopper A 是否沒有在上方, 是的話 Stopper A up
        if (
            self.modbusA.read_modbus_input_state(8) == 0
            and self.modbusB.read_modbus_input_state(8) == 0
        ):
            self.manual_control_up(self.modbusA, 4, 5)
            self.manual_control_up(self.modbusB, 4, 5)
        while True:
            # 檢查是否有清洗製成的鋼管
            if (
                self.modbusA.read_modbus_input_state(7) == 1
                or self.modbusB.read_modbus_input_state(7) == 1
            ):
                self.wash_process()
            # 檢查機械式確認，有的話 Stopper A up
            if self.modbusB.read_modbus_input_state(6) == 1:
                QThread.sleep(2)
                self.manual_control_up(self.modbusA, 4, 5)
                self.manual_control_up(self.modbusB, 4, 5)
            # 檢查是否有檢查製成的鋼管
            if (
                self.modbusA.read_modbus_input_state(1) == 1
                or self.modbusB.read_modbus_input_state(1) == 1
            ):
                self.check_process()
            # 檢查 Position B 是否在上方, 是的話 Position B down
            if (
                self.modbusA.read_modbus_input_state(4) == 1
                and self.modbusB.read_modbus_input_state(4) == 1
            ):
                # 檢查 Keyence 是否在後方, 是的話 Keyence 往前推
                if (
                    self.modbusA.read_modbus_input_state(13) == 0
                    or self.modbusB.read_modbus_input_state(13) == 0
                ):
                    QThread.sleep(2)
                    self.manual_control_down(self.modbusA, 8, 9)
                    self.manual_control_down(self.modbusB, 9, 10)
                    QThread.sleep(3)
                    # 檢查 Keyence 是否在前方, 是的話 Keyence 往後推
                    self.manual_control_up(self.modbusA, 9, 8)
                    self.manual_control_up(self.modbusB, 10, 9)
                    QThread.sleep(2)
                    self.manual_control_down(self.modbusA, 3, 2)
                    self.manual_control_down(self.modbusB, 3, 2)
                    QThread.sleep(2)
            if self.modbusB.read_modbus_input_state(0) == 1:
                self.manual_control_down(self.modbusA, 0, 1)
                self.manual_control_down(self.modbusB, 0, 1)

    def stopBtn_clicked(self):
        self.collect_keyence_data_controller.stop()
        self.modbusA.stop()
        self.modbusB.stop()

        self.view.keyence_connect_status.setText(self.fail_connect_msg)
        self.view.io_connect_status.setText(self.fail_connect_msg)

        self.view.keyence_connect_status.setStyleSheet("color: red")
        self.view.io_connect_status.setStyleSheet("color: red")

        self.view.manual_startBtn.setEnabled(False)
        self.view.manual_restartBtn.setEnabled(False)
        self.view.manual_stopBtn.setEnabled(False)
        self.view.auto_control_btn.setEnabled(False)

        self.manual_control_btn_clicked(False)

    def manual_control_on(self):
        self.manual_control_btn_clicked(True)
        self.view.manual_stopBtn.setEnabled(True)
        self.view.manual_startBtn.setEnabled(False)
        self.view.manual_restartBtn.setEnabled(True)

        # 清洗製程 Stopper A
        self.view.clean_stopper_cyl_up_btn.clicked.connect(
            lambda: self.manual_control_up(self.modbusA, 4, 5)
        )
        self.view.clean_stopper_cyl_up_btn.clicked.connect(
            lambda: self.manual_control_up(self.modbusB, 4, 5)
        )

        self.view.clean_stopper_cyl_down_btn.clicked.connect(
            lambda: self.manual_control_down(self.modbusA, 5, 4)
        )
        self.view.clean_stopper_cyl_down_btn.clicked.connect(
            lambda: self.manual_control_down(self.modbusB, 5, 4)
        )

        # 清洗製程 Position A
        self.view.clean_fixed_position_CYL_up_btn.clicked.connect(
            lambda: self.manual_control_up(self.modbusA, 6, 7)
        )
        self.view.clean_fixed_position_CYL_up_btn.clicked.connect(
            lambda: self.manual_control_up(self.modbusB, 7, 6)
        )

        self.view.clean_fixed_position_CYL_down_btn.clicked.connect(
            lambda: self.manual_control_down(self.modbusA, 7, 6)
        )
        self.view.clean_fixed_position_CYL_down_btn.clicked.connect(
            lambda: self.manual_control_down(self.modbusB, 6, 7)
        )

        # 吹氣
        # self.view.blow_air_on_btn.clicked.connect(
        #     lambda: self.manual_control_up(self.modbusA, 10, 11)
        # )

        # 檢查製程 Stopper B
        self.view.check_stopper_cyl_up_btn.clicked.connect(
            lambda: self.manual_control_up(self.modbusA, 0, 1)
        )
        self.view.check_stopper_cyl_up_btn.clicked.connect(
            lambda: self.manual_control_up(self.modbusB, 0, 1)
        )

        self.view.check_stopper_cyl_down_btn.clicked.connect(
            lambda: self.manual_control_down(self.modbusA, 1, 0)
        )
        self.view.check_stopper_cyl_down_btn.clicked.connect(
            lambda: self.manual_control_down(self.modbusB, 1, 0)
        )

        # 檢查製程 Position B
        self.view.check_fixed_position_CYL_up_btn.clicked.connect(
            lambda: self.manual_control_up(self.modbusA, 2, 3)
        )
        self.view.check_fixed_position_CYL_up_btn.clicked.connect(
            lambda: self.manual_control_up(self.modbusB, 2, 3)
        )

        self.view.check_fixed_position_CYL_down_btn.clicked.connect(
            lambda: self.manual_control_down(self.modbusA, 3, 2)
        )
        self.view.check_fixed_position_CYL_down_btn.clicked.connect(
            lambda: self.manual_control_down(self.modbusB, 3, 2)
        )

        # keyence sensor
        self.view.laser_on_btn.clicked.connect(
            lambda: self.manual_control_up(self.modbusA, 8, 9)
        )
        self.view.laser_on_btn.clicked.connect(
            lambda: self.manual_control_up(self.modbusB, 9, 10)
        )

        self.view.laser_off_btn.clicked.connect(
            lambda: self.manual_control_down(self.modbusA, 9, 8)
        )
        self.view.laser_off_btn.clicked.connect(
            lambda: self.manual_control_down(self.modbusB, 10, 9)
        )

    def manual_control_off(self):
        self.manual_control_btn_clicked(False)
        self.view.manual_stopBtn.setEnabled(False)
        self.view.manual_startBtn.setEnabled(True)
        self.view.manual_restartBtn.setEnabled(False)
        self.modbusA.clear_output()
        self.modbusB.clear_output()

    def manual_control_up(self, modbus, pin_up, pin_down):
        modbus.set_modbus_output_state(pin_up, True)
        modbus.set_modbus_output_state(pin_down, False)

    def manual_control_down(self, modbus, pin_up, pin_down):
        modbus.set_modbus_output_state(pin_up, True)
        modbus.set_modbus_output_state(pin_down, False)

    def manual_control_btn_clicked(self, activate):
        # 清洗製程
        self.view.clean_stopper_cyl_up_btn.setEnabled(activate)
        self.view.clean_stopper_cyl_down_btn.setEnabled(activate)
        self.view.clean_fixed_position_CYL_up_btn.setEnabled(activate)
        self.view.clean_fixed_position_CYL_down_btn.setEnabled(activate)

        # 檢查製程
        self.view.check_stopper_cyl_up_btn.setEnabled(activate)
        self.view.check_stopper_cyl_down_btn.setEnabled(activate)
        self.view.check_fixed_position_CYL_up_btn.setEnabled(activate)
        self.view.check_fixed_position_CYL_down_btn.setEnabled(activate)

        # pump
        self.view.pomp_power_on_btn.setEnabled(activate)
        self.view.pomp_power_off_btn.setEnabled(activate)

        # 電磁閥
        self.view.solenoid_value_on_btn.setEnabled(activate)
        self.view.solenoid_value_off_btn.setEnabled(activate)

        # 雷射
        self.view.laser_on_btn.setEnabled(activate)
        self.view.laser_off_btn.setEnabled(activate)

        # 吹氣
        self.view.blow_air_on_btn.setEnabled(activate)
        self.view.blow_air_off_btn.setEnabled(activate)

    def connect_io(self):
        try:
            if self.modbusA.client.is_open and self.modbusB.client.is_open:
                self.view.auto_control_btn.setEnabled(True)
                self.view.io_connect_status.setText(self.sucess_connect_msg)
                self.view.io_connect_status.setStyleSheet("color: green")
                self.view.manual_startBtn.setEnabled(True)
                return True
            else:
                self.view.io_connect_status.setText(self.fail_connect_msg)
                self.view.io_connect_status.setStyleSheet("color: red")
                return False
        except Exception as e:
            print(e)
            print("I/O 連線失敗")
            self.view.io_connect_status.setText("I/O 連線失敗")
            self.view.io_connect_status.setStyleSheet("color: red")
            return False

    def keyence_sensor_connections(self, host="192.168.3.10", port=8500):
        self.collect_keyence_data_controller = GetKeyenceSensorData(host, port)
        if self.collect_keyence_data_controller.connect_keyence_sensor() == False:
            self.view.keyence_connect_status.setText(self.fail_connect_msg)
            self.view.keyence_connect_status.setStyleSheet("color: red")
            return False
        else:
            self.view.keyence_connect_status.setText(self.sucess_connect_msg)
            self.view.keyence_connect_status.setStyleSheet("color: green")
            self.collect_keyence_data_controller.data_signal.connect(
                self.update_keyence_data
            )
            self.collect_keyence_data_controller.start()
            return True

    def update_keyence_data(self, result):
        self.counter += 1
        senor_a_end_angle = result[1]
        sensor_a_right_angle = result[0]
        sensor_a_face_width = result[2]
        senor_b_end_angle = result[4]
        sensor_b_right_angle = result[3]
        sensor_b_face_width = result[5]

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
            self.view.sensor_A_detection_value.setStyleSheet("color: red")
        else:
            self.view.sensor_A_detection_value.setText("OK")
            self.view.sensor_A_detection_value.setStyleSheet("color: green")

        if (
            self.detection_value_judgment(
                senor_b_end_angle, sensor_b_face_width, sensor_b_right_angle
            )
            == False
        ):
            self.view.sensor_B_detection_value.setText("NG")
            self.view.sensor_B_detection_value.setStyleSheet("color: red")
        else:
            self.view.sensor_B_detection_value.setText("OK")
            self.view.sensor_B_detection_value.setStyleSheet("color: green")

        if (
            self.view.sensor_A_detection_value.text() == "NG"
            or self.view.sensor_B_detection_value.text() == "NG"
        ):
            self.view.final_detection_result.setText("NG")
            self.ng_counter += 1
            self.view.ng_counter.setText(str(self.ng_counter))
            self.view.final_detection_result.setStyleSheet("color: red")
            self.view.ng_counter.setStyleSheet("color: red")
        else:
            self.view.final_detection_result.setText("OK")
            self.view.final_detection_result.setStyleSheet("color: green")

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
    apply_stylesheet(app, theme="dark_cyan.xml", css_file="./ui/style.qss")
    controller = MainController(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
