import sys
from pathlib import Path

from controller import Controller
from PySide6.QtWidgets import QApplication, QMainWindow
from qt_material import apply_stylesheet
from view import Ui_MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    apply_stylesheet(app, theme="dark_amber.xml", css_file="./style.qss")
    controller = Controller(MainWindow)
    controller.set_text("Hello World!")
    MainWindow.show()
    sys.exit(app.exec())
