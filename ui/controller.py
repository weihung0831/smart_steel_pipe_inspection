from view import Ui_MainWindow


class Controller:
    def __init__(self, MainWindow):
        self.view = Ui_MainWindow()
        self.view.setupUi(MainWindow)

    def set_text(self, text):
        self.view.end_face_angle_target_lineEdit.setText(text)
