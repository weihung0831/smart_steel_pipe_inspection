import socket

import numpy as np
from PyQt6.QtCore import QThread, pyqtSignal


class GetKeyenceSensorData(QThread):
    data_signal = pyqtSignal(list)

    def __init__(self, host, port):
        super().__init__()
        self.host = host
        self.port = port

    def run(self):
        client_socket = self.connect_keyence_sensor()
        try:
            while True:
                result = self.collect_keyence_sensor_data(client_socket)
                self.data_signal.emit(result)
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            client_socket.close()

    def connect_keyence_sensor(self):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((self.host, self.port))
        print("連線成功")
        return client_socket

    def collect_keyence_sensor_data(self, client_socket):
        end_face_angle, right_angle, end_face_width = [], [], []
        for i in range(3):
            data = client_socket.recv(1024)
            data = data.decode("utf-8")
            data_list = data.split(",")
            data_float = [float(i) for i in data_list]
            # print(data_float)
            end_face_angle.append(data_float[0])
            right_angle.append(data_float[1])
            end_face_width.append(data_float[2])
        result = [
            np.mean(end_face_angle),
            np.mean(right_angle),
            np.mean(end_face_width),
        ]
        result = [round(i, 2) for i in result]
        return result
