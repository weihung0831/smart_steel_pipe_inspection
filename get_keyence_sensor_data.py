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
        print("Keyence Sensor 連線成功")
        return client_socket

    def collect_keyence_sensor_data(self, client_socket):
        senor_a_end_angle, sensor_a_right_angle, sensor_a_face_width = [], [], []
        senor_b_end_angle, sensor_b_right_angle, sensor_b_face_width = [], [], []
        
        for i in range(5):
            data = client_socket.recv(1024)
            data = data.decode("utf-8")
            data_list = data.split(",")
            data_float = [float(i) for i in data_list]
            # print(data_float)
            senor_a_end_angle.append(data_float[0])
            sensor_a_right_angle.append(data_float[1])
            sensor_a_face_width.append(data_float[2])
            senor_b_end_angle.append(data_float[3])
            sensor_b_right_angle.append(data_float[4])
            sensor_b_face_width.append(data_float[5])

        result = [
            np.mean(senor_a_end_angle),
            np.mean(sensor_a_right_angle),
            np.mean(sensor_a_face_width),
            np.mean(senor_b_end_angle),
            np.mean(sensor_b_right_angle),
            np.mean(sensor_b_face_width),
        ]
        result = [round(i, 2) for i in result]
        # print(result)
        return result
    
if __name__ == "__main__":
    host = "192.168.10.10"
    port = 8500
    keyence_sensor = GetKeyenceSensorData(host, port)
    keyence_sensor.run()
