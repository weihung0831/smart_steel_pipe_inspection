import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from view import Ui_MainWindow
from qt_material import apply_stylesheet
from pathlib import Path

app = QApplication(sys.argv)
MainWindow = QMainWindow()
apply_stylesheet(app, theme="dark_amber.xml", css_file='./style.qss')
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec())
