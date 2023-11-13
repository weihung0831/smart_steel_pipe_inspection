# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitledXhKtdQ.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QStatusBar,
    QTabWidget,
    QWidget,
)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1004, 768)
        MainWindow.setMaximumSize(QSize(1004, 768))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tabWidget.setGeometry(QRect(10, 0, 1041, 761))
        self.tab = QWidget()
        self.tab.setObjectName("tab")
        self.gridLayoutWidget = QWidget(self.tab)
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 60, 971, 271))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.sensor_A_end_angle = QLineEdit(self.gridLayoutWidget)
        self.sensor_A_end_angle.setObjectName("sensor_A_end_angle")
        self.sensor_A_end_angle.setEnabled(True)
        self.sensor_A_end_angle.setReadOnly(True)

        self.gridLayout.addWidget(self.sensor_A_end_angle, 4, 4, 1, 1)

        self.horizontalSpacer_19 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.gridLayout.addItem(self.horizontalSpacer_19, 0, 0, 1, 1)

        self.label_9 = QLabel(self.gridLayoutWidget)
        self.label_9.setObjectName("label_9")

        self.gridLayout.addWidget(self.label_9, 8, 2, 1, 1, Qt.AlignHCenter)

        self.horizontalSpacer_4 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.gridLayout.addItem(self.horizontalSpacer_4, 0, 11, 1, 1)

        self.sensor_B_right_angle = QLineEdit(self.gridLayoutWidget)
        self.sensor_B_right_angle.setObjectName("sensor_B_right_angle")
        self.sensor_B_right_angle.setReadOnly(True)

        self.gridLayout.addWidget(self.sensor_B_right_angle, 6, 6, 1, 1)

        self.sensor_A_face_width = QLineEdit(self.gridLayoutWidget)
        self.sensor_A_face_width.setObjectName("sensor_A_face_width")
        self.sensor_A_face_width.setReadOnly(True)

        self.gridLayout.addWidget(self.sensor_A_face_width, 4, 8, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.gridLayout.addItem(self.horizontalSpacer_8, 0, 7, 1, 1)

        self.label_8 = QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName("label_8")

        self.gridLayout.addWidget(self.label_8, 1, 10, 1, 1, Qt.AlignHCenter)

        self.right_angle_target = QLineEdit(self.gridLayoutWidget)
        self.right_angle_target.setObjectName("right_angle_target")

        self.gridLayout.addWidget(self.right_angle_target, 8, 6, 1, 1)

        self.sensor_A_right_angle = QLineEdit(self.gridLayoutWidget)
        self.sensor_A_right_angle.setObjectName("sensor_A_right_angle")
        self.sensor_A_right_angle.setReadOnly(True)

        self.gridLayout.addWidget(self.sensor_A_right_angle, 4, 6, 1, 1)

        self.label_6 = QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")

        self.gridLayout.addWidget(self.label_6, 1, 6, 1, 1, Qt.AlignHCenter)

        self.face_width_target = QLineEdit(self.gridLayoutWidget)
        self.face_width_target.setObjectName("face_width_target")

        self.gridLayout.addWidget(self.face_width_target, 8, 8, 1, 1)

        self.sensor_B_end_angle = QLineEdit(self.gridLayoutWidget)
        self.sensor_B_end_angle.setObjectName("sensor_B_end_angle")
        self.sensor_B_end_angle.setReadOnly(True)

        self.gridLayout.addWidget(self.sensor_B_end_angle, 6, 4, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.gridLayout.addItem(self.horizontalSpacer_7, 0, 9, 1, 1)

        self.label_5 = QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")

        self.gridLayout.addWidget(self.label_5, 1, 4, 1, 1, Qt.AlignHCenter)

        self.final_detection_result = QLineEdit(self.gridLayoutWidget)
        self.final_detection_result.setObjectName("final_detection_result")
        self.final_detection_result.setReadOnly(True)

        self.gridLayout.addWidget(self.final_detection_result, 10, 10, 1, 1)

        self.sensor_B_face_width = QLineEdit(self.gridLayoutWidget)
        self.sensor_B_face_width.setObjectName("sensor_B_face_width")
        self.sensor_B_face_width.setReadOnly(True)

        self.gridLayout.addWidget(self.sensor_B_face_width, 6, 8, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")

        self.gridLayout.addWidget(self.label_3, 6, 2, 1, 1, Qt.AlignHCenter)

        self.sensor_A_detection_value = QLineEdit(self.gridLayoutWidget)
        self.sensor_A_detection_value.setObjectName("sensor_A_detection_value")
        self.sensor_A_detection_value.setReadOnly(True)

        self.gridLayout.addWidget(self.sensor_A_detection_value, 4, 10, 1, 1)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")

        self.gridLayout.addWidget(self.label, 4, 2, 1, 1, Qt.AlignHCenter)

        self.end_angle_target = QLineEdit(self.gridLayoutWidget)
        self.end_angle_target.setObjectName("end_angle_target")

        self.gridLayout.addWidget(self.end_angle_target, 8, 4, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.gridLayout.addItem(self.horizontalSpacer_9, 0, 3, 1, 1)

        self.sensor_B_detection_value = QLineEdit(self.gridLayoutWidget)
        self.sensor_B_detection_value.setObjectName("sensor_B_detection_value")
        self.sensor_B_detection_value.setReadOnly(True)

        self.gridLayout.addWidget(self.sensor_B_detection_value, 6, 10, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.gridLayout.addItem(self.horizontalSpacer_5, 0, 5, 1, 1)

        self.label_7 = QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName("label_7")

        self.gridLayout.addWidget(self.label_7, 1, 8, 1, 1, Qt.AlignHCenter)

        self.label_11 = QLabel(self.gridLayoutWidget)
        self.label_11.setObjectName("label_11")

        self.gridLayout.addWidget(self.label_11, 10, 2, 1, 1, Qt.AlignHCenter)

        self.verticalSpacer_8 = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.gridLayout.addItem(self.verticalSpacer_8, 2, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.gridLayout.addItem(self.verticalSpacer_3, 5, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.gridLayout.addItem(self.verticalSpacer_4, 7, 0, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.gridLayout.addItem(self.verticalSpacer_6, 9, 0, 1, 1)

        self.horizontalLayoutWidget = QWidget(self.tab)
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 590, 971, 51))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.startBtn = QPushButton(self.horizontalLayoutWidget)
        self.startBtn.setObjectName("startBtn")

        self.horizontalLayout.addWidget(self.startBtn)

        self.horizontalSpacer_3 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.auto_control_btn = QPushButton(self.horizontalLayoutWidget)
        self.auto_control_btn.setObjectName("auto_control_btn")
        self.auto_control_btn.setEnabled(False)

        self.horizontalLayout.addWidget(self.auto_control_btn)

        self.horizontalSpacer_20 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout.addItem(self.horizontalSpacer_20)

        self.pauseBtn = QPushButton(self.horizontalLayoutWidget)
        self.pauseBtn.setObjectName("pauseBtn")

        self.horizontalLayout.addWidget(self.pauseBtn)

        self.horizontalSpacer_6 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout.addItem(self.horizontalSpacer_6)

        self.restartBtn = QPushButton(self.horizontalLayoutWidget)
        self.restartBtn.setObjectName("restartBtn")

        self.horizontalLayout.addWidget(self.restartBtn)

        self.horizontalSpacer_10 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout.addItem(self.horizontalSpacer_10)

        self.stopBtn = QPushButton(self.horizontalLayoutWidget)
        self.stopBtn.setObjectName("stopBtn")

        self.horizontalLayout.addWidget(self.stopBtn)

        self.horizontalSpacer_2 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.horizontalLayoutWidget_2 = QWidget(self.tab)
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(10, 420, 971, 80))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_11 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_2.addItem(self.horizontalSpacer_11)

        self.label_12 = QLabel(self.horizontalLayoutWidget_2)
        self.label_12.setObjectName("label_12")

        self.horizontalLayout_2.addWidget(self.label_12, 0, Qt.AlignHCenter)

        self.horizontalSpacer_15 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_2.addItem(self.horizontalSpacer_15)

        self.counter = QLineEdit(self.horizontalLayoutWidget_2)
        self.counter.setObjectName("counter")
        self.counter.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.counter)

        self.horizontalSpacer_12 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_2.addItem(self.horizontalSpacer_12)

        self.label_13 = QLabel(self.horizontalLayoutWidget_2)
        self.label_13.setObjectName("label_13")

        self.horizontalLayout_2.addWidget(self.label_13, 0, Qt.AlignHCenter)

        self.horizontalSpacer_16 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_2.addItem(self.horizontalSpacer_16)

        self.total_counter = QLineEdit(self.horizontalLayoutWidget_2)
        self.total_counter.setObjectName("total_counter")
        self.total_counter.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.total_counter)

        self.horizontalSpacer_13 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_2.addItem(self.horizontalSpacer_13)

        self.label_14 = QLabel(self.horizontalLayoutWidget_2)
        self.label_14.setObjectName("label_14")

        self.horizontalLayout_2.addWidget(self.label_14, 0, Qt.AlignHCenter)

        self.horizontalSpacer_17 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_2.addItem(self.horizontalSpacer_17)

        self.ng_counter = QLineEdit(self.horizontalLayoutWidget_2)
        self.ng_counter.setObjectName("ng_counter")
        self.ng_counter.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.ng_counter)

        self.horizontalSpacer_14 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_2.addItem(self.horizontalSpacer_14)

        self.horizontalLayoutWidget_3 = QWidget(self.tab)
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(10, 10, 971, 41))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_5 = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.horizontalLayout_3.addItem(self.verticalSpacer_5)

        self.horizontalLayoutWidget_4 = QWidget(self.tab)
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(10, 340, 971, 71))
        self.horizontalLayout_4 = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_7 = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.horizontalLayout_4.addItem(self.verticalSpacer_7)

        self.horizontalLayoutWidget_5 = QWidget(self.tab)
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayoutWidget_5.setGeometry(QRect(10, 510, 971, 71))
        self.horizontalLayout_5 = QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_9 = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.horizontalLayout_5.addItem(self.verticalSpacer_9)

        self.horizontalLayoutWidget_6 = QWidget(self.tab)
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.horizontalLayoutWidget_6.setGeometry(QRect(10, 650, 971, 21))
        self.horizontalLayout_6 = QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_10 = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.horizontalLayout_6.addItem(self.verticalSpacer_10)

        self.horizontalLayoutWidget_15 = QWidget(self.tab)
        self.horizontalLayoutWidget_15.setObjectName("horizontalLayoutWidget_15")
        self.horizontalLayoutWidget_15.setGeometry(QRect(10, 680, 481, 31))
        self.horizontalLayout_11 = QHBoxLayout(self.horizontalLayoutWidget_15)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.horizontalLayoutWidget_15)
        self.label_10.setObjectName("label_10")
        self.label_10.setEnabled(True)

        self.horizontalLayout_11.addWidget(self.label_10)

        self.keyence_connect_status = QLabel(self.horizontalLayoutWidget_15)
        self.keyence_connect_status.setObjectName("keyence_connect_status")

        self.horizontalLayout_11.addWidget(self.keyence_connect_status)

        self.label_15 = QLabel(self.horizontalLayoutWidget_15)
        self.label_15.setObjectName("label_15")

        self.horizontalLayout_11.addWidget(self.label_15)

        self.io_connect_status = QLabel(self.horizontalLayoutWidget_15)
        self.io_connect_status.setObjectName("io_connect_status")

        self.horizontalLayout_11.addWidget(self.io_connect_status)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayoutWidget_7 = QWidget(self.tab_2)
        self.horizontalLayoutWidget_7.setObjectName("horizontalLayoutWidget_7")
        self.horizontalLayoutWidget_7.setGeometry(QRect(10, 10, 971, 41))
        self.horizontalLayout_7 = QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_11 = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.horizontalLayout_7.addItem(self.verticalSpacer_11)

        self.gridLayoutWidget_2 = QWidget(self.tab_2)
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(10, 60, 971, 196))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.check_fixed_position_CYL_down_btn = QPushButton(self.gridLayoutWidget_2)
        self.check_fixed_position_CYL_down_btn.setObjectName(
            "check_fixed_position_CYL_down_btn"
        )
        self.check_fixed_position_CYL_down_btn.setEnabled(False)

        self.gridLayout_2.addWidget(self.check_fixed_position_CYL_down_btn, 6, 10, 1, 1)

        self.check_fixed_position_CYL_up_btn = QPushButton(self.gridLayoutWidget_2)
        self.check_fixed_position_CYL_up_btn.setObjectName(
            "check_fixed_position_CYL_up_btn"
        )
        self.check_fixed_position_CYL_up_btn.setEnabled(False)

        self.gridLayout_2.addWidget(self.check_fixed_position_CYL_up_btn, 6, 8, 1, 1)

        self.clean_fixed_position_CYL_down_btn = QPushButton(self.gridLayoutWidget_2)
        self.clean_fixed_position_CYL_down_btn.setObjectName(
            "clean_fixed_position_CYL_down_btn"
        )
        self.clean_fixed_position_CYL_down_btn.setEnabled(False)

        self.gridLayout_2.addWidget(self.clean_fixed_position_CYL_down_btn, 6, 6, 1, 1)

        self.clean_stopper_cyl_up_btn = QPushButton(self.gridLayoutWidget_2)
        self.clean_stopper_cyl_up_btn.setObjectName("clean_stopper_cyl_up_btn")
        self.clean_stopper_cyl_up_btn.setEnabled(False)

        self.gridLayout_2.addWidget(self.clean_stopper_cyl_up_btn, 4, 4, 1, 1)

        self.horizontalSpacer_18 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.gridLayout_2.addItem(self.horizontalSpacer_18, 0, 11, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget_2)
        self.label_2.setObjectName("label_2")

        self.gridLayout_2.addWidget(self.label_2, 4, 2, 1, 1, Qt.AlignHCenter)

        self.label_4 = QLabel(self.gridLayoutWidget_2)
        self.label_4.setObjectName("label_4")

        self.gridLayout_2.addWidget(self.label_4, 6, 2, 1, 1, Qt.AlignHCenter)

        self.horizontalSpacer_22 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.gridLayout_2.addItem(self.horizontalSpacer_22, 0, 9, 1, 1)

        self.horizontalSpacer_23 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.gridLayout_2.addItem(self.horizontalSpacer_23, 0, 3, 1, 1)

        self.horizontalSpacer_24 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.gridLayout_2.addItem(self.horizontalSpacer_24, 0, 5, 1, 1)

        self.verticalSpacer_13 = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.gridLayout_2.addItem(self.verticalSpacer_13, 5, 0, 1, 1)

        self.horizontalSpacer_21 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.gridLayout_2.addItem(self.horizontalSpacer_21, 0, 7, 1, 1)

        self.clean_stopper_cyl_down_btn = QPushButton(self.gridLayoutWidget_2)
        self.clean_stopper_cyl_down_btn.setObjectName("clean_stopper_cyl_down_btn")
        self.clean_stopper_cyl_down_btn.setEnabled(False)

        self.gridLayout_2.addWidget(self.clean_stopper_cyl_down_btn, 4, 6, 1, 1)

        self.label_17 = QLabel(self.gridLayoutWidget_2)
        self.label_17.setObjectName("label_17")

        self.gridLayout_2.addWidget(self.label_17, 1, 5, 1, 1, Qt.AlignHCenter)

        self.label_20 = QLabel(self.gridLayoutWidget_2)
        self.label_20.setObjectName("label_20")

        self.gridLayout_2.addWidget(self.label_20, 1, 9, 1, 1, Qt.AlignHCenter)

        self.check_stopper_cyl_down_btn = QPushButton(self.gridLayoutWidget_2)
        self.check_stopper_cyl_down_btn.setObjectName("check_stopper_cyl_down_btn")
        self.check_stopper_cyl_down_btn.setEnabled(False)

        self.gridLayout_2.addWidget(self.check_stopper_cyl_down_btn, 4, 10, 1, 1)

        self.check_stopper_cyl_up_btn = QPushButton(self.gridLayoutWidget_2)
        self.check_stopper_cyl_up_btn.setObjectName("check_stopper_cyl_up_btn")
        self.check_stopper_cyl_up_btn.setEnabled(False)

        self.gridLayout_2.addWidget(self.check_stopper_cyl_up_btn, 4, 8, 1, 1)

        self.clean_fixed_position_CYL_up_btn = QPushButton(self.gridLayoutWidget_2)
        self.clean_fixed_position_CYL_up_btn.setObjectName(
            "clean_fixed_position_CYL_up_btn"
        )
        self.clean_fixed_position_CYL_up_btn.setEnabled(False)

        self.gridLayout_2.addWidget(self.clean_fixed_position_CYL_up_btn, 6, 4, 1, 1)

        self.verticalSpacer_12 = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.gridLayout_2.addItem(self.verticalSpacer_12, 2, 0, 1, 1)

        self.horizontalLayoutWidget_8 = QWidget(self.tab_2)
        self.horizontalLayoutWidget_8.setObjectName("horizontalLayoutWidget_8")
        self.horizontalLayoutWidget_8.setGeometry(QRect(10, 260, 971, 41))
        self.horizontalLayout_8 = QHBoxLayout(self.horizontalLayoutWidget_8)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_18 = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.horizontalLayout_8.addItem(self.verticalSpacer_18)

        self.gridLayoutWidget_3 = QWidget(self.tab_2)
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(10, 310, 971, 128))
        self.gridLayout_4 = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_33 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.gridLayout_4.addItem(self.horizontalSpacer_33, 0, 3, 1, 1)

        self.horizontalSpacer_37 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.gridLayout_4.addItem(self.horizontalSpacer_37, 0, 9, 1, 1)

        self.verticalSpacer_20 = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.gridLayout_4.addItem(self.verticalSpacer_20, 3, 0, 1, 1)

        self.solenoid_value_off_btn = QPushButton(self.gridLayoutWidget_3)
        self.solenoid_value_off_btn.setObjectName("solenoid_value_off_btn")
        self.solenoid_value_off_btn.setEnabled(False)

        self.gridLayout_4.addWidget(self.solenoid_value_off_btn, 5, 6, 1, 1)

        self.label_22 = QLabel(self.gridLayoutWidget_3)
        self.label_22.setObjectName("label_22")

        self.gridLayout_4.addWidget(self.label_22, 5, 2, 1, 1, Qt.AlignHCenter)

        self.solenoid_value_on_btn = QPushButton(self.gridLayoutWidget_3)
        self.solenoid_value_on_btn.setObjectName("solenoid_value_on_btn")
        self.solenoid_value_on_btn.setEnabled(False)

        self.gridLayout_4.addWidget(self.solenoid_value_on_btn, 5, 4, 1, 1)

        self.horizontalSpacer_39 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.gridLayout_4.addItem(self.horizontalSpacer_39, 0, 14, 1, 1)

        self.blow_air_on_btn = QPushButton(self.gridLayoutWidget_3)
        self.blow_air_on_btn.setObjectName("blow_air_on_btn")
        self.blow_air_on_btn.setEnabled(False)

        self.gridLayout_4.addWidget(self.blow_air_on_btn, 5, 11, 1, 1)

        self.pomp_power_off_btn = QPushButton(self.gridLayoutWidget_3)
        self.pomp_power_off_btn.setObjectName("pomp_power_off_btn")
        self.pomp_power_off_btn.setEnabled(False)

        self.gridLayout_4.addWidget(self.pomp_power_off_btn, 2, 6, 1, 1)

        self.label_19 = QLabel(self.gridLayoutWidget_3)
        self.label_19.setObjectName("label_19")

        self.gridLayout_4.addWidget(self.label_19, 2, 8, 1, 1, Qt.AlignHCenter)

        self.blow_air_off_btn = QPushButton(self.gridLayoutWidget_3)
        self.blow_air_off_btn.setObjectName("blow_air_off_btn")
        self.blow_air_off_btn.setEnabled(False)

        self.gridLayout_4.addWidget(self.blow_air_off_btn, 5, 13, 1, 1)

        self.horizontalSpacer_32 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.gridLayout_4.addItem(self.horizontalSpacer_32, 0, 12, 1, 1)

        self.pomp_power_on_btn = QPushButton(self.gridLayoutWidget_3)
        self.pomp_power_on_btn.setObjectName("pomp_power_on_btn")
        self.pomp_power_on_btn.setEnabled(False)

        self.gridLayout_4.addWidget(self.pomp_power_on_btn, 2, 4, 1, 1)

        self.label_16 = QLabel(self.gridLayoutWidget_3)
        self.label_16.setObjectName("label_16")

        self.gridLayout_4.addWidget(self.label_16, 2, 2, 1, 1, Qt.AlignHCenter)

        self.laser_off_btn = QPushButton(self.gridLayoutWidget_3)
        self.laser_off_btn.setObjectName("laser_off_btn")
        self.laser_off_btn.setEnabled(False)

        self.gridLayout_4.addWidget(self.laser_off_btn, 2, 13, 1, 1)

        self.laser_on_btn = QPushButton(self.gridLayoutWidget_3)
        self.laser_on_btn.setObjectName("laser_on_btn")
        self.laser_on_btn.setEnabled(False)

        self.gridLayout_4.addWidget(self.laser_on_btn, 2, 11, 1, 1)

        self.label_23 = QLabel(self.gridLayoutWidget_3)
        self.label_23.setObjectName("label_23")

        self.gridLayout_4.addWidget(self.label_23, 5, 8, 1, 1, Qt.AlignHCenter)

        self.horizontalSpacer_34 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.gridLayout_4.addItem(self.horizontalSpacer_34, 0, 5, 1, 1)

        self.horizontalSpacer_35 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.gridLayout_4.addItem(self.horizontalSpacer_35, 0, 7, 1, 1)

        self.horizontalLayoutWidget_9 = QWidget(self.tab_2)
        self.horizontalLayoutWidget_9.setObjectName("horizontalLayoutWidget_9")
        self.horizontalLayoutWidget_9.setGeometry(QRect(10, 450, 971, 111))
        self.horizontalLayout_9 = QHBoxLayout(self.horizontalLayoutWidget_9)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_19 = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.horizontalLayout_9.addItem(self.verticalSpacer_19)

        self.horizontalLayoutWidget_10 = QWidget(self.tab_2)
        self.horizontalLayoutWidget_10.setObjectName("horizontalLayoutWidget_10")
        self.horizontalLayoutWidget_10.setGeometry(QRect(10, 570, 971, 71))
        self.horizontalLayout_10 = QHBoxLayout(self.horizontalLayoutWidget_10)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_31 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_10.addItem(self.horizontalSpacer_31)

        self.manual_startBtn = QPushButton(self.horizontalLayoutWidget_10)
        self.manual_startBtn.setObjectName("manual_startBtn")
        self.manual_startBtn.setEnabled(False)

        self.horizontalLayout_10.addWidget(self.manual_startBtn)

        self.horizontalSpacer_38 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_10.addItem(self.horizontalSpacer_38)

        self.manual_pauseBtn = QPushButton(self.horizontalLayoutWidget_10)
        self.manual_pauseBtn.setObjectName("manual_pauseBtn")
        self.manual_pauseBtn.setEnabled(False)

        self.horizontalLayout_10.addWidget(self.manual_pauseBtn)

        self.horizontalSpacer_40 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_10.addItem(self.horizontalSpacer_40)

        self.manual_restartBtn = QPushButton(self.horizontalLayoutWidget_10)
        self.manual_restartBtn.setObjectName("manual_restartBtn")
        self.manual_restartBtn.setEnabled(False)

        self.horizontalLayout_10.addWidget(self.manual_restartBtn)

        self.horizontalSpacer_41 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_10.addItem(self.horizontalSpacer_41)

        self.manual_stopBtn = QPushButton(self.horizontalLayoutWidget_10)
        self.manual_stopBtn.setObjectName("manual_stopBtn")
        self.manual_stopBtn.setEnabled(False)

        self.horizontalLayout_10.addWidget(self.manual_stopBtn)

        self.horizontalSpacer_42 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_10.addItem(self.horizontalSpacer_42)

        self.horizontalLayoutWidget_11 = QWidget(self.tab_2)
        self.horizontalLayoutWidget_11.setObjectName("horizontalLayoutWidget_11")
        self.horizontalLayoutWidget_11.setGeometry(QRect(10, 650, 971, 71))
        self.horizontalLayout_12 = QHBoxLayout(self.horizontalLayoutWidget_11)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_21 = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.horizontalLayout_12.addItem(self.verticalSpacer_21)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName("tab_3")
        self.horizontalLayoutWidget_12 = QWidget(self.tab_3)
        self.horizontalLayoutWidget_12.setObjectName("horizontalLayoutWidget_12")
        self.horizontalLayoutWidget_12.setGeometry(QRect(10, 10, 971, 41))
        self.horizontalLayout_13 = QHBoxLayout(self.horizontalLayoutWidget_12)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_25 = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.horizontalLayout_13.addItem(self.verticalSpacer_25)

        self.gridLayoutWidget_4 = QWidget(self.tab_3)
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.gridLayoutWidget_4.setGeometry(QRect(10, 60, 971, 48))
        self.gridLayout_5 = QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.sensor_A_detection_value_5 = QLineEdit(self.gridLayoutWidget_4)
        self.sensor_A_detection_value_5.setObjectName("sensor_A_detection_value_5")
        self.sensor_A_detection_value_5.setReadOnly(True)

        self.gridLayout_5.addWidget(self.sensor_A_detection_value_5, 3, 16, 1, 1)

        self.horizontalSpacer_43 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.gridLayout_5.addItem(self.horizontalSpacer_43, 1, 0, 1, 1)

        self.label_33 = QLabel(self.gridLayoutWidget_4)
        self.label_33.setObjectName("label_33")

        self.gridLayout_5.addWidget(self.label_33, 3, 10, 1, 1)

        self.horizontalSpacer_45 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.gridLayout_5.addItem(self.horizontalSpacer_45, 1, 7, 1, 1)

        self.horizontalSpacer_47 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.gridLayout_5.addItem(self.horizontalSpacer_47, 1, 3, 1, 1)

        self.label_29 = QLabel(self.gridLayoutWidget_4)
        self.label_29.setObjectName("label_29")

        self.gridLayout_5.addWidget(self.label_29, 3, 2, 1, 1, Qt.AlignHCenter)

        self.horizontalSpacer_48 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.gridLayout_5.addItem(self.horizontalSpacer_48, 1, 5, 1, 1)

        self.sensor_A_detection_value_3 = QLineEdit(self.gridLayoutWidget_4)
        self.sensor_A_detection_value_3.setObjectName("sensor_A_detection_value_3")
        self.sensor_A_detection_value_3.setReadOnly(True)

        self.gridLayout_5.addWidget(self.sensor_A_detection_value_3, 3, 12, 1, 1)

        self.label_32 = QLabel(self.gridLayoutWidget_4)
        self.label_32.setObjectName("label_32")

        self.gridLayout_5.addWidget(self.label_32, 3, 6, 1, 1, Qt.AlignHCenter)

        self.horizontalSpacer_44 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.gridLayout_5.addItem(self.horizontalSpacer_44, 1, 11, 1, 1)

        self.sensor_A_face_width_2 = QLineEdit(self.gridLayoutWidget_4)
        self.sensor_A_face_width_2.setObjectName("sensor_A_face_width_2")
        self.sensor_A_face_width_2.setReadOnly(True)

        self.gridLayout_5.addWidget(self.sensor_A_face_width_2, 3, 8, 1, 1)

        self.label_35 = QLabel(self.gridLayoutWidget_4)
        self.label_35.setObjectName("label_35")

        self.gridLayout_5.addWidget(self.label_35, 3, 14, 1, 1)

        self.sensor_A_end_angle_2 = QLineEdit(self.gridLayoutWidget_4)
        self.sensor_A_end_angle_2.setObjectName("sensor_A_end_angle_2")
        self.sensor_A_end_angle_2.setEnabled(True)
        self.sensor_A_end_angle_2.setReadOnly(True)

        self.gridLayout_5.addWidget(self.sensor_A_end_angle_2, 3, 4, 1, 1)

        self.horizontalSpacer_51 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.gridLayout_5.addItem(self.horizontalSpacer_51, 1, 15, 1, 1)

        self.horizontalSpacer_50 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.gridLayout_5.addItem(self.horizontalSpacer_50, 1, 13, 1, 1)

        self.horizontalSpacer_46 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.gridLayout_5.addItem(self.horizontalSpacer_46, 1, 9, 1, 1)

        self.horizontalSpacer_55 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.gridLayout_5.addItem(self.horizontalSpacer_55, 1, 17, 1, 1)

        self.horizontalLayoutWidget_13 = QWidget(self.tab_3)
        self.horizontalLayoutWidget_13.setObjectName("horizontalLayoutWidget_13")
        self.horizontalLayoutWidget_13.setGeometry(QRect(10, 120, 971, 91))
        self.horizontalLayout_14 = QHBoxLayout(self.horizontalLayoutWidget_13)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_26 = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.horizontalLayout_14.addItem(self.verticalSpacer_26)

        self.gridLayoutWidget_5 = QWidget(self.tab_3)
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")
        self.gridLayoutWidget_5.setGeometry(QRect(10, 220, 971, 238))
        self.gridLayout_6 = QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_31 = QLabel(self.gridLayoutWidget_5)
        self.label_31.setObjectName("label_31")

        self.gridLayout_6.addWidget(self.label_31, 1, 4, 1, 1, Qt.AlignHCenter)

        self.verticalSpacer_14 = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.gridLayout_6.addItem(self.verticalSpacer_14, 2, 0, 1, 1)

        self.label_30 = QLabel(self.gridLayoutWidget_5)
        self.label_30.setObjectName("label_30")

        self.gridLayout_6.addWidget(self.label_30, 3, 2, 1, 1, Qt.AlignHCenter)

        self.label_36 = QLabel(self.gridLayoutWidget_5)
        self.label_36.setObjectName("label_36")

        self.gridLayout_6.addWidget(self.label_36, 7, 2, 1, 1, Qt.AlignHCenter)

        self.verticalSpacer_22 = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.gridLayout_6.addItem(self.verticalSpacer_22, 4, 0, 1, 1)

        self.label_34 = QLabel(self.gridLayoutWidget_5)
        self.label_34.setObjectName("label_34")

        self.gridLayout_6.addWidget(self.label_34, 5, 2, 1, 1, Qt.AlignHCenter)

        self.label_38 = QLabel(self.gridLayoutWidget_5)
        self.label_38.setObjectName("label_38")

        self.gridLayout_6.addWidget(self.label_38, 1, 6, 1, 1, Qt.AlignHCenter)

        self.horizontalSpacer_53 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.gridLayout_6.addItem(self.horizontalSpacer_53, 1, 3, 1, 1)

        self.horizontalSpacer_54 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.gridLayout_6.addItem(self.horizontalSpacer_54, 1, 5, 1, 1)

        self.sensor_A_face_width_3 = QLineEdit(self.gridLayoutWidget_5)
        self.sensor_A_face_width_3.setObjectName("sensor_A_face_width_3")
        self.sensor_A_face_width_3.setReadOnly(True)

        self.gridLayout_6.addWidget(self.sensor_A_face_width_3, 3, 6, 1, 1)

        self.sensor_A_end_angle_3 = QLineEdit(self.gridLayoutWidget_5)
        self.sensor_A_end_angle_3.setObjectName("sensor_A_end_angle_3")
        self.sensor_A_end_angle_3.setEnabled(True)
        self.sensor_A_end_angle_3.setReadOnly(True)

        self.gridLayout_6.addWidget(self.sensor_A_end_angle_3, 3, 4, 1, 1)

        self.horizontalSpacer_58 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.gridLayout_6.addItem(self.horizontalSpacer_58, 1, 7, 1, 1)

        self.horizontalSpacer_49 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.gridLayout_6.addItem(self.horizontalSpacer_49, 1, 0, 1, 1)

        self.sensor_A_detection_value_4 = QLineEdit(self.gridLayoutWidget_5)
        self.sensor_A_detection_value_4.setObjectName("sensor_A_detection_value_4")
        self.sensor_A_detection_value_4.setReadOnly(True)

        self.gridLayout_6.addWidget(self.sensor_A_detection_value_4, 3, 8, 1, 1)

        self.label_39 = QLabel(self.gridLayoutWidget_5)
        self.label_39.setObjectName("label_39")

        self.gridLayout_6.addWidget(self.label_39, 1, 8, 1, 1, Qt.AlignHCenter)

        self.horizontalSpacer_56 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.gridLayout_6.addItem(self.horizontalSpacer_56, 1, 10, 1, 1)

        self.verticalSpacer_27 = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.gridLayout_6.addItem(self.verticalSpacer_27, 6, 0, 1, 1)

        self.sensor_A_end_angle_4 = QLineEdit(self.gridLayoutWidget_5)
        self.sensor_A_end_angle_4.setObjectName("sensor_A_end_angle_4")
        self.sensor_A_end_angle_4.setEnabled(True)
        self.sensor_A_end_angle_4.setReadOnly(True)

        self.gridLayout_6.addWidget(self.sensor_A_end_angle_4, 5, 4, 1, 1)

        self.sensor_A_end_angle_5 = QLineEdit(self.gridLayoutWidget_5)
        self.sensor_A_end_angle_5.setObjectName("sensor_A_end_angle_5")
        self.sensor_A_end_angle_5.setEnabled(True)
        self.sensor_A_end_angle_5.setReadOnly(True)

        self.gridLayout_6.addWidget(self.sensor_A_end_angle_5, 5, 6, 1, 1)

        self.sensor_A_end_angle_6 = QLineEdit(self.gridLayoutWidget_5)
        self.sensor_A_end_angle_6.setObjectName("sensor_A_end_angle_6")
        self.sensor_A_end_angle_6.setEnabled(True)
        self.sensor_A_end_angle_6.setReadOnly(True)

        self.gridLayout_6.addWidget(self.sensor_A_end_angle_6, 5, 8, 1, 1)

        self.sensor_A_end_angle_7 = QLineEdit(self.gridLayoutWidget_5)
        self.sensor_A_end_angle_7.setObjectName("sensor_A_end_angle_7")
        self.sensor_A_end_angle_7.setEnabled(True)
        self.sensor_A_end_angle_7.setReadOnly(True)

        self.gridLayout_6.addWidget(self.sensor_A_end_angle_7, 7, 4, 1, 1)

        self.sensor_A_end_angle_8 = QLineEdit(self.gridLayoutWidget_5)
        self.sensor_A_end_angle_8.setObjectName("sensor_A_end_angle_8")
        self.sensor_A_end_angle_8.setEnabled(True)
        self.sensor_A_end_angle_8.setReadOnly(True)

        self.gridLayout_6.addWidget(self.sensor_A_end_angle_8, 7, 6, 1, 1)

        self.sensor_A_end_angle_9 = QLineEdit(self.gridLayoutWidget_5)
        self.sensor_A_end_angle_9.setObjectName("sensor_A_end_angle_9")
        self.sensor_A_end_angle_9.setEnabled(True)
        self.sensor_A_end_angle_9.setReadOnly(True)

        self.gridLayout_6.addWidget(self.sensor_A_end_angle_9, 7, 8, 1, 1)

        self.horizontalLayoutWidget_14 = QWidget(self.tab_3)
        self.horizontalLayoutWidget_14.setObjectName("horizontalLayoutWidget_14")
        self.horizontalLayoutWidget_14.setGeometry(QRect(10, 470, 971, 251))
        self.horizontalLayout_15 = QHBoxLayout(self.horizontalLayoutWidget_14)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_28 = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.horizontalLayout_15.addItem(self.verticalSpacer_28)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tabWidget.addTab(self.tab_4, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "MainWindow", None)
        )
        self.label_9.setText(
            QCoreApplication.translate("MainWindow", "\u76ee\u6a19\u503c", None)
        )
        self.label_8.setText(
            QCoreApplication.translate("MainWindow", "\u6aa2\u6e2c\u503c", None)
        )
        self.label_6.setText(
            QCoreApplication.translate("MainWindow", "\u76f4\u89d2\u5ea6", None)
        )
        self.label_5.setText(
            QCoreApplication.translate("MainWindow", "\u7aef\u9762\u89d2\u5ea6", None)
        )
        self.label_3.setText(
            QCoreApplication.translate("MainWindow", "B \u93e1\u982d", None)
        )
        self.label.setText(
            QCoreApplication.translate("MainWindow", "A \u93e1\u982d", None)
        )
        self.label_7.setText(
            QCoreApplication.translate("MainWindow", "\u7aef\u9762\u5bec\u5ea6", None)
        )
        self.label_11.setText(
            QCoreApplication.translate(
                "MainWindow", "\u6700\u7d42\u6aa2\u6e2c\u7d50\u679c", None
            )
        )
        self.startBtn.setText(
            QCoreApplication.translate("MainWindow", "\u958b\u59cb", None)
        )
        self.auto_control_btn.setText(
            QCoreApplication.translate("MainWindow", "\u81ea\u52d5\u63a7\u5236", None)
        )
        self.pauseBtn.setText(
            QCoreApplication.translate("MainWindow", "\u66ab\u505c", None)
        )
        self.restartBtn.setText(
            QCoreApplication.translate("MainWindow", "\u91cd\u555f", None)
        )
        self.stopBtn.setText(
            QCoreApplication.translate("MainWindow", "\u505c\u6b62", None)
        )
        self.label_12.setText(
            QCoreApplication.translate("MainWindow", "\u8a08\u6578", None)
        )
        self.label_13.setText(
            QCoreApplication.translate(
                "MainWindow", "\u751f\u7522\u7e3d\u6578\u91cf", None
            )
        )
        self.label_14.setText(
            QCoreApplication.translate("MainWindow", "NG \u7e3d\u6578\u91cf", None)
        )
        self.label_10.setText(
            QCoreApplication.translate(
                "MainWindow", "Keyence Sensor \u9023\u7dda\u72c0\u614b : ", None
            )
        )
        self.keyence_connect_status.setText("")
        self.label_15.setText(
            QCoreApplication.translate(
                "MainWindow", "I/O \u9023\u7dda\u72c0\u614b : ", None
            )
        )
        self.io_connect_status.setText("")
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab),
            QCoreApplication.translate("MainWindow", "\u9996\u9801", None),
        )
        self.check_fixed_position_CYL_down_btn.setText(
            QCoreApplication.translate("MainWindow", "\u4e0b\u964d", None)
        )
        self.check_fixed_position_CYL_up_btn.setText(
            QCoreApplication.translate("MainWindow", "\u4e0a\u5347", None)
        )
        self.clean_fixed_position_CYL_down_btn.setText(
            QCoreApplication.translate("MainWindow", "\u4e0b\u964d", None)
        )
        self.clean_stopper_cyl_up_btn.setText(
            QCoreApplication.translate("MainWindow", "\u4e0a\u5347", None)
        )
        self.label_2.setText(
            QCoreApplication.translate(
                "MainWindow", "Stopper \u78c1\u7c27\u958b\u95dc", None
            )
        )
        self.label_4.setText(
            QCoreApplication.translate(
                "MainWindow", "Position \u78c1\u7c27\u958b\u95dc", None
            )
        )
        self.clean_stopper_cyl_down_btn.setText(
            QCoreApplication.translate("MainWindow", "\u4e0b\u964d", None)
        )
        self.label_17.setText(
            QCoreApplication.translate("MainWindow", "\u6e05\u6d17\u88fd\u7a0b", None)
        )
        self.label_20.setText(
            QCoreApplication.translate("MainWindow", "\u6aa2\u67e5\u88fd\u7a0b", None)
        )
        self.check_stopper_cyl_down_btn.setText(
            QCoreApplication.translate("MainWindow", "\u4e0b\u964d", None)
        )
        self.check_stopper_cyl_up_btn.setText(
            QCoreApplication.translate("MainWindow", "\u4e0a\u5347", None)
        )
        self.clean_fixed_position_CYL_up_btn.setText(
            QCoreApplication.translate("MainWindow", "\u4e0a\u5347", None)
        )
        self.solenoid_value_off_btn.setText(
            QCoreApplication.translate("MainWindow", "\u95dc\u9589", None)
        )
        self.label_22.setText(
            QCoreApplication.translate("MainWindow", "\u96fb\u78c1\u95a5", None)
        )
        self.solenoid_value_on_btn.setText(
            QCoreApplication.translate("MainWindow", "\u6253\u958b", None)
        )
        self.blow_air_on_btn.setText(
            QCoreApplication.translate("MainWindow", "\u6253\u958b", None)
        )
        self.pomp_power_off_btn.setText(
            QCoreApplication.translate("MainWindow", "\u95dc\u9589", None)
        )
        self.label_19.setText(
            QCoreApplication.translate("MainWindow", "\u96f7\u5c04\u6a5f\u69cb", None)
        )
        self.blow_air_off_btn.setText(
            QCoreApplication.translate("MainWindow", "\u95dc\u9589", None)
        )
        self.pomp_power_on_btn.setText(
            QCoreApplication.translate("MainWindow", "\u6253\u958b", None)
        )
        self.label_16.setText(
            QCoreApplication.translate("MainWindow", "Pump \u96fb\u6e90", None)
        )
        self.laser_off_btn.setText(
            QCoreApplication.translate("MainWindow", "\u95dc\u9589", None)
        )
        self.laser_on_btn.setText(
            QCoreApplication.translate("MainWindow", "\u6253\u958b", None)
        )
        self.label_23.setText(
            QCoreApplication.translate("MainWindow", "\u5439\u6c23", None)
        )
        self.manual_startBtn.setText(
            QCoreApplication.translate("MainWindow", "\u958b\u59cb", None)
        )
        self.manual_pauseBtn.setText(
            QCoreApplication.translate("MainWindow", "\u66ab\u505c", None)
        )
        self.manual_restartBtn.setText(
            QCoreApplication.translate("MainWindow", "\u91cd\u555f", None)
        )
        self.manual_stopBtn.setText(
            QCoreApplication.translate("MainWindow", "\u505c\u6b62", None)
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_2),
            QCoreApplication.translate("MainWindow", "\u624b\u52d5\u63a7\u5236", None),
        )
        self.label_33.setText(
            QCoreApplication.translate("MainWindow", "\u92fc\u7ba1\u9577\u5ea6", None)
        )
        self.label_29.setText(
            QCoreApplication.translate("MainWindow", "\u751f\u7522\u7de8\u865f", None)
        )
        self.label_32.setText(
            QCoreApplication.translate("MainWindow", "\u92fc\u7ba1\u76f4\u5f91", None)
        )
        self.label_35.setText(
            QCoreApplication.translate("MainWindow", "\u92fc\u7ba1\u9577\u5ea6", None)
        )
        self.label_31.setText(
            QCoreApplication.translate("MainWindow", "\u76ee\u6a19\u503c", None)
        )
        self.label_30.setText(
            QCoreApplication.translate("MainWindow", "\u7aef\u9762\u89d2\u5ea6", None)
        )
        self.label_36.setText(
            QCoreApplication.translate("MainWindow", "\u7aef\u9762\u5bec\u5ea6", None)
        )
        self.label_34.setText(
            QCoreApplication.translate("MainWindow", "\u76f4\u89d2\u5ea6", None)
        )
        self.label_38.setText(
            QCoreApplication.translate(
                "MainWindow", "\u6700\u5927\u5bb9\u8a31\u503c", None
            )
        )
        self.label_39.setText(
            QCoreApplication.translate(
                "MainWindow", "\u6700\u5c0f\u5bb9\u8a31\u503c", None
            )
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_3),
            QCoreApplication.translate("MainWindow", "\u8a2d\u5b9a", None),
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_4),
            QCoreApplication.translate("MainWindow", "\u7570\u5e38\u7d00\u9304", None),
        )

    # retranslateUi
