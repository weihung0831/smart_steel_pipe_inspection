import sys
from configparser import ConfigParser

from Controller.CylinderController import CylinderController
from Controller.ConnectionController import ConnectionController
sys.path.append("../ui/")
from ui.view import Ui_MainWindow

from backend import ModbusCom

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
        self.connectionController = ConnectionController(self.view, self.modbus)
        self.actuatorController = CylinderController(self.view, self.modbus)
