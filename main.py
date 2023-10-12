import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from qt_material import apply_stylesheet

from Controller.MainController import MainController

sys.path.append("../backend/")
from backend import *


@LoggerSetup().log_execution
def main():
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    apply_stylesheet(app, theme="dark_amber.xml", css_file="./ui/style.qss")
    controller = MainController(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
