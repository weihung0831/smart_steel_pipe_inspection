# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerTFJSAV.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QTabWidget, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1024, 768)
        MainWindow.setMinimumSize(QSize(1024, 768))
        MainWindow.setMaximumSize(QSize(1024, 768))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 1591, 751))
        font = QFont()
        font.setPointSize(9)
        self.tabWidget.setFont(font)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.frame = QFrame(self.tab)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(20, 143, 991, 571))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayoutWidget_5 = QWidget(self.frame)
        self.gridLayoutWidget_5.setObjectName(u"gridLayoutWidget_5")
        self.gridLayoutWidget_5.setGeometry(QRect(20, 80, 196, 63))
        self.gridLayout_18 = QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.gridLayout_18.setContentsMargins(0, 0, 0, 0)
        self.stop_btn = QPushButton(self.gridLayoutWidget_5)
        self.stop_btn.setObjectName(u"stop_btn")

        self.gridLayout_18.addWidget(self.stop_btn, 0, 2, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(10, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_18.addItem(self.horizontalSpacer_5, 0, 3, 1, 1)

        self.power_btn = QPushButton(self.gridLayoutWidget_5)
        self.power_btn.setObjectName(u"power_btn")

        self.gridLayout_18.addWidget(self.power_btn, 0, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(10, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_18.addItem(self.horizontalSpacer_4, 0, 1, 1, 1)

        self.verticalSpacer_1 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_18.addItem(self.verticalSpacer_1, 1, 0, 1, 1)

        self.gridLayoutWidget_7 = QWidget(self.frame)
        self.gridLayoutWidget_7.setObjectName(u"gridLayoutWidget_7")
        self.gridLayoutWidget_7.setGeometry(QRect(510, 170, 461, 191))
        self.gridLayout_22 = QGridLayout(self.gridLayoutWidget_7)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.gridLayout_22.setContentsMargins(0, 0, 0, 0)
        self.check_stopper_cyl_label = QLabel(self.gridLayoutWidget_7)
        self.check_stopper_cyl_label.setObjectName(u"check_stopper_cyl_label")
        font1 = QFont()
        font1.setFamilies([u"Cascadia Code"])
        font1.setPointSize(14)
        self.check_stopper_cyl_label.setFont(font1)

        self.gridLayout_22.addWidget(self.check_stopper_cyl_label, 4, 0, 1, 1, Qt.AlignHCenter)

        self.check_stopper_cyl_down_btn = QPushButton(self.gridLayoutWidget_7)
        self.check_stopper_cyl_down_btn.setObjectName(u"check_stopper_cyl_down_btn")

        self.gridLayout_22.addWidget(self.check_stopper_cyl_down_btn, 4, 4, 1, 1)

        self.check_fixed_position_CYL_label = QLabel(self.gridLayoutWidget_7)
        self.check_fixed_position_CYL_label.setObjectName(u"check_fixed_position_CYL_label")
        self.check_fixed_position_CYL_label.setFont(font1)

        self.gridLayout_22.addWidget(self.check_fixed_position_CYL_label, 6, 0, 1, 1, Qt.AlignHCenter)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_22.addItem(self.horizontalSpacer_9, 0, 1, 1, 1)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_22.addItem(self.horizontalSpacer_10, 0, 3, 1, 1)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_22.addItem(self.horizontalSpacer_11, 0, 5, 1, 1)

        self.check_fixed_position_CYL_down_btn = QPushButton(self.gridLayoutWidget_7)
        self.check_fixed_position_CYL_down_btn.setObjectName(u"check_fixed_position_CYL_down_btn")

        self.gridLayout_22.addWidget(self.check_fixed_position_CYL_down_btn, 6, 4, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_22.addItem(self.verticalSpacer_7, 2, 0, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_22.addItem(self.verticalSpacer_6, 0, 0, 1, 1)

        self.check_fixed_position_CYL_up_btn = QPushButton(self.gridLayoutWidget_7)
        self.check_fixed_position_CYL_up_btn.setObjectName(u"check_fixed_position_CYL_up_btn")

        self.gridLayout_22.addWidget(self.check_fixed_position_CYL_up_btn, 6, 2, 1, 1, Qt.AlignHCenter)

        self.check_stopper_cyl_up_btn = QPushButton(self.gridLayoutWidget_7)
        self.check_stopper_cyl_up_btn.setObjectName(u"check_stopper_cyl_up_btn")

        self.gridLayout_22.addWidget(self.check_stopper_cyl_up_btn, 4, 2, 1, 1, Qt.AlignHCenter)

        self.check_label = QLabel(self.gridLayoutWidget_7)
        self.check_label.setObjectName(u"check_label")
        self.check_label.setFont(font1)

        self.gridLayout_22.addWidget(self.check_label, 1, 0, 1, 1, Qt.AlignHCenter)

        self.verticalSpacer_8 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_22.addItem(self.verticalSpacer_8, 5, 0, 1, 1)

        self.verticalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_22.addItem(self.verticalSpacer_9, 7, 0, 1, 1)

        self.gridLayoutWidget_6 = QWidget(self.frame)
        self.gridLayoutWidget_6.setObjectName(u"gridLayoutWidget_6")
        self.gridLayoutWidget_6.setGeometry(QRect(20, 170, 471, 191))
        self.gridLayout_23 = QGridLayout(self.gridLayoutWidget_6)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.gridLayout_23.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_23.addItem(self.verticalSpacer_3, 2, 0, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_23.addItem(self.horizontalSpacer_6, 0, 1, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_23.addItem(self.verticalSpacer_5, 6, 0, 1, 1)

        self.clean_fixed_position_CYL_up_btn = QPushButton(self.gridLayoutWidget_6)
        self.clean_fixed_position_CYL_up_btn.setObjectName(u"clean_fixed_position_CYL_up_btn")

        self.gridLayout_23.addWidget(self.clean_fixed_position_CYL_up_btn, 5, 2, 1, 1, Qt.AlignHCenter)

        self.clean_stopper_cyl_label = QLabel(self.gridLayoutWidget_6)
        self.clean_stopper_cyl_label.setObjectName(u"clean_stopper_cyl_label")
        self.clean_stopper_cyl_label.setFont(font1)

        self.gridLayout_23.addWidget(self.clean_stopper_cyl_label, 3, 0, 1, 1, Qt.AlignHCenter)

        self.clean_fixed_position_CYL_label = QLabel(self.gridLayoutWidget_6)
        self.clean_fixed_position_CYL_label.setObjectName(u"clean_fixed_position_CYL_label")
        self.clean_fixed_position_CYL_label.setFont(font1)

        self.gridLayout_23.addWidget(self.clean_fixed_position_CYL_label, 5, 0, 1, 1, Qt.AlignHCenter)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_23.addItem(self.verticalSpacer_2, 0, 0, 1, 1)

        self.clean_label = QLabel(self.gridLayoutWidget_6)
        self.clean_label.setObjectName(u"clean_label")
        self.clean_label.setFont(font1)

        self.gridLayout_23.addWidget(self.clean_label, 1, 0, 1, 1, Qt.AlignHCenter)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_23.addItem(self.horizontalSpacer_7, 0, 3, 1, 1)

        self.clean_stopper_cyl_up_btn = QPushButton(self.gridLayoutWidget_6)
        self.clean_stopper_cyl_up_btn.setObjectName(u"clean_stopper_cyl_up_btn")

        self.gridLayout_23.addWidget(self.clean_stopper_cyl_up_btn, 3, 2, 1, 1, Qt.AlignHCenter)

        self.clean_fixed_position_CYL_down_btn = QPushButton(self.gridLayoutWidget_6)
        self.clean_fixed_position_CYL_down_btn.setObjectName(u"clean_fixed_position_CYL_down_btn")

        self.gridLayout_23.addWidget(self.clean_fixed_position_CYL_down_btn, 5, 4, 1, 1)

        self.clean_stopper_cyl_down_btn = QPushButton(self.gridLayoutWidget_6)
        self.clean_stopper_cyl_down_btn.setObjectName(u"clean_stopper_cyl_down_btn")

        self.gridLayout_23.addWidget(self.clean_stopper_cyl_down_btn, 3, 4, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_23.addItem(self.horizontalSpacer_8, 0, 5, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_23.addItem(self.verticalSpacer_4, 4, 0, 1, 1)

        self.gridLayoutWidget_8 = QWidget(self.frame)
        self.gridLayoutWidget_8.setObjectName(u"gridLayoutWidget_8")
        self.gridLayoutWidget_8.setGeometry(QRect(20, 380, 471, 171))
        self.gridLayout_24 = QGridLayout(self.gridLayoutWidget_8)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.gridLayout_24.setContentsMargins(0, 0, 0, 0)
        self.pomp_check_CYL_open_btn = QPushButton(self.gridLayoutWidget_8)
        self.pomp_check_CYL_open_btn.setObjectName(u"pomp_check_CYL_open_btn")

        self.gridLayout_24.addWidget(self.pomp_check_CYL_open_btn, 6, 2, 1, 1)

        self.pomp_label = QLabel(self.gridLayoutWidget_8)
        self.pomp_label.setObjectName(u"pomp_label")
        self.pomp_label.setFont(font1)

        self.gridLayout_24.addWidget(self.pomp_label, 1, 0, 1, 1, Qt.AlignHCenter)

        self.pomp_power_label = QLabel(self.gridLayoutWidget_8)
        self.pomp_power_label.setObjectName(u"pomp_power_label")
        self.pomp_power_label.setFont(font1)

        self.gridLayout_24.addWidget(self.pomp_power_label, 4, 0, 1, 1, Qt.AlignHCenter)

        self.pomp_check_CYL_close_btn = QPushButton(self.gridLayoutWidget_8)
        self.pomp_check_CYL_close_btn.setObjectName(u"pomp_check_CYL_close_btn")

        self.gridLayout_24.addWidget(self.pomp_check_CYL_close_btn, 6, 5, 1, 1)

        self.pomp_check_CYL_label = QLabel(self.gridLayoutWidget_8)
        self.pomp_check_CYL_label.setObjectName(u"pomp_check_CYL_label")
        self.pomp_check_CYL_label.setFont(font1)

        self.gridLayout_24.addWidget(self.pomp_check_CYL_label, 6, 0, 1, 1, Qt.AlignHCenter)

        self.verticalSpacer_11 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_24.addItem(self.verticalSpacer_11, 2, 0, 1, 1)

        self.pomp_power_close_btn = QPushButton(self.gridLayoutWidget_8)
        self.pomp_power_close_btn.setObjectName(u"pomp_power_close_btn")

        self.gridLayout_24.addWidget(self.pomp_power_close_btn, 4, 5, 1, 1)

        self.verticalSpacer_12 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_24.addItem(self.verticalSpacer_12, 5, 0, 1, 1)

        self.verticalSpacer_10 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_24.addItem(self.verticalSpacer_10, 0, 0, 1, 1)

        self.pomp_power_open_btn = QPushButton(self.gridLayoutWidget_8)
        self.pomp_power_open_btn.setObjectName(u"pomp_power_open_btn")

        self.gridLayout_24.addWidget(self.pomp_power_open_btn, 4, 2, 1, 1, Qt.AlignHCenter)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_24.addItem(self.horizontalSpacer_12, 0, 1, 1, 1)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_24.addItem(self.horizontalSpacer_13, 0, 4, 1, 1)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_24.addItem(self.horizontalSpacer_14, 0, 6, 1, 1)

        self.layoutWidget = QWidget(self.frame)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 20, 202, 34))
        self.gridLayout_7 = QGridLayout(self.layoutWidget)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.action_setting = QLabel(self.layoutWidget)
        self.action_setting.setObjectName(u"action_setting")
        font2 = QFont()
        font2.setFamilies([u"Cascadia Code"])
        font2.setPointSize(20)
        self.action_setting.setFont(font2)

        self.gridLayout_7.addWidget(self.action_setting, 0, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_3, 0, 1, 1, 1)

        self.gridLayoutWidget_9 = QWidget(self.frame)
        self.gridLayoutWidget_9.setObjectName(u"gridLayoutWidget_9")
        self.gridLayoutWidget_9.setGeometry(QRect(510, 380, 461, 171))
        self.gridLayout_25 = QGridLayout(self.gridLayoutWidget_9)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.gridLayout_25.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_14 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_25.addItem(self.verticalSpacer_14, 3, 0, 1, 1)

        self.verticalSpacer_13 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_25.addItem(self.verticalSpacer_13, 0, 0, 1, 1)

        self.air_value_close_btn = QPushButton(self.gridLayoutWidget_9)
        self.air_value_close_btn.setObjectName(u"air_value_close_btn")

        self.gridLayout_25.addWidget(self.air_value_close_btn, 6, 4, 1, 1)

        self.airValue_value_label = QLabel(self.gridLayoutWidget_9)
        self.airValue_value_label.setObjectName(u"airValue_value_label")
        self.airValue_value_label.setFont(font1)

        self.gridLayout_25.addWidget(self.airValue_value_label, 4, 0, 1, 1, Qt.AlignHCenter)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_25.addItem(self.horizontalSpacer_17, 0, 5, 1, 1)

        self.air_value_title_label = QLabel(self.gridLayoutWidget_9)
        self.air_value_title_label.setObjectName(u"air_value_title_label")
        self.air_value_title_label.setFont(font1)

        self.gridLayout_25.addWidget(self.air_value_title_label, 1, 0, 1, 1, Qt.AlignHCenter)

        self.air_value_label = QLabel(self.gridLayoutWidget_9)
        self.air_value_label.setObjectName(u"air_value_label")
        self.air_value_label.setFont(font1)

        self.gridLayout_25.addWidget(self.air_value_label, 6, 0, 1, 1, Qt.AlignHCenter)

        self.verticalSpacer_15 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_25.addItem(self.verticalSpacer_15, 5, 0, 1, 1)

        self.airValue_value_open_btn = QPushButton(self.gridLayoutWidget_9)
        self.airValue_value_open_btn.setObjectName(u"airValue_value_open_btn")

        self.gridLayout_25.addWidget(self.airValue_value_open_btn, 4, 2, 1, 1, Qt.AlignHCenter)

        self.airValue_value_close_btn = QPushButton(self.gridLayoutWidget_9)
        self.airValue_value_close_btn.setObjectName(u"airValue_value_close_btn")

        self.gridLayout_25.addWidget(self.airValue_value_close_btn, 4, 4, 1, 1)

        self.air_value_open_btn = QPushButton(self.gridLayoutWidget_9)
        self.air_value_open_btn.setObjectName(u"air_value_open_btn")

        self.gridLayout_25.addWidget(self.air_value_open_btn, 6, 2, 1, 1)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_25.addItem(self.horizontalSpacer_15, 0, 1, 1, 1)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_25.addItem(self.horizontalSpacer_16, 0, 3, 1, 1)

        self.gridLayoutWidget = QWidget(self.tab)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 10, 1021, 103))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_1, 1, 0, 1, 1)

        self.title = QLabel(self.gridLayoutWidget)
        self.title.setObjectName(u"title")
        self.title.setMinimumSize(QSize(216, 32))
        font3 = QFont()
        font3.setFamilies([u"Cascadia Code"])
        font3.setPointSize(48)
        self.title.setFont(font3)

        self.gridLayout.addWidget(self.title, 1, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        self.verticalSpacer_49 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_49, 0, 1, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.frame_2 = QFrame(self.tab_2)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(40, 180, 951, 485))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.lineEdit_5 = QLineEdit(self.frame_2)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setReadOnly(True)

        self.gridLayout_3.addWidget(self.lineEdit_5, 4, 7, 1, 1)

        self.lineEdit_8 = QLineEdit(self.frame_2)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setReadOnly(True)

        self.gridLayout_3.addWidget(self.lineEdit_8, 8, 7, 1, 1)

        self.lineEdit = QLineEdit(self.frame_2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setReadOnly(True)

        self.gridLayout_3.addWidget(self.lineEdit, 4, 3, 1, 1)

        self.verticalSpacer_48 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_48, 15, 0, 1, 1)

        self.lineEdit_14 = QLineEdit(self.frame_2)
        self.lineEdit_14.setObjectName(u"lineEdit_14")
        self.lineEdit_14.setReadOnly(True)

        self.gridLayout_3.addWidget(self.lineEdit_14, 14, 3, 1, 1)

        self.lineEdit_7 = QLineEdit(self.frame_2)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setReadOnly(True)

        self.gridLayout_3.addWidget(self.lineEdit_7, 6, 5, 1, 1)

        self.lineEdit_9 = QLineEdit(self.frame_2)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setReadOnly(True)

        self.gridLayout_3.addWidget(self.lineEdit_9, 8, 5, 1, 1)

        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font2)

        self.gridLayout_3.addWidget(self.label_2, 0, 1, 1, 1)

        self.lineEdit_4 = QLineEdit(self.frame_2)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setReadOnly(True)

        self.gridLayout_3.addWidget(self.lineEdit_4, 4, 5, 1, 1)

        self.horizontalSpacer_69 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_69, 0, 8, 1, 1)

        self.lineEdit_10 = QLineEdit(self.frame_2)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setReadOnly(True)

        self.gridLayout_3.addWidget(self.lineEdit_10, 12, 3, 1, 1)

        self.label_10 = QLabel(self.frame_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font1)

        self.gridLayout_3.addWidget(self.label_10, 12, 1, 1, 1, Qt.AlignHCenter)

        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.gridLayout_3.addWidget(self.label_5, 8, 1, 1, 1, Qt.AlignHCenter)

        self.label_12 = QLabel(self.frame_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font1)

        self.gridLayout_3.addWidget(self.label_12, 10, 5, 1, 1, Qt.AlignHCenter)

        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_21, 0, 2, 1, 1)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.horizontalSpacer_23 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_23, 0, 1, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_6, 0, 4, 1, 1)

        self.lineEdit_13 = QLineEdit(self.frame_2)
        self.lineEdit_13.setObjectName(u"lineEdit_13")
        self.lineEdit_13.setReadOnly(True)

        self.gridLayout_3.addWidget(self.lineEdit_13, 12, 7, 1, 1)

        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.gridLayout_3.addWidget(self.label_3, 4, 1, 1, 1, Qt.AlignHCenter)

        self.lineEdit_3 = QLineEdit(self.frame_2)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setReadOnly(True)

        self.gridLayout_3.addWidget(self.lineEdit_3, 8, 3, 1, 1)

        self.lineEdit_2 = QLineEdit(self.frame_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setReadOnly(True)

        self.gridLayout_3.addWidget(self.lineEdit_2, 6, 3, 1, 1)

        self.horizontalSpacer_68 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_68, 0, 6, 1, 1)

        self.verticalSpacer_47 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_47, 13, 0, 1, 1)

        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)

        self.gridLayout_3.addWidget(self.label_7, 2, 3, 1, 1, Qt.AlignHCenter)

        self.verticalSpacer_45 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_45, 7, 0, 1, 1)

        self.label_9 = QLabel(self.frame_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)

        self.gridLayout_3.addWidget(self.label_9, 2, 7, 1, 1, Qt.AlignHCenter)

        self.lineEdit_6 = QLineEdit(self.frame_2)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setReadOnly(True)

        self.gridLayout_3.addWidget(self.lineEdit_6, 6, 7, 1, 1)

        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)

        self.gridLayout_3.addWidget(self.label_6, 2, 1, 1, 1, Qt.AlignHCenter)

        self.verticalSpacer_36 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_36, 9, 0, 1, 1)

        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.gridLayout_3.addWidget(self.label_4, 6, 1, 1, 1, Qt.AlignHCenter)

        self.verticalSpacer_44 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_44, 5, 0, 1, 1)

        self.lineEdit_12 = QLineEdit(self.frame_2)
        self.lineEdit_12.setObjectName(u"lineEdit_12")
        self.lineEdit_12.setReadOnly(True)

        self.gridLayout_3.addWidget(self.lineEdit_12, 12, 5, 1, 1)

        self.label_11 = QLabel(self.frame_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font1)

        self.gridLayout_3.addWidget(self.label_11, 14, 1, 1, 1, Qt.AlignHCenter)

        self.verticalSpacer_43 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_43, 3, 0, 1, 1)

        self.label_13 = QLabel(self.frame_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font1)

        self.gridLayout_3.addWidget(self.label_13, 10, 7, 1, 1, Qt.AlignHCenter)

        self.label_8 = QLabel(self.frame_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)

        self.gridLayout_3.addWidget(self.label_8, 2, 5, 1, 1, Qt.AlignHCenter)

        self.verticalSpacer_25 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_25, 1, 0, 1, 1)

        self.verticalSpacer_50 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_50, 11, 0, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout_3)

        self.gridLayoutWidget_2 = QWidget(self.tab_2)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(0, 10, 1021, 103))
        self.gridLayout_4 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_61 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_61, 1, 2, 1, 1)

        self.horizontalSpacer_60 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_60, 1, 0, 1, 1)

        self.title2 = QLabel(self.gridLayoutWidget_2)
        self.title2.setObjectName(u"title2")
        self.title2.setMinimumSize(QSize(216, 32))
        self.title2.setFont(font3)

        self.gridLayout_4.addWidget(self.title2, 1, 1, 1, 1)

        self.verticalSpacer_46 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_46, 0, 1, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.frame_3 = QFrame(self.tab_6)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(35, 170, 941, 521))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_33 = QLabel(self.frame_3)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setFont(font1)

        self.gridLayout_5.addWidget(self.label_33, 10, 1, 1, 1, Qt.AlignHCenter)

        self.lineEdit_38 = QLineEdit(self.frame_3)
        self.lineEdit_38.setObjectName(u"lineEdit_38")
        self.lineEdit_38.setReadOnly(True)

        self.gridLayout_5.addWidget(self.lineEdit_38, 10, 3, 1, 1)

        self.lineEdit_40 = QLineEdit(self.frame_3)
        self.lineEdit_40.setObjectName(u"lineEdit_40")
        self.lineEdit_40.setReadOnly(False)

        self.gridLayout_5.addWidget(self.lineEdit_40, 4, 1, 1, 1)

        self.label_31 = QLabel(self.frame_3)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setFont(font1)

        self.gridLayout_5.addWidget(self.label_31, 2, 5, 1, 1, Qt.AlignHCenter)

        self.lineEdit_39 = QLineEdit(self.frame_3)
        self.lineEdit_39.setObjectName(u"lineEdit_39")
        self.lineEdit_39.setReadOnly(False)

        self.gridLayout_5.addWidget(self.lineEdit_39, 10, 5, 1, 1)

        self.lineEdit_35 = QLineEdit(self.frame_3)
        self.lineEdit_35.setObjectName(u"lineEdit_35")
        self.lineEdit_35.setReadOnly(False)

        self.gridLayout_5.addWidget(self.lineEdit_35, 8, 7, 1, 1)

        self.label_30 = QLabel(self.frame_3)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFont(font1)

        self.gridLayout_5.addWidget(self.label_30, 2, 1, 1, 1, Qt.AlignHCenter)

        self.label_37 = QLabel(self.frame_3)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setFont(font1)

        self.gridLayout_5.addWidget(self.label_37, 2, 3, 1, 1, Qt.AlignHCenter)

        self.lineEdit_41 = QLineEdit(self.frame_3)
        self.lineEdit_41.setObjectName(u"lineEdit_41")
        self.lineEdit_41.setReadOnly(True)

        self.gridLayout_5.addWidget(self.lineEdit_41, 4, 3, 1, 1)

        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.horizontalSpacer_30 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_30, 0, 1, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_8, 0, 4, 1, 1)

        self.label_40 = QLabel(self.frame_3)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setFont(font1)

        self.gridLayout_5.addWidget(self.label_40, 6, 5, 1, 1, Qt.AlignHCenter)

        self.label_28 = QLabel(self.frame_3)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font1)

        self.gridLayout_5.addWidget(self.label_28, 2, 7, 1, 1, Qt.AlignHCenter)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_20, 0, 8, 1, 1)

        self.verticalSpacer_56 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_56, 13, 0, 1, 1)

        self.verticalSpacer_60 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_60, 7, 0, 1, 1)

        self.verticalSpacer_64 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_64, 11, 0, 1, 1)

        self.label_32 = QLabel(self.frame_3)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setFont(font1)

        self.gridLayout_5.addWidget(self.label_32, 6, 1, 1, 1, Qt.AlignHCenter)

        self.lineEdit_43 = QLineEdit(self.frame_3)
        self.lineEdit_43.setObjectName(u"lineEdit_43")
        self.lineEdit_43.setReadOnly(True)

        self.gridLayout_5.addWidget(self.lineEdit_43, 4, 7, 1, 1)

        self.lineEdit_37 = QLineEdit(self.frame_3)
        self.lineEdit_37.setObjectName(u"lineEdit_37")
        self.lineEdit_37.setReadOnly(False)

        self.gridLayout_5.addWidget(self.lineEdit_37, 12, 5, 1, 1)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_19, 0, 6, 1, 1)

        self.lineEdit_32 = QLineEdit(self.frame_3)
        self.lineEdit_32.setObjectName(u"lineEdit_32")
        self.lineEdit_32.setReadOnly(True)

        self.gridLayout_5.addWidget(self.lineEdit_32, 14, 3, 1, 1)

        self.label_38 = QLabel(self.frame_3)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setFont(font1)

        self.gridLayout_5.addWidget(self.label_38, 6, 3, 1, 1, Qt.AlignHCenter)

        self.lineEdit_30 = QLineEdit(self.frame_3)
        self.lineEdit_30.setObjectName(u"lineEdit_30")
        self.lineEdit_30.setReadOnly(False)

        self.gridLayout_5.addWidget(self.lineEdit_30, 12, 7, 1, 1)

        self.lineEdit_28 = QLineEdit(self.frame_3)
        self.lineEdit_28.setObjectName(u"lineEdit_28")
        self.lineEdit_28.setReadOnly(False)

        self.gridLayout_5.addWidget(self.lineEdit_28, 8, 5, 1, 1)

        self.verticalSpacer_55 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_55, 5, 0, 1, 1)

        self.lineEdit_42 = QLineEdit(self.frame_3)
        self.lineEdit_42.setObjectName(u"lineEdit_42")
        self.lineEdit_42.setReadOnly(True)

        self.gridLayout_5.addWidget(self.lineEdit_42, 4, 5, 1, 1)

        self.verticalSpacer_59 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_59, 3, 0, 1, 1)

        self.lineEdit_29 = QLineEdit(self.frame_3)
        self.lineEdit_29.setObjectName(u"lineEdit_29")
        self.lineEdit_29.setReadOnly(True)

        self.gridLayout_5.addWidget(self.lineEdit_29, 12, 3, 1, 1)

        self.label_29 = QLabel(self.frame_3)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font1)

        self.gridLayout_5.addWidget(self.label_29, 12, 1, 1, 1, Qt.AlignHCenter)

        self.label_39 = QLabel(self.frame_3)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setFont(font1)

        self.gridLayout_5.addWidget(self.label_39, 6, 7, 1, 1, Qt.AlignHCenter)

        self.verticalSpacer_62 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_62, 9, 0, 1, 1)

        self.lineEdit_36 = QLineEdit(self.frame_3)
        self.lineEdit_36.setObjectName(u"lineEdit_36")
        self.lineEdit_36.setReadOnly(False)

        self.gridLayout_5.addWidget(self.lineEdit_36, 10, 7, 1, 1)

        self.verticalSpacer_58 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_58, 15, 0, 1, 1)

        self.label_36 = QLabel(self.frame_3)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setFont(font2)

        self.gridLayout_5.addWidget(self.label_36, 0, 1, 1, 1)

        self.label_34 = QLabel(self.frame_3)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setFont(font1)

        self.gridLayout_5.addWidget(self.label_34, 8, 1, 1, 1, Qt.AlignHCenter)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_18, 0, 2, 1, 1)

        self.lineEdit_34 = QLineEdit(self.frame_3)
        self.lineEdit_34.setObjectName(u"lineEdit_34")
        self.lineEdit_34.setReadOnly(True)

        self.gridLayout_5.addWidget(self.lineEdit_34, 8, 3, 1, 1)

        self.label_26 = QLabel(self.frame_3)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font1)

        self.gridLayout_5.addWidget(self.label_26, 14, 1, 1, 1, Qt.AlignHCenter)

        self.verticalSpacer_68 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_68, 1, 0, 1, 1)


        self.verticalLayout_6.addLayout(self.gridLayout_5)

        self.gridLayoutWidget_11 = QWidget(self.tab_6)
        self.gridLayoutWidget_11.setObjectName(u"gridLayoutWidget_11")
        self.gridLayoutWidget_11.setGeometry(QRect(0, 10, 1021, 103))
        self.gridLayout_12 = QGridLayout(self.gridLayoutWidget_11)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_70 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_12.addItem(self.horizontalSpacer_70, 1, 0, 1, 1)

        self.horizontalSpacer_71 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_12.addItem(self.horizontalSpacer_71, 1, 2, 1, 1)

        self.title3 = QLabel(self.gridLayoutWidget_11)
        self.title3.setObjectName(u"title3")
        self.title3.setMinimumSize(QSize(216, 32))
        self.title3.setFont(font3)

        self.gridLayout_12.addWidget(self.title3, 1, 1, 1, 1)

        self.verticalSpacer_51 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_12.addItem(self.verticalSpacer_51, 0, 1, 1, 1)

        self.tabWidget.addTab(self.tab_6, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.frame_4 = QFrame(self.tab_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(40, 170, 931, 261))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_4)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.gridLayout_13 = QGridLayout()
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.lineEdit_53 = QLineEdit(self.frame_4)
        self.lineEdit_53.setObjectName(u"lineEdit_53")
        self.lineEdit_53.setReadOnly(True)

        self.gridLayout_13.addWidget(self.lineEdit_53, 7, 1, 1, 1)

        self.horizontalSpacer_59 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer_59, 0, 5, 1, 1)

        self.lineEdit_31 = QLineEdit(self.frame_4)
        self.lineEdit_31.setObjectName(u"lineEdit_31")
        self.lineEdit_31.setReadOnly(True)

        self.gridLayout_13.addWidget(self.lineEdit_31, 5, 1, 1, 1)

        self.lineEdit_52 = QLineEdit(self.frame_4)
        self.lineEdit_52.setObjectName(u"lineEdit_52")
        self.lineEdit_52.setReadOnly(True)

        self.gridLayout_13.addWidget(self.lineEdit_52, 7, 4, 1, 1)

        self.verticalSpacer_63 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_13.addItem(self.verticalSpacer_63, 2, 0, 1, 1)

        self.horizontalSpacer_72 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer_72, 0, 3, 1, 1)

        self.lineEdit_48 = QLineEdit(self.frame_4)
        self.lineEdit_48.setObjectName(u"lineEdit_48")
        self.lineEdit_48.setReadOnly(True)

        self.gridLayout_13.addWidget(self.lineEdit_48, 5, 4, 1, 1)

        self.label_27 = QLabel(self.frame_4)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font2)

        self.gridLayout_13.addWidget(self.label_27, 0, 1, 1, 1, Qt.AlignHCenter)

        self.label_50 = QLabel(self.frame_4)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setFont(font1)

        self.gridLayout_13.addWidget(self.label_50, 2, 4, 1, 1, Qt.AlignHCenter)

        self.label_44 = QLabel(self.frame_4)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setFont(font1)

        self.gridLayout_13.addWidget(self.label_44, 3, 1, 1, 1, Qt.AlignHCenter)

        self.verticalSpacer_69 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_13.addItem(self.verticalSpacer_69, 4, 0, 1, 1)

        self.verticalSpacer_70 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_13.addItem(self.verticalSpacer_70, 6, 0, 1, 1)

        self.verticalSpacer_71 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_13.addItem(self.verticalSpacer_71, 8, 0, 1, 1)


        self.verticalLayout_8.addLayout(self.gridLayout_13)

        self.gridLayoutWidget_3 = QWidget(self.tab_3)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(0, 10, 1021, 103))
        self.gridLayout_9 = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_62 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_62, 1, 0, 1, 1)

        self.horizontalSpacer_63 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_63, 1, 2, 1, 1)

        self.title4 = QLabel(self.gridLayoutWidget_3)
        self.title4.setObjectName(u"title4")
        self.title4.setMinimumSize(QSize(216, 32))
        self.title4.setFont(font3)

        self.gridLayout_9.addWidget(self.title4, 1, 1, 1, 1)

        self.verticalSpacer_52 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_9.addItem(self.verticalSpacer_52, 0, 1, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.frame_5 = QFrame(self.tab_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(40, 180, 941, 221))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_5)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.gridLayout_15 = QGridLayout()
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.label_55 = QLabel(self.frame_5)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setFont(font1)

        self.gridLayout_15.addWidget(self.label_55, 3, 4, 1, 1, Qt.AlignHCenter)

        self.horizontalSpacer_33 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_15.addItem(self.horizontalSpacer_33, 0, 3, 1, 1)

        self.label_56 = QLabel(self.frame_5)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setFont(font1)

        self.gridLayout_15.addWidget(self.label_56, 3, 1, 1, 1, Qt.AlignHCenter)

        self.horizontalSpacer_31 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_15.addItem(self.horizontalSpacer_31, 0, 5, 1, 1)

        self.label_35 = QLabel(self.frame_5)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setFont(font2)

        self.gridLayout_15.addWidget(self.label_35, 0, 1, 1, 1, Qt.AlignHCenter)

        self.horizontalSpacer_32 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_15.addItem(self.horizontalSpacer_32, 0, 7, 1, 1)

        self.label_57 = QLabel(self.frame_5)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setFont(font1)

        self.gridLayout_15.addWidget(self.label_57, 3, 6, 1, 1, Qt.AlignHCenter)

        self.lineEdit_55 = QLineEdit(self.frame_5)
        self.lineEdit_55.setObjectName(u"lineEdit_55")
        self.lineEdit_55.setReadOnly(True)

        self.gridLayout_15.addWidget(self.lineEdit_55, 5, 4, 1, 1)

        self.lineEdit_59 = QLineEdit(self.frame_5)
        self.lineEdit_59.setObjectName(u"lineEdit_59")
        self.lineEdit_59.setReadOnly(True)

        self.gridLayout_15.addWidget(self.lineEdit_59, 5, 6, 1, 1)

        self.lineEdit_33 = QLineEdit(self.frame_5)
        self.lineEdit_33.setObjectName(u"lineEdit_33")
        self.lineEdit_33.setReadOnly(True)

        self.gridLayout_15.addWidget(self.lineEdit_33, 5, 1, 1, 1)

        self.verticalSpacer_61 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_15.addItem(self.verticalSpacer_61, 2, 0, 1, 1)

        self.verticalSpacer_74 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_15.addItem(self.verticalSpacer_74, 4, 0, 1, 1)

        self.verticalSpacer_75 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_15.addItem(self.verticalSpacer_75, 6, 0, 1, 1)


        self.verticalLayout_9.addLayout(self.gridLayout_15)

        self.gridLayoutWidget_4 = QWidget(self.tab_4)
        self.gridLayoutWidget_4.setObjectName(u"gridLayoutWidget_4")
        self.gridLayoutWidget_4.setGeometry(QRect(0, 10, 1021, 103))
        self.gridLayout_10 = QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.title5 = QLabel(self.gridLayoutWidget_4)
        self.title5.setObjectName(u"title5")
        self.title5.setMinimumSize(QSize(216, 32))
        self.title5.setFont(font3)

        self.gridLayout_10.addWidget(self.title5, 1, 1, 1, 1)

        self.horizontalSpacer_65 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer_65, 1, 2, 1, 1)

        self.horizontalSpacer_64 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer_64, 1, 0, 1, 1)

        self.verticalSpacer_53 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_10.addItem(self.verticalSpacer_53, 0, 1, 1, 1)

        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.frame_6 = QFrame(self.tab_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(40, 170, 931, 281))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_6)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.gridLayout_17 = QGridLayout()
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.lineEdit_63 = QLineEdit(self.frame_6)
        self.lineEdit_63.setObjectName(u"lineEdit_63")
        self.lineEdit_63.setReadOnly(True)

        self.gridLayout_17.addWidget(self.lineEdit_63, 4, 11, 1, 1)

        self.lineEdit_58 = QLineEdit(self.frame_6)
        self.lineEdit_58.setObjectName(u"lineEdit_58")
        self.lineEdit_58.setReadOnly(True)

        self.gridLayout_17.addWidget(self.lineEdit_58, 4, 3, 1, 1)

        self.lineEdit_44 = QLineEdit(self.frame_6)
        self.lineEdit_44.setObjectName(u"lineEdit_44")
        self.lineEdit_44.setReadOnly(True)

        self.gridLayout_17.addWidget(self.lineEdit_44, 4, 1, 1, 1)

        self.label_60 = QLabel(self.frame_6)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setFont(font1)

        self.gridLayout_17.addWidget(self.label_60, 2, 3, 1, 1, Qt.AlignHCenter)

        self.label_61 = QLabel(self.frame_6)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setFont(font1)

        self.gridLayout_17.addWidget(self.label_61, 2, 7, 1, 1, Qt.AlignHCenter)

        self.lineEdit_64 = QLineEdit(self.frame_6)
        self.lineEdit_64.setObjectName(u"lineEdit_64")
        self.lineEdit_64.setReadOnly(True)

        self.gridLayout_17.addWidget(self.lineEdit_64, 6, 11, 1, 1)

        self.horizontalSpacer_54 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_17.addItem(self.horizontalSpacer_54, 0, 10, 1, 1)

        self.label_58 = QLabel(self.frame_6)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setFont(font1)

        self.gridLayout_17.addWidget(self.label_58, 2, 1, 1, 1, Qt.AlignHCenter)

        self.lineEdit_62 = QLineEdit(self.frame_6)
        self.lineEdit_62.setObjectName(u"lineEdit_62")
        self.lineEdit_62.setReadOnly(True)

        self.gridLayout_17.addWidget(self.lineEdit_62, 4, 9, 1, 1)

        self.horizontalSpacer_50 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_17.addItem(self.horizontalSpacer_50, 0, 2, 1, 1)

        self.horizontalSpacer_49 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_17.addItem(self.horizontalSpacer_49, 0, 4, 1, 1)

        self.label_59 = QLabel(self.frame_6)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setFont(font1)

        self.gridLayout_17.addWidget(self.label_59, 2, 5, 1, 1, Qt.AlignHCenter)

        self.lineEdit_65 = QLineEdit(self.frame_6)
        self.lineEdit_65.setObjectName(u"lineEdit_65")
        self.lineEdit_65.setReadOnly(True)

        self.gridLayout_17.addWidget(self.lineEdit_65, 6, 9, 1, 1)

        self.lineEdit_57 = QLineEdit(self.frame_6)
        self.lineEdit_57.setObjectName(u"lineEdit_57")
        self.lineEdit_57.setReadOnly(True)

        self.gridLayout_17.addWidget(self.lineEdit_57, 6, 3, 1, 1)

        self.label_64 = QLabel(self.frame_6)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setFont(font2)

        self.gridLayout_17.addWidget(self.label_64, 0, 1, 1, 1)

        self.label_63 = QLabel(self.frame_6)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setFont(font1)

        self.gridLayout_17.addWidget(self.label_63, 2, 11, 1, 1, Qt.AlignHCenter)

        self.lineEdit_60 = QLineEdit(self.frame_6)
        self.lineEdit_60.setObjectName(u"lineEdit_60")
        self.lineEdit_60.setReadOnly(True)

        self.gridLayout_17.addWidget(self.lineEdit_60, 6, 5, 1, 1)

        self.lineEdit_56 = QLineEdit(self.frame_6)
        self.lineEdit_56.setObjectName(u"lineEdit_56")
        self.lineEdit_56.setReadOnly(True)

        self.gridLayout_17.addWidget(self.lineEdit_56, 6, 1, 1, 1)

        self.lineEdit_51 = QLineEdit(self.frame_6)
        self.lineEdit_51.setObjectName(u"lineEdit_51")
        self.lineEdit_51.setReadOnly(True)

        self.gridLayout_17.addWidget(self.lineEdit_51, 4, 5, 1, 1)

        self.lineEdit_66 = QLineEdit(self.frame_6)
        self.lineEdit_66.setObjectName(u"lineEdit_66")
        self.lineEdit_66.setReadOnly(True)

        self.gridLayout_17.addWidget(self.lineEdit_66, 6, 7, 1, 1)

        self.horizontalSpacer_52 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_17.addItem(self.horizontalSpacer_52, 0, 6, 1, 1)

        self.label_62 = QLabel(self.frame_6)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setFont(font1)

        self.gridLayout_17.addWidget(self.label_62, 2, 9, 1, 1, Qt.AlignHCenter)

        self.horizontalSpacer_53 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_17.addItem(self.horizontalSpacer_53, 0, 8, 1, 1)

        self.lineEdit_61 = QLineEdit(self.frame_6)
        self.lineEdit_61.setObjectName(u"lineEdit_61")
        self.lineEdit_61.setReadOnly(True)

        self.gridLayout_17.addWidget(self.lineEdit_61, 4, 7, 1, 1)

        self.verticalSpacer_57 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_17.addItem(self.verticalSpacer_57, 1, 0, 1, 1)

        self.verticalSpacer_67 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_17.addItem(self.verticalSpacer_67, 3, 0, 1, 1)

        self.verticalSpacer_72 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_17.addItem(self.verticalSpacer_72, 5, 0, 1, 1)

        self.verticalSpacer_73 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_17.addItem(self.verticalSpacer_73, 7, 0, 1, 1)


        self.verticalLayout_10.addLayout(self.gridLayout_17)

        self.gridLayoutWidget_10 = QWidget(self.tab_5)
        self.gridLayoutWidget_10.setObjectName(u"gridLayoutWidget_10")
        self.gridLayoutWidget_10.setGeometry(QRect(0, 10, 1021, 103))
        self.gridLayout_11 = QGridLayout(self.gridLayoutWidget_10)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_67 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer_67, 1, 2, 1, 1)

        self.horizontalSpacer_66 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer_66, 1, 0, 1, 1)

        self.title6 = QLabel(self.gridLayoutWidget_10)
        self.title6.setObjectName(u"title6")
        self.title6.setMinimumSize(QSize(216, 32))
        self.title6.setFont(font3)

        self.gridLayout_11.addWidget(self.title6, 1, 1, 1, 1)

        self.verticalSpacer_54 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_11.addItem(self.verticalSpacer_54, 0, 1, 1, 1)

        self.tabWidget.addTab(self.tab_5, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.stop_btn.setText(QCoreApplication.translate("MainWindow", u"\u505c\u6b62", None))
        self.power_btn.setText(QCoreApplication.translate("MainWindow", u"\u96fb\u6e90", None))
        self.check_stopper_cyl_label.setText(QCoreApplication.translate("MainWindow", u"STOPPER CYL", None))
        self.check_stopper_cyl_down_btn.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u964d", None))
        self.check_fixed_position_CYL_label.setText(QCoreApplication.translate("MainWindow", u"\u5b9a\u4f4d\u7f6e CYL", None))
        self.check_fixed_position_CYL_down_btn.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u964d", None))
        self.check_fixed_position_CYL_up_btn.setText(QCoreApplication.translate("MainWindow", u"\u4e0a\u5347", None))
        self.check_stopper_cyl_up_btn.setText(QCoreApplication.translate("MainWindow", u"\u4e0a\u5347", None))
        self.check_label.setText(QCoreApplication.translate("MainWindow", u"\u6aa2\u67e5", None))
        self.clean_fixed_position_CYL_up_btn.setText(QCoreApplication.translate("MainWindow", u"\u4e0a\u5347", None))
        self.clean_stopper_cyl_label.setText(QCoreApplication.translate("MainWindow", u"STOPPER CYL", None))
        self.clean_fixed_position_CYL_label.setText(QCoreApplication.translate("MainWindow", u"\u5b9a\u4f4d\u7f6e CYL", None))
        self.clean_label.setText(QCoreApplication.translate("MainWindow", u"\u6d17\u6de8", None))
        self.clean_stopper_cyl_up_btn.setText(QCoreApplication.translate("MainWindow", u"\u4e0a\u5347", None))
        self.clean_fixed_position_CYL_down_btn.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u964d", None))
        self.clean_stopper_cyl_down_btn.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u964d", None))
        self.pomp_check_CYL_open_btn.setText(QCoreApplication.translate("MainWindow", u"\u6253\u958b", None))
        self.pomp_label.setText(QCoreApplication.translate("MainWindow", u"POMP", None))
        self.pomp_power_label.setText(QCoreApplication.translate("MainWindow", u"\u96fb\u6e90", None))
        self.pomp_check_CYL_close_btn.setText(QCoreApplication.translate("MainWindow", u"\u95dc\u9589", None))
        self.pomp_check_CYL_label.setText(QCoreApplication.translate("MainWindow", u"\u6aa2\u67e5 CYL", None))
        self.pomp_power_close_btn.setText(QCoreApplication.translate("MainWindow", u"\u95dc\u9589", None))
        self.pomp_power_open_btn.setText(QCoreApplication.translate("MainWindow", u"\u6253\u958b", None))
        self.action_setting.setText(QCoreApplication.translate("MainWindow", u"\u52d5\u4f5c\u8a2d\u5b9a", None))
        self.air_value_close_btn.setText(QCoreApplication.translate("MainWindow", u"\u95dc\u9589", None))
        self.airValue_value_label.setText(QCoreApplication.translate("MainWindow", u"VALVE", None))
        self.air_value_title_label.setText(QCoreApplication.translate("MainWindow", u"Air Value", None))
        self.air_value_label.setText(QCoreApplication.translate("MainWindow", u"AIR VALVE", None))
        self.airValue_value_open_btn.setText(QCoreApplication.translate("MainWindow", u"\u6253\u958b", None))
        self.airValue_value_close_btn.setText(QCoreApplication.translate("MainWindow", u"\u95dc\u9589", None))
        self.air_value_open_btn.setText(QCoreApplication.translate("MainWindow", u"\u6253\u958b", None))
        self.title.setText(QCoreApplication.translate("MainWindow", u"\u92fc\u7ba1\u54c1\u8cea\u6aa2\u9a57\u7cfb\u7d71", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u52d5\u4f5c\u8a2d\u5b9a", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u6e2c\u91cf\u986f\u793a", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u751f\u7522 Count", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u76f4\u89d2\u5ea6", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Count", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u7aef\u9762\u89d2\u5ea6", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u76ee\u6a19\u503c", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u5224\u5b9a\u503c", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u9805\u76ee", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u7aef\u9762\u5bec\u5ea6", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Cycle Time", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"NG \u6578\u91cf", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u5be6\u6e2c\u503c", None))
        self.title2.setText(QCoreApplication.translate("MainWindow", u"\u92fc\u7ba1\u54c1\u8cea\u6aa2\u9a57\u7cfb\u7d71", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u6e2c\u91cf\u986f\u793a", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"\u7aef\u9762\u5bec\u5ea6", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"\u92fc\u7ba1\u9577\u5ea6", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"\u751f\u7522 NO.", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"\u92fc\u7ba1\u76f4\u5f91", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Max \u5bb9\u8a31\u503c", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"\u92fc\u7ba1\u539a\u5ea6", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"\u9805\u76ee", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"\u76ee\u6a19\u503c", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"\u76f4\u89d2\u5ea6", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Min \u5bb9\u8a31\u503c", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"\u6e2c\u91cf\u8a2d\u5b9a", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"\u7aef\u9762\u89d2\u5ea6", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"\u751f\u7522 Count", None))
        self.title3.setText(QCoreApplication.translate("MainWindow", u"\u92fc\u7ba1\u54c1\u8cea\u6aa2\u9a57\u7cfb\u7d71", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"\u6e2c\u91cf\u8a2d\u5b9a", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"\u611f\u6e2c\u5668\u72c0\u614b", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"\u7576\u524d\u72c0\u614b", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"\u611f\u6e2c\u5668\u540d\u7a31", None))
        self.title4.setText(QCoreApplication.translate("MainWindow", u"\u92fc\u7ba1\u54c1\u8cea\u6aa2\u9a57\u7cfb\u7d71", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"\u611f\u6e2c\u5668\u72c0\u614b", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"\u72c0\u614b", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"\u92fc\u7ba1 NO.", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"\u7570\u5e38\u7d00\u9304", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"\u7570\u5e38\u6642\u9593", None))
        self.title5.setText(QCoreApplication.translate("MainWindow", u"\u92fc\u7ba1\u54c1\u8cea\u6aa2\u9a57\u7cfb\u7d71", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"\u7570\u5e38\u7d00\u9304", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"\u7aef\u9762\u89d2\u5ea6", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"\u76f4\u89d2\u5ea6", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"\u92fc\u7ba1 NO.", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"\u7aef\u9762\u5bec\u5ea6", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"\u8cc7\u6599\u4fdd\u5b58", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"\u7570\u5e38\u6642\u9593", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"\u72c0\u614b", None))
        self.title6.setText(QCoreApplication.translate("MainWindow", u"\u92fc\u7ba1\u54c1\u8cea\u6aa2\u9a57\u7cfb\u7d71", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"\u8cc7\u6599\u4fdd\u5b58", None))
    # retranslateUi

