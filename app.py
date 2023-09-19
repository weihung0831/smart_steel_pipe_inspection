import sys
import time

import eel

sys.path.append("./backend/")
from backend import LoggerSetup, ModbusCom


@eel.expose
def modbus_status():
    ip = "192.168.3.5"
    modbus = ModbusCom(ip)
    return modbus.client.is_open

eel.init("web")  # 設定web的資料夾路徑
eel.start("index.html")  # 設定要開啟的html檔案路徑
