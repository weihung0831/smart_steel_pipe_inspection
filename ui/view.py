# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitledHuoYfW.ui'
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
    QFrame,
    QGridLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QStatusBar,
    QTabWidget,
    QVBoxLayout,
    QWidget,
)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 768)
        MainWindow.setMinimumSize(QSize(1024, 768))
        MainWindow.setMaximumSize(QSize(1024, 768))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tabWidget.setGeometry(QRect(0, 10, 1591, 731))
        font = QFont()
        font.setPointSize(9)
        self.tabWidget.setFont(font)
        self.tab = QWidget()
        self.tab.setObjectName("tab")
        self.frame = QFrame(self.tab)
        self.frame.setObjectName("frame")
        self.frame.setGeometry(QRect(40, 20, 941, 580))
        self.frame.setMinimumSize(QSize(900, 580))
        self.frame.setMaximumSize(QSize(991, 561))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayoutWidget_5 = QWidget(self.frame)
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")
        self.gridLayoutWidget_5.setGeometry(QRect(20, 100, 190, 52))
        self.gridLayout_18 = QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.gridLayout_18.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_5 = QSpacerItem(
            10, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.gridLayout_18.addItem(self.horizontalSpacer_5, 1, 3, 1, 1)

        self.stop_btn = QPushButton(self.gridLayoutWidget_5)
        self.stop_btn.setObjectName("stop_btn")

        self.gridLayout_18.addWidget(self.stop_btn, 1, 2, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(
            10, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.gridLayout_18.addItem(self.horizontalSpacer_4, 1, 1, 1, 1)

        self.power_btn = QPushButton(self.gridLayoutWidget_5)
        self.power_btn.setObjectName("power_btn")

        self.gridLayout_18.addWidget(self.power_btn, 1, 0, 1, 1)

        self.gridLayoutWidget_7 = QWidget(self.frame)
        self.gridLayoutWidget_7.setObjectName("gridLayoutWidget_7")
        self.gridLayoutWidget_7.setGeometry(QRect(510, 170, 379, 191))
        self.gridLayout_22 = QGridLayout(self.gridLayoutWidget_7)
        self.gridLayout_22.setObjectName("gridLayout_22")
        self.gridLayout_22.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_10 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.gridLayout_22.addItem(self.horizontalSpacer_10, 0, 3, 1, 1)

        self.check_label = QLabel(self.gridLayoutWidget_7)
        self.check_label.setObjectName("check_label")
        font1 = QFont()
        font1.setFamilies(["Cascadia Code"])
        font1.setPointSize(14)
        self.check_label.setFont(font1)

        self.gridLayout_22.addWidget(self.check_label, 1, 0, 1, 1, Qt.AlignLeft)

        self.check_fixed_position_CYL_label = QLabel(self.gridLayoutWidget_7)
        self.check_fixed_position_CYL_label.setObjectName(
            "check_fixed_position_CYL_label"
        )
        self.check_fixed_position_CYL_label.setFont(font1)

        self.gridLayout_22.addWidget(
            self.check_fixed_position_CYL_label, 6, 0, 1, 1, Qt.AlignLeft
        )

        self.check_stopper_cyl_up_btn = QPushButton(self.gridLayoutWidget_7)
        self.check_stopper_cyl_up_btn.setObjectName("check_stopper_cyl_up_btn")

        self.gridLayout_22.addWidget(
            self.check_stopper_cyl_up_btn, 4, 2, 1, 1, Qt.AlignHCenter
        )

        self.verticalSpacer_9 = QSpacerItem(
            20, 10, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.gridLayout_22.addItem(self.verticalSpacer_9, 5, 0, 1, 1)

        self.check_fixed_position_CYL_down_btn = QPushButton(self.gridLayoutWidget_7)
        self.check_fixed_position_CYL_down_btn.setObjectName(
            "check_fixed_position_CYL_down_btn"
        )

        self.gridLayout_22.addWidget(self.check_fixed_position_CYL_down_btn, 6, 4, 1, 1)

        self.check_fixed_position_CYL_up_btn = QPushButton(self.gridLayoutWidget_7)
        self.check_fixed_position_CYL_up_btn.setObjectName(
            "check_fixed_position_CYL_up_btn"
        )

        self.gridLayout_22.addWidget(
            self.check_fixed_position_CYL_up_btn, 6, 2, 1, 1, Qt.AlignHCenter
        )

        self.verticalSpacer_7 = QSpacerItem(
            20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.gridLayout_22.addItem(self.verticalSpacer_7, 0, 0, 1, 1)

        self.verticalSpacer_10 = QSpacerItem(
            40, 20, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.gridLayout_22.addItem(self.verticalSpacer_10, 7, 0, 1, 1)

        self.check_stopper_cyl_down_btn = QPushButton(self.gridLayoutWidget_7)
        self.check_stopper_cyl_down_btn.setObjectName("check_stopper_cyl_down_btn")

        self.gridLayout_22.addWidget(self.check_stopper_cyl_down_btn, 4, 4, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(
            20, 10, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.gridLayout_22.addItem(self.verticalSpacer_8, 2, 0, 1, 1)

        self.check_stopper_cyl_label = QLabel(self.gridLayoutWidget_7)
        self.check_stopper_cyl_label.setObjectName("check_stopper_cyl_label")
        self.check_stopper_cyl_label.setFont(font1)

        self.gridLayout_22.addWidget(
            self.check_stopper_cyl_label, 4, 0, 1, 1, Qt.AlignLeft
        )

        self.horizontalSpacer_9 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.gridLayout_22.addItem(self.horizontalSpacer_9, 0, 1, 1, 1)

        self.gridLayoutWidget_6 = QWidget(self.frame)
        self.gridLayoutWidget_6.setObjectName("gridLayoutWidget_6")
        self.gridLayoutWidget_6.setGeometry(QRect(20, 170, 471, 191))
        self.gridLayout_23 = QGridLayout(self.gridLayoutWidget_6)
        self.gridLayout_23.setObjectName("gridLayout_23")
        self.gridLayout_23.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_4 = QSpacerItem(
            20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.gridLayout_23.addItem(self.verticalSpacer_4, 2, 0, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.gridLayout_23.addItem(self.horizontalSpacer_6, 0, 1, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(
            40, 20, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.gridLayout_23.addItem(self.verticalSpacer_6, 6, 0, 1, 1)

        self.clean_fixed_position_CYL_up_btn = QPushButton(self.gridLayoutWidget_6)
        self.clean_fixed_position_CYL_up_btn.setObjectName(
            "clean_fixed_position_CYL_up_btn"
        )

        self.gridLayout_23.addWidget(
            self.clean_fixed_position_CYL_up_btn, 5, 2, 1, 1, Qt.AlignHCenter
        )

        self.clean_stopper_cyl_label = QLabel(self.gridLayoutWidget_6)
        self.clean_stopper_cyl_label.setObjectName("clean_stopper_cyl_label")
        self.clean_stopper_cyl_label.setFont(font1)

        self.gridLayout_23.addWidget(
            self.clean_stopper_cyl_label, 3, 0, 1, 1, Qt.AlignLeft
        )

        self.clean_fixed_position_CYL_label = QLabel(self.gridLayoutWidget_6)
        self.clean_fixed_position_CYL_label.setObjectName(
            "clean_fixed_position_CYL_label"
        )
        self.clean_fixed_position_CYL_label.setFont(font1)

        self.gridLayout_23.addWidget(
            self.clean_fixed_position_CYL_label, 5, 0, 1, 1, Qt.AlignLeft
        )

        self.verticalSpacer_3 = QSpacerItem(
            20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.gridLayout_23.addItem(self.verticalSpacer_3, 0, 0, 1, 1)

        self.clean_label = QLabel(self.gridLayoutWidget_6)
        self.clean_label.setObjectName("clean_label")
        self.clean_label.setFont(font1)

        self.gridLayout_23.addWidget(self.clean_label, 1, 0, 1, 1, Qt.AlignLeft)

        self.horizontalSpacer_7 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.gridLayout_23.addItem(self.horizontalSpacer_7, 0, 3, 1, 1)

        self.clean_stopper_cyl_up_btn = QPushButton(self.gridLayoutWidget_6)
        self.clean_stopper_cyl_up_btn.setObjectName("clean_stopper_cyl_up_btn")

        self.gridLayout_23.addWidget(
            self.clean_stopper_cyl_up_btn, 3, 2, 1, 1, Qt.AlignHCenter
        )

        self.clean_fixed_position_CYL_down_btn = QPushButton(self.gridLayoutWidget_6)
        self.clean_fixed_position_CYL_down_btn.setObjectName(
            "clean_fixed_position_CYL_down_btn"
        )

        self.gridLayout_23.addWidget(self.clean_fixed_position_CYL_down_btn, 5, 4, 1, 1)

        self.clean_stopper_cyl_down_btn = QPushButton(self.gridLayoutWidget_6)
        self.clean_stopper_cyl_down_btn.setObjectName("clean_stopper_cyl_down_btn")

        self.gridLayout_23.addWidget(self.clean_stopper_cyl_down_btn, 3, 4, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.gridLayout_23.addItem(self.horizontalSpacer_8, 0, 5, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(
            20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.gridLayout_23.addItem(self.verticalSpacer_5, 4, 0, 1, 1)

        self.gridLayoutWidget_8 = QWidget(self.frame)
        self.gridLayoutWidget_8.setObjectName("gridLayoutWidget_8")
        self.gridLayoutWidget_8.setGeometry(QRect(20, 380, 471, 171))
        self.gridLayout_24 = QGridLayout(self.gridLayoutWidget_8)
        self.gridLayout_24.setObjectName("gridLayout_24")
        self.gridLayout_24.setContentsMargins(0, 0, 0, 0)
        self.pomp_check_CYL_open_btn = QPushButton(self.gridLayoutWidget_8)
        self.pomp_check_CYL_open_btn.setObjectName("pomp_check_CYL_open_btn")

        self.gridLayout_24.addWidget(self.pomp_check_CYL_open_btn, 6, 2, 1, 1)

        self.pomp_label = QLabel(self.gridLayoutWidget_8)
        self.pomp_label.setObjectName("pomp_label")
        self.pomp_label.setFont(font1)

        self.gridLayout_24.addWidget(self.pomp_label, 1, 0, 1, 1, Qt.AlignLeft)

        self.pomp_power_label = QLabel(self.gridLayoutWidget_8)
        self.pomp_power_label.setObjectName("pomp_power_label")
        self.pomp_power_label.setFont(font1)

        self.gridLayout_24.addWidget(self.pomp_power_label, 4, 0, 1, 1, Qt.AlignLeft)

        self.pomp_check_CYL_close_btn = QPushButton(self.gridLayoutWidget_8)
        self.pomp_check_CYL_close_btn.setObjectName("pomp_check_CYL_close_btn")

        self.gridLayout_24.addWidget(self.pomp_check_CYL_close_btn, 6, 5, 1, 1)

        self.pomp_check_CYL_label = QLabel(self.gridLayoutWidget_8)
        self.pomp_check_CYL_label.setObjectName("pomp_check_CYL_label")
        self.pomp_check_CYL_label.setFont(font1)

        self.gridLayout_24.addWidget(
            self.pomp_check_CYL_label, 6, 0, 1, 1, Qt.AlignLeft
        )

        self.verticalSpacer_12 = QSpacerItem(
            20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.gridLayout_24.addItem(self.verticalSpacer_12, 2, 0, 1, 1)

        self.pomp_power_close_btn = QPushButton(self.gridLayoutWidget_8)
        self.pomp_power_close_btn.setObjectName("pomp_power_close_btn")

        self.gridLayout_24.addWidget(self.pomp_power_close_btn, 4, 5, 1, 1)

        self.verticalSpacer_13 = QSpacerItem(
            20, 10, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.gridLayout_24.addItem(self.verticalSpacer_13, 5, 0, 1, 1)

        self.verticalSpacer_11 = QSpacerItem(
            20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.gridLayout_24.addItem(self.verticalSpacer_11, 0, 0, 1, 1)

        self.pomp_power_open_btn = QPushButton(self.gridLayoutWidget_8)
        self.pomp_power_open_btn.setObjectName("pomp_power_open_btn")

        self.gridLayout_24.addWidget(
            self.pomp_power_open_btn, 4, 2, 1, 1, Qt.AlignHCenter
        )

        self.horizontalSpacer_12 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.gridLayout_24.addItem(self.horizontalSpacer_12, 0, 1, 1, 1)

        self.horizontalSpacer_13 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.gridLayout_24.addItem(self.horizontalSpacer_13, 0, 4, 1, 1)

        self.horizontalSpacer_14 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.gridLayout_24.addItem(self.horizontalSpacer_14, 0, 6, 1, 1)

        self.layoutWidget = QWidget(self.frame)
        self.layoutWidget.setObjectName("layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 10, 202, 34))
        self.gridLayout_7 = QGridLayout(self.layoutWidget)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.sub_title = QLabel(self.layoutWidget)
        self.sub_title.setObjectName("sub_title")
        font2 = QFont()
        font2.setFamilies(["Cascadia Code"])
        font2.setPointSize(20)
        self.sub_title.setFont(font2)

        self.gridLayout_7.addWidget(self.sub_title, 0, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.gridLayout_7.addItem(self.horizontalSpacer_3, 0, 1, 1, 1)

        self.gridLayoutWidget_9 = QWidget(self.frame)
        self.gridLayoutWidget_9.setObjectName("gridLayoutWidget_9")
        self.gridLayoutWidget_9.setGeometry(QRect(510, 380, 381, 171))
        self.gridLayout_25 = QGridLayout(self.gridLayoutWidget_9)
        self.gridLayout_25.setObjectName("gridLayout_25")
        self.gridLayout_25.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_14 = QSpacerItem(
            20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.gridLayout_25.addItem(self.verticalSpacer_14, 0, 0, 1, 1)

        self.airValue_value_open_btn = QPushButton(self.gridLayoutWidget_9)
        self.airValue_value_open_btn.setObjectName("airValue_value_open_btn")

        self.gridLayout_25.addWidget(
            self.airValue_value_open_btn, 4, 2, 1, 1, Qt.AlignHCenter
        )

        self.air_value_close_btn = QPushButton(self.gridLayoutWidget_9)
        self.air_value_close_btn.setObjectName("air_value_close_btn")

        self.gridLayout_25.addWidget(self.air_value_close_btn, 6, 4, 1, 1)

        self.air_value_label = QLabel(self.gridLayoutWidget_9)
        self.air_value_label.setObjectName("air_value_label")
        self.air_value_label.setFont(font1)

        self.gridLayout_25.addWidget(self.air_value_label, 6, 0, 1, 1, Qt.AlignLeft)

        self.air_value_open_btn = QPushButton(self.gridLayoutWidget_9)
        self.air_value_open_btn.setObjectName("air_value_open_btn")

        self.gridLayout_25.addWidget(self.air_value_open_btn, 6, 2, 1, 1)

        self.airValue_value_label = QLabel(self.gridLayoutWidget_9)
        self.airValue_value_label.setObjectName("airValue_value_label")
        self.airValue_value_label.setFont(font1)

        self.gridLayout_25.addWidget(
            self.airValue_value_label, 4, 0, 1, 1, Qt.AlignLeft
        )

        self.airValue_value_close_btn = QPushButton(self.gridLayoutWidget_9)
        self.airValue_value_close_btn.setObjectName("airValue_value_close_btn")

        self.gridLayout_25.addWidget(self.airValue_value_close_btn, 4, 4, 1, 1)

        self.verticalSpacer_15 = QSpacerItem(
            20, 10, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.gridLayout_25.addItem(self.verticalSpacer_15, 3, 0, 1, 1)

        self.horizontalSpacer_16 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.gridLayout_25.addItem(self.horizontalSpacer_16, 0, 3, 1, 1)

        self.air_value_title_label = QLabel(self.gridLayoutWidget_9)
        self.air_value_title_label.setObjectName("air_value_title_label")
        self.air_value_title_label.setFont(font1)

        self.gridLayout_25.addWidget(
            self.air_value_title_label, 1, 0, 1, 1, Qt.AlignLeft
        )

        self.horizontalSpacer_15 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.gridLayout_25.addItem(self.horizontalSpacer_15, 0, 1, 1, 1)

        self.verticalSpacer_16 = QSpacerItem(
            20, 10, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.gridLayout_25.addItem(self.verticalSpacer_16, 5, 0, 1, 1)

        self.power_status_label = QLabel(self.frame)
        self.power_status_label.setObjectName("power_status_label")
        self.power_status_label.setGeometry(QRect(20, 60, 191, 31))
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName("tab_2")
        self.frame_2 = QFrame(self.tab_2)
        self.frame_2.setObjectName("frame_2")
        self.frame_2.setGeometry(QRect(40, 20, 951, 485))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.end_face_angle_target_lineEdit = QLineEdit(self.frame_2)
        self.end_face_angle_target_lineEdit.setObjectName(
            "end_face_angle_target_lineEdit"
        )
        self.end_face_angle_target_lineEdit.setReadOnly(True)

        self.gridLayout_3.addWidget(self.end_face_angle_target_lineEdit, 5, 3, 1, 1)

        self.measured_value_label = QLabel(self.frame_2)
        self.measured_value_label.setObjectName("measured_value_label")
        self.measured_value_label.setFont(font1)

        self.gridLayout_3.addWidget(self.measured_value_label, 2, 5, 1, 1, Qt.AlignLeft)

        self.horizontalSpacer_22 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.gridLayout_3.addItem(self.horizontalSpacer_22, 0, 6, 1, 1)

        self.verticalSpacer_18 = QSpacerItem(
            20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.gridLayout_3.addItem(self.verticalSpacer_18, 1, 1, 1, 1)

        self.total_production_ng_label_lineEdit = QLineEdit(self.frame_2)
        self.total_production_ng_label_lineEdit.setObjectName(
            "total_production_ng_label_lineEdit"
        )
        self.total_production_ng_label_lineEdit.setReadOnly(True)

        self.gridLayout_3.addWidget(
            self.total_production_ng_label_lineEdit, 13, 7, 1, 1
        )

        self.lineEdit_6 = QLineEdit(self.frame_2)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_6.setReadOnly(True)

        self.gridLayout_3.addWidget(self.lineEdit_6, 7, 7, 1, 1)

        self.verticalSpacer_19 = QSpacerItem(
            20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.gridLayout_3.addItem(self.verticalSpacer_19, 4, 1, 1, 1)

        self.end_face_width_target_lineEdit = QLineEdit(self.frame_2)
        self.end_face_width_target_lineEdit.setObjectName(
            "end_face_width_target_lineEdit"
        )
        self.end_face_width_target_lineEdit.setReadOnly(True)

        self.gridLayout_3.addWidget(self.end_face_width_target_lineEdit, 7, 3, 1, 1)

        self.ng_count_label = QLabel(self.frame_2)
        self.ng_count_label.setObjectName("ng_count_label")
        self.ng_count_label.setFont(font1)

        self.gridLayout_3.addWidget(self.ng_count_label, 11, 7, 1, 1, Qt.AlignLeft)

        self.verticalSpacer_25 = QSpacerItem(
            20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.gridLayout_3.addItem(self.verticalSpacer_25, 17, 1, 1, 1)

        self.end_face_angle_label = QLabel(self.frame_2)
        self.end_face_angle_label.setObjectName("end_face_angle_label")
        self.end_face_angle_label.setFont(font1)

        self.gridLayout_3.addWidget(self.end_face_angle_label, 5, 1, 1, 1, Qt.AlignLeft)

        self.right_angle_degree_measured_value_lineEdit = QLineEdit(self.frame_2)
        self.right_angle_degree_measured_value_lineEdit.setObjectName(
            "right_angle_degree_measured_value_lineEdit"
        )
        self.right_angle_degree_measured_value_lineEdit.setReadOnly(True)

        self.gridLayout_3.addWidget(
            self.right_angle_degree_measured_value_lineEdit, 9, 5, 1, 1
        )

        self.verticalSpacer_20 = QSpacerItem(
            20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.gridLayout_3.addItem(self.verticalSpacer_20, 6, 1, 1, 1)

        self.end_face_width_label = QLabel(self.frame_2)
        self.end_face_width_label.setObjectName("end_face_width_label")
        self.end_face_width_label.setFont(font1)

        self.gridLayout_3.addWidget(self.end_face_width_label, 7, 1, 1, 1, Qt.AlignLeft)

        self.end_face_angle_measured_value_lineEdit = QLineEdit(self.frame_2)
        self.end_face_angle_measured_value_lineEdit.setObjectName(
            "end_face_angle_measured_value_lineEdit"
        )
        self.end_face_angle_measured_value_lineEdit.setReadOnly(True)

        self.gridLayout_3.addWidget(
            self.end_face_angle_measured_value_lineEdit, 5, 5, 1, 1
        )

        self.end_angular_target_value_lineEdit = QLineEdit(self.frame_2)
        self.end_angular_target_value_lineEdit.setObjectName(
            "end_angular_target_value_lineEdit"
        )
        self.end_angular_target_value_lineEdit.setReadOnly(True)

        self.gridLayout_3.addWidget(self.end_angular_target_value_lineEdit, 9, 3, 1, 1)

        self.production_cycle_label = QLabel(self.frame_2)
        self.production_cycle_label.setObjectName("production_cycle_label")
        self.production_cycle_label.setFont(font1)

        self.gridLayout_3.addWidget(
            self.production_cycle_label, 16, 1, 1, 1, Qt.AlignLeft
        )

        self.end_face_width_measured_value_lineEdit = QLineEdit(self.frame_2)
        self.end_face_width_measured_value_lineEdit.setObjectName(
            "end_face_width_measured_value_lineEdit"
        )
        self.end_face_width_measured_value_lineEdit.setReadOnly(True)

        self.gridLayout_3.addWidget(
            self.end_face_width_measured_value_lineEdit, 7, 5, 1, 1
        )

        self.count_label = QLabel(self.frame_2)
        self.count_label.setObjectName("count_label")
        self.count_label.setFont(font1)

        self.gridLayout_3.addWidget(self.count_label, 11, 5, 1, 1, Qt.AlignLeft)

        self.production_count_label = QLabel(self.frame_2)
        self.production_count_label.setObjectName("production_count_label")
        self.production_count_label.setFont(font1)

        self.gridLayout_3.addWidget(
            self.production_count_label, 13, 1, 1, 1, Qt.AlignLeft
        )

        self.sub_title2 = QLabel(self.frame_2)
        self.sub_title2.setObjectName("sub_title2")
        self.sub_title2.setFont(font2)

        self.gridLayout_3.addWidget(self.sub_title2, 0, 1, 1, 1)

        self.verticalSpacer_22 = QSpacerItem(
            20, 30, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.gridLayout_3.addItem(self.verticalSpacer_22, 10, 1, 1, 1)

        self.decision_value_label = QLabel(self.frame_2)
        self.decision_value_label.setObjectName("decision_value_label")
        self.decision_value_label.setFont(font1)

        self.gridLayout_3.addWidget(self.decision_value_label, 2, 7, 1, 1, Qt.AlignLeft)

        self.verticalSpacer_21 = QSpacerItem(
            20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.gridLayout_3.addItem(self.verticalSpacer_21, 8, 1, 1, 1)

        self.production_count_target_lineEdit = QLineEdit(self.frame_2)
        self.production_count_target_lineEdit.setObjectName(
            "production_count_target_lineEdit"
        )
        self.production_count_target_lineEdit.setReadOnly(True)

        self.gridLayout_3.addWidget(self.production_count_target_lineEdit, 13, 3, 1, 1)

        self.verticalSpacer_24 = QSpacerItem(
            20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.gridLayout_3.addItem(self.verticalSpacer_24, 14, 1, 1, 1)

        self.list_item_label = QLabel(self.frame_2)
        self.list_item_label.setObjectName("list_item_label")
        self.list_item_label.setFont(font1)

        self.gridLayout_3.addWidget(self.list_item_label, 2, 1, 1, 1, Qt.AlignLeft)

        self.horizontalSpacer_20 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.gridLayout_3.addItem(self.horizontalSpacer_20, 0, 2, 1, 1)

        self.production_cycle_target_lineEdit = QLineEdit(self.frame_2)
        self.production_cycle_target_lineEdit.setObjectName(
            "production_cycle_target_lineEdit"
        )
        self.production_cycle_target_lineEdit.setReadOnly(True)

        self.gridLayout_3.addWidget(self.production_cycle_target_lineEdit, 16, 3, 1, 1)

        self.target_value_label = QLabel(self.frame_2)
        self.target_value_label.setObjectName("target_value_label")
        self.target_value_label.setFont(font1)

        self.gridLayout_3.addWidget(self.target_value_label, 2, 3, 1, 1, Qt.AlignLeft)

        self.total_production_count_lineEdit = QLineEdit(self.frame_2)
        self.total_production_count_lineEdit.setObjectName(
            "total_production_count_lineEdit"
        )
        self.total_production_count_lineEdit.setReadOnly(True)

        self.gridLayout_3.addWidget(self.total_production_count_lineEdit, 13, 5, 1, 1)

        self.lineEdit_5 = QLineEdit(self.frame_2)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_5.setReadOnly(True)

        self.gridLayout_3.addWidget(self.lineEdit_5, 5, 7, 1, 1)

        self.verticalSpacer_23 = QSpacerItem(
            20, 30, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.gridLayout_3.addItem(self.verticalSpacer_23, 12, 1, 1, 1)

        self.horizontalSpacer_23 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.gridLayout_3.addItem(self.horizontalSpacer_23, 0, 8, 1, 1)

        self.lineEdit_8 = QLineEdit(self.frame_2)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_8.setReadOnly(True)

        self.gridLayout_3.addWidget(self.lineEdit_8, 9, 7, 1, 1)

        self.right_angle_degree_label = QLabel(self.frame_2)
        self.right_angle_degree_label.setObjectName("right_angle_degree_label")
        self.right_angle_degree_label.setFont(font1)

        self.gridLayout_3.addWidget(
            self.right_angle_degree_label, 9, 1, 1, 1, Qt.AlignLeft
        )

        self.horizontalSpacer_21 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.gridLayout_3.addItem(self.horizontalSpacer_21, 0, 4, 1, 1)

        self.verticalLayout_4.addLayout(self.gridLayout_3)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName("tab_6")
        self.frame_3 = QFrame(self.tab_6)
        self.frame_3.setObjectName("frame_3")
        self.frame_3.setGeometry(QRect(50, 20, 941, 521))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_3)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.min_allowed_face_angle_lineEdit = QLineEdit(self.frame_3)
        self.min_allowed_face_angle_lineEdit.setObjectName(
            "min_allowed_face_angle_lineEdit"
        )
        self.min_allowed_face_angle_lineEdit.setReadOnly(False)

        self.gridLayout_5.addWidget(self.min_allowed_face_angle_lineEdit, 9, 7, 1, 1)

        self.min_allowed_angle_lineEdit = QLineEdit(self.frame_3)
        self.min_allowed_angle_lineEdit.setObjectName("min_allowed_angle_lineEdit")
        self.min_allowed_angle_lineEdit.setReadOnly(False)

        self.gridLayout_5.addWidget(self.min_allowed_angle_lineEdit, 13, 7, 1, 1)

        self.horizontalSpacer_29 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.gridLayout_5.addItem(self.horizontalSpacer_29, 0, 8, 1, 1)

        self.sub_title3 = QLabel(self.frame_3)
        self.sub_title3.setObjectName("sub_title3")
        self.sub_title3.setFont(font2)

        self.gridLayout_5.addWidget(self.sub_title3, 0, 1, 1, 1)

        self.steel_pipe_diameter_lineEdit = QLineEdit(self.frame_3)
        self.steel_pipe_diameter_lineEdit.setObjectName("steel_pipe_diameter_lineEdit")
        self.steel_pipe_diameter_lineEdit.setReadOnly(True)

        self.gridLayout_5.addWidget(self.steel_pipe_diameter_lineEdit, 5, 3, 1, 1)

        self.verticalSpacer_30 = QSpacerItem(
            20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.gridLayout_5.addItem(self.verticalSpacer_30, 8, 1, 1, 1)

        self.verticalSpacer_28 = QSpacerItem(
            20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.gridLayout_5.addItem(self.verticalSpacer_28, 4, 1, 1, 1)

        self.production_id_lineEdit = QLineEdit(self.frame_3)
        self.production_id_lineEdit.setObjectName("production_id_lineEdit")
        self.production_id_lineEdit.setReadOnly(False)

        self.gridLayout_5.addWidget(self.production_id_lineEdit, 5, 1, 1, 1)

        self.max_allowed_face_angle_lineEdit = QLineEdit(self.frame_3)
        self.max_allowed_face_angle_lineEdit.setObjectName(
            "max_allowed_face_angle_lineEdit"
        )
        self.max_allowed_face_angle_lineEdit.setReadOnly(False)

        self.gridLayout_5.addWidget(self.max_allowed_face_angle_lineEdit, 9, 5, 1, 1)

        self.max_allowed_value_label = QLabel(self.frame_3)
        self.max_allowed_value_label.setObjectName("max_allowed_value_label")
        self.max_allowed_value_label.setFont(font1)

        self.gridLayout_5.addWidget(
            self.max_allowed_value_label, 7, 5, 1, 1, Qt.AlignLeft
        )

        self.verticalSpacer_32 = QSpacerItem(
            20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.gridLayout_5.addItem(self.verticalSpacer_32, 12, 1, 1, 1)

        self.verticalSpacer_29 = QSpacerItem(
            20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.gridLayout_5.addItem(self.verticalSpacer_29, 6, 1, 1, 1)

        self.min_allowed_value_label = QLabel(self.frame_3)
        self.min_allowed_value_label.setObjectName("min_allowed_value_label")
        self.min_allowed_value_label.setFont(font1)

        self.gridLayout_5.addWidget(
            self.min_allowed_value_label, 7, 7, 1, 1, Qt.AlignLeft
        )

        self.verticalSpacer_31 = QSpacerItem(
            20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.gridLayout_5.addItem(self.verticalSpacer_31, 10, 1, 1, 1)

        self.steel_pipe_thickness_label = QLabel(self.frame_3)
        self.steel_pipe_thickness_label.setObjectName("steel_pipe_thickness_label")
        self.steel_pipe_thickness_label.setFont(font1)

        self.gridLayout_5.addWidget(
            self.steel_pipe_thickness_label, 3, 7, 1, 1, Qt.AlignLeft
        )

        self.list_item_label_2 = QLabel(self.frame_3)
        self.list_item_label_2.setObjectName("list_item_label_2")
        self.list_item_label_2.setFont(font1)

        self.gridLayout_5.addWidget(self.list_item_label_2, 7, 1, 1, 1, Qt.AlignLeft)

        self.horizontalSpacer_28 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.gridLayout_5.addItem(self.horizontalSpacer_28, 0, 6, 1, 1)

        self.steel_pipe_length_lineEdit = QLineEdit(self.frame_3)
        self.steel_pipe_length_lineEdit.setObjectName("steel_pipe_length_lineEdit")
        self.steel_pipe_length_lineEdit.setReadOnly(True)

        self.gridLayout_5.addWidget(self.steel_pipe_length_lineEdit, 5, 5, 1, 1)

        self.steel_pipe_length_label = QLabel(self.frame_3)
        self.steel_pipe_length_label.setObjectName("steel_pipe_length_label")
        self.steel_pipe_length_label.setFont(font1)

        self.gridLayout_5.addWidget(
            self.steel_pipe_length_label, 3, 5, 1, 1, Qt.AlignLeft
        )

        self.label_38 = QLabel(self.frame_3)
        self.label_38.setObjectName("label_38")
        self.label_38.setFont(font1)

        self.gridLayout_5.addWidget(self.label_38, 7, 3, 1, 1, Qt.AlignLeft)

        self.production_id_label = QLabel(self.frame_3)
        self.production_id_label.setObjectName("production_id_label")
        self.production_id_label.setFont(font1)

        self.gridLayout_5.addWidget(self.production_id_label, 3, 1, 1, 1, Qt.AlignLeft)

        self.steel_pipe_thickness_lineEdit = QLineEdit(self.frame_3)
        self.steel_pipe_thickness_lineEdit.setObjectName(
            "steel_pipe_thickness_lineEdit"
        )
        self.steel_pipe_thickness_lineEdit.setReadOnly(True)

        self.gridLayout_5.addWidget(self.steel_pipe_thickness_lineEdit, 5, 7, 1, 1)

        self.horizontalSpacer_26 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.gridLayout_5.addItem(self.horizontalSpacer_26, 0, 2, 1, 1)

        self.max_allowed_end_face_width_lineEdit = QLineEdit(self.frame_3)
        self.max_allowed_end_face_width_lineEdit.setObjectName(
            "max_allowed_end_face_width_lineEdit"
        )
        self.max_allowed_end_face_width_lineEdit.setReadOnly(False)

        self.gridLayout_5.addWidget(
            self.max_allowed_end_face_width_lineEdit, 11, 5, 1, 1
        )

        self.verticalSpacer_27 = QSpacerItem(
            20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.gridLayout_5.addItem(self.verticalSpacer_27, 2, 1, 1, 1)

        self.verticalSpacer_34 = QSpacerItem(
            20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.gridLayout_5.addItem(self.verticalSpacer_34, 17, 1, 1, 1)

        self.verticalSpacer_33 = QSpacerItem(
            20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.gridLayout_5.addItem(self.verticalSpacer_33, 14, 1, 1, 1)

        self.steel_pipe_diameter_label = QLabel(self.frame_3)
        self.steel_pipe_diameter_label.setObjectName("steel_pipe_diameter_label")
        self.steel_pipe_diameter_label.setFont(font1)

        self.gridLayout_5.addWidget(
            self.steel_pipe_diameter_label, 3, 3, 1, 1, Qt.AlignLeft
        )

        self.min_allowed_end_face_width_lineEdit = QLineEdit(self.frame_3)
        self.min_allowed_end_face_width_lineEdit.setObjectName(
            "min_allowed_end_face_width_lineEdit"
        )
        self.min_allowed_end_face_width_lineEdit.setReadOnly(False)

        self.gridLayout_5.addWidget(
            self.min_allowed_end_face_width_lineEdit, 11, 7, 1, 1
        )

        self.max_allowed_angle_lineEdit = QLineEdit(self.frame_3)
        self.max_allowed_angle_lineEdit.setObjectName("max_allowed_angle_lineEdit")
        self.max_allowed_angle_lineEdit.setReadOnly(False)

        self.gridLayout_5.addWidget(self.max_allowed_angle_lineEdit, 13, 5, 1, 1)

        self.horizontalSpacer_27 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.gridLayout_5.addItem(self.horizontalSpacer_27, 0, 4, 1, 1)

        self.end_face_angle_label_2 = QLabel(self.frame_3)
        self.end_face_angle_label_2.setObjectName("end_face_angle_label_2")
        self.end_face_angle_label_2.setFont(font1)

        self.gridLayout_5.addWidget(
            self.end_face_angle_label_2, 9, 1, 1, 1, Qt.AlignLeft
        )

        self.end_face_width_label_2 = QLabel(self.frame_3)
        self.end_face_width_label_2.setObjectName("end_face_width_label_2")
        self.end_face_width_label_2.setFont(font1)

        self.gridLayout_5.addWidget(
            self.end_face_width_label_2, 11, 1, 1, 1, Qt.AlignLeft
        )

        self.right_angle_degree_label_2 = QLabel(self.frame_3)
        self.right_angle_degree_label_2.setObjectName("right_angle_degree_label_2")
        self.right_angle_degree_label_2.setFont(font1)

        self.gridLayout_5.addWidget(
            self.right_angle_degree_label_2, 13, 1, 1, 1, Qt.AlignLeft
        )

        self.production_count_label_2 = QLabel(self.frame_3)
        self.production_count_label_2.setObjectName("production_count_label_2")
        self.production_count_label_2.setFont(font1)

        self.gridLayout_5.addWidget(
            self.production_count_label_2, 16, 1, 1, 1, Qt.AlignLeft
        )

        self.end_face_angle_target_lineEdit_2 = QLineEdit(self.frame_3)
        self.end_face_angle_target_lineEdit_2.setObjectName(
            "end_face_angle_target_lineEdit_2"
        )
        self.end_face_angle_target_lineEdit_2.setReadOnly(True)

        self.gridLayout_5.addWidget(self.end_face_angle_target_lineEdit_2, 9, 3, 1, 1)

        self.end_face_width_target_lineEdit_2 = QLineEdit(self.frame_3)
        self.end_face_width_target_lineEdit_2.setObjectName(
            "end_face_width_target_lineEdit_2"
        )
        self.end_face_width_target_lineEdit_2.setReadOnly(True)

        self.gridLayout_5.addWidget(self.end_face_width_target_lineEdit_2, 11, 3, 1, 1)

        self.end_angular_target_value_lineEdit_2 = QLineEdit(self.frame_3)
        self.end_angular_target_value_lineEdit_2.setObjectName(
            "end_angular_target_value_lineEdit_2"
        )
        self.end_angular_target_value_lineEdit_2.setReadOnly(True)

        self.gridLayout_5.addWidget(
            self.end_angular_target_value_lineEdit_2, 13, 3, 1, 1
        )

        self.production_count_target_lineEdit_2 = QLineEdit(self.frame_3)
        self.production_count_target_lineEdit_2.setObjectName(
            "production_count_target_lineEdit_2"
        )
        self.production_count_target_lineEdit_2.setReadOnly(True)

        self.gridLayout_5.addWidget(
            self.production_count_target_lineEdit_2, 16, 3, 1, 1
        )

        self.verticalLayout_6.addLayout(self.gridLayout_5)

        self.tabWidget.addTab(self.tab_6, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName("tab_3")
        self.frame_4 = QFrame(self.tab_3)
        self.frame_4.setObjectName("frame_4")
        self.frame_4.setGeometry(QRect(40, 20, 386, 187))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_4)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.gridLayout_13 = QGridLayout()
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.verticalSpacer_36 = QSpacerItem(
            20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.gridLayout_13.addItem(self.verticalSpacer_36, 1, 1, 1, 1)

        self.sensor_names_lineEdit = QLineEdit(self.frame_4)
        self.sensor_names_lineEdit.setObjectName("sensor_names_lineEdit")
        self.sensor_names_lineEdit.setReadOnly(True)

        self.gridLayout_13.addWidget(
            self.sensor_names_lineEdit, 5, 1, 1, 1, Qt.AlignHCenter
        )

        self.current_status_label = QLabel(self.frame_4)
        self.current_status_label.setObjectName("current_status_label")
        self.current_status_label.setFont(font1)

        self.gridLayout_13.addWidget(
            self.current_status_label, 3, 4, 1, 1, Qt.AlignLeft
        )

        self.sub_title4 = QLabel(self.frame_4)
        self.sub_title4.setObjectName("sub_title4")
        self.sub_title4.setFont(font2)

        self.gridLayout_13.addWidget(self.sub_title4, 0, 1, 1, 1)

        self.horizontalSpacer_33 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.gridLayout_13.addItem(self.horizontalSpacer_33, 0, 5, 1, 1)

        self.current_status_lineEdit = QLineEdit(self.frame_4)
        self.current_status_lineEdit.setObjectName("current_status_lineEdit")
        self.current_status_lineEdit.setReadOnly(True)

        self.gridLayout_13.addWidget(
            self.current_status_lineEdit, 5, 4, 1, 1, Qt.AlignHCenter
        )

        self.verticalSpacer_37 = QSpacerItem(
            20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.gridLayout_13.addItem(self.verticalSpacer_37, 4, 1, 1, 1)

        self.horizontalSpacer_32 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.gridLayout_13.addItem(self.horizontalSpacer_32, 0, 3, 1, 1)

        self.sensor_names_label = QLabel(self.frame_4)
        self.sensor_names_label.setObjectName("sensor_names_label")
        self.sensor_names_label.setFont(font1)

        self.gridLayout_13.addWidget(self.sensor_names_label, 3, 1, 1, 1, Qt.AlignLeft)

        self.verticalSpacer_38 = QSpacerItem(
            20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.gridLayout_13.addItem(self.verticalSpacer_38, 6, 1, 1, 1)

        self.verticalLayout_8.addLayout(self.gridLayout_13)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName("tab_4")
        self.frame_5 = QFrame(self.tab_4)
        self.frame_5.setObjectName("frame_5")
        self.frame_5.setGeometry(QRect(30, 20, 565, 181))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_5)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.gridLayout_15 = QGridLayout()
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.horizontalSpacer_36 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.gridLayout_15.addItem(self.horizontalSpacer_36, 0, 3, 1, 1)

        self.steel_pipe_id_label = QLabel(self.frame_5)
        self.steel_pipe_id_label.setObjectName("steel_pipe_id_label")
        self.steel_pipe_id_label.setFont(font1)

        self.gridLayout_15.addWidget(self.steel_pipe_id_label, 3, 1, 1, 1, Qt.AlignLeft)

        self.anomaly_time_lineEdit = QLineEdit(self.frame_5)
        self.anomaly_time_lineEdit.setObjectName("anomaly_time_lineEdit")
        self.anomaly_time_lineEdit.setReadOnly(True)

        self.gridLayout_15.addWidget(self.anomaly_time_lineEdit, 6, 6, 1, 1)

        self.status_lineEdit = QLineEdit(self.frame_5)
        self.status_lineEdit.setObjectName("status_lineEdit")
        self.status_lineEdit.setReadOnly(True)

        self.gridLayout_15.addWidget(self.status_lineEdit, 6, 4, 1, 1)

        self.horizontalSpacer_38 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.gridLayout_15.addItem(self.horizontalSpacer_38, 0, 7, 1, 1)

        self.steel_pipe_id_lineEdit = QLineEdit(self.frame_5)
        self.steel_pipe_id_lineEdit.setObjectName("steel_pipe_id_lineEdit")
        self.steel_pipe_id_lineEdit.setReadOnly(True)

        self.gridLayout_15.addWidget(self.steel_pipe_id_lineEdit, 6, 1, 1, 1)

        self.verticalSpacer_40 = QSpacerItem(
            20, 5, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.gridLayout_15.addItem(self.verticalSpacer_40, 1, 1, 1, 1)

        self.verticalSpacer_41 = QSpacerItem(
            20, 5, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.gridLayout_15.addItem(self.verticalSpacer_41, 4, 1, 1, 1)

        self.anomaly_time_label = QLabel(self.frame_5)
        self.anomaly_time_label.setObjectName("anomaly_time_label")
        self.anomaly_time_label.setFont(font1)

        self.gridLayout_15.addWidget(self.anomaly_time_label, 3, 6, 1, 1, Qt.AlignLeft)

        self.verticalSpacer_42 = QSpacerItem(
            20, 5, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.gridLayout_15.addItem(self.verticalSpacer_42, 7, 1, 1, 1)

        self.status_label = QLabel(self.frame_5)
        self.status_label.setObjectName("status_label")
        self.status_label.setFont(font1)

        self.gridLayout_15.addWidget(self.status_label, 3, 4, 1, 1, Qt.AlignLeft)

        self.horizontalSpacer_37 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.gridLayout_15.addItem(self.horizontalSpacer_37, 0, 5, 1, 1)

        self.sub_title5 = QLabel(self.frame_5)
        self.sub_title5.setObjectName("sub_title5")
        self.sub_title5.setFont(font2)

        self.gridLayout_15.addWidget(self.sub_title5, 0, 1, 1, 1)

        self.verticalLayout_9.addLayout(self.gridLayout_15)

        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName("tab_5")
        self.frame_6 = QFrame(self.tab_5)
        self.frame_6.setObjectName("frame_6")
        self.frame_6.setGeometry(QRect(30, 20, 931, 231))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_6)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.gridLayout_17 = QGridLayout()
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.verticalSpacer_44 = QSpacerItem(
            20, 5, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.gridLayout_17.addItem(self.verticalSpacer_44, 1, 1, 1, 1)

        self.end_face_angle_label_3 = QLabel(self.frame_6)
        self.end_face_angle_label_3.setObjectName("end_face_angle_label_3")
        self.end_face_angle_label_3.setFont(font1)

        self.gridLayout_17.addWidget(
            self.end_face_angle_label_3, 2, 3, 1, 1, Qt.AlignLeft
        )

        self.horizontalSpacer_41 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.gridLayout_17.addItem(self.horizontalSpacer_41, 0, 2, 1, 1)

        self.anomaly_time_label_2 = QLabel(self.frame_6)
        self.anomaly_time_label_2.setObjectName("anomaly_time_label_2")
        self.anomaly_time_label_2.setFont(font1)

        self.gridLayout_17.addWidget(
            self.anomaly_time_label_2, 2, 11, 1, 1, Qt.AlignLeft
        )

        self.horizontalSpacer_43 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.gridLayout_17.addItem(self.horizontalSpacer_43, 0, 6, 1, 1)

        self.right_angle_degree_label_3 = QLabel(self.frame_6)
        self.right_angle_degree_label_3.setObjectName("right_angle_degree_label_3")
        self.right_angle_degree_label_3.setFont(font1)

        self.gridLayout_17.addWidget(
            self.right_angle_degree_label_3, 2, 7, 1, 1, Qt.AlignLeft
        )

        self.end_face_angle_lineEdit = QLineEdit(self.frame_6)
        self.end_face_angle_lineEdit.setObjectName("end_face_angle_lineEdit")
        self.end_face_angle_lineEdit.setReadOnly(True)

        self.gridLayout_17.addWidget(self.end_face_angle_lineEdit, 4, 3, 1, 1)

        self.steel_pipe_id_label_2 = QLabel(self.frame_6)
        self.steel_pipe_id_label_2.setObjectName("steel_pipe_id_label_2")
        self.steel_pipe_id_label_2.setFont(font1)

        self.gridLayout_17.addWidget(
            self.steel_pipe_id_label_2, 2, 1, 1, 1, Qt.AlignLeft
        )

        self.steel_pipe_id_lineEdit_2 = QLineEdit(self.frame_6)
        self.steel_pipe_id_lineEdit_2.setObjectName("steel_pipe_id_lineEdit_2")
        self.steel_pipe_id_lineEdit_2.setReadOnly(True)

        self.gridLayout_17.addWidget(self.steel_pipe_id_lineEdit_2, 4, 1, 1, 1)

        self.verticalSpacer_46 = QSpacerItem(
            20, 5, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.gridLayout_17.addItem(self.verticalSpacer_46, 5, 1, 1, 1)

        self.horizontalSpacer_42 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.gridLayout_17.addItem(self.horizontalSpacer_42, 0, 4, 1, 1)

        self.end_face_width_label_3 = QLabel(self.frame_6)
        self.end_face_width_label_3.setObjectName("end_face_width_label_3")
        self.end_face_width_label_3.setFont(font1)

        self.gridLayout_17.addWidget(
            self.end_face_width_label_3, 2, 5, 1, 1, Qt.AlignLeft
        )

        self.horizontalSpacer_44 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.gridLayout_17.addItem(self.horizontalSpacer_44, 0, 8, 1, 1)

        self.right_angle_degree_lineEdit = QLineEdit(self.frame_6)
        self.right_angle_degree_lineEdit.setObjectName("right_angle_degree_lineEdit")
        self.right_angle_degree_lineEdit.setReadOnly(True)

        self.gridLayout_17.addWidget(self.right_angle_degree_lineEdit, 4, 7, 1, 1)

        self.end_face_width_lineEdit = QLineEdit(self.frame_6)
        self.end_face_width_lineEdit.setObjectName("end_face_width_lineEdit")
        self.end_face_width_lineEdit.setReadOnly(True)

        self.gridLayout_17.addWidget(self.end_face_width_lineEdit, 4, 5, 1, 1)

        self.anomaly_time_lineEdit_2 = QLineEdit(self.frame_6)
        self.anomaly_time_lineEdit_2.setObjectName("anomaly_time_lineEdit_2")
        self.anomaly_time_lineEdit_2.setReadOnly(True)

        self.gridLayout_17.addWidget(self.anomaly_time_lineEdit_2, 4, 11, 1, 1)

        self.verticalSpacer_45 = QSpacerItem(
            20, 5, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.gridLayout_17.addItem(self.verticalSpacer_45, 3, 1, 1, 1)

        self.horizontalSpacer_45 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.gridLayout_17.addItem(self.horizontalSpacer_45, 0, 10, 1, 1)

        self.status_label_2 = QLabel(self.frame_6)
        self.status_label_2.setObjectName("status_label_2")
        self.status_label_2.setFont(font1)

        self.gridLayout_17.addWidget(self.status_label_2, 2, 9, 1, 1, Qt.AlignLeft)

        self.status_lineEdit_2 = QLineEdit(self.frame_6)
        self.status_lineEdit_2.setObjectName("status_lineEdit_2")
        self.status_lineEdit_2.setReadOnly(True)

        self.gridLayout_17.addWidget(self.status_lineEdit_2, 4, 9, 1, 1)

        self.sub_title6 = QLabel(self.frame_6)
        self.sub_title6.setObjectName("sub_title6")
        self.sub_title6.setFont(font2)

        self.gridLayout_17.addWidget(self.sub_title6, 0, 1, 1, 1)

        self.verticalLayout_10.addLayout(self.gridLayout_17)

        self.tabWidget.addTab(self.tab_5, "")
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
            QCoreApplication.translate(
                "MainWindow", "\u92fc\u7ba1\u54c1\u8cea\u6aa2\u9a57\u7cfb\u7d71", None
            )
        )
        self.stop_btn.setText(
            QCoreApplication.translate("MainWindow", "\u505c\u6b62", None)
        )
        self.power_btn.setText(
            QCoreApplication.translate("MainWindow", "\u96fb\u6e90", None)
        )
        self.check_label.setText(
            QCoreApplication.translate("MainWindow", "\u6aa2\u67e5", None)
        )
        self.check_fixed_position_CYL_label.setText(
            QCoreApplication.translate("MainWindow", "\u5b9a\u4f4d\u7f6e CYL", None)
        )
        self.check_stopper_cyl_up_btn.setText(
            QCoreApplication.translate("MainWindow", "\u4e0a\u5347", None)
        )
        self.check_fixed_position_CYL_down_btn.setText(
            QCoreApplication.translate("MainWindow", "\u4e0b\u964d", None)
        )
        self.check_fixed_position_CYL_up_btn.setText(
            QCoreApplication.translate("MainWindow", "\u4e0a\u5347", None)
        )
        self.check_stopper_cyl_down_btn.setText(
            QCoreApplication.translate("MainWindow", "\u4e0b\u964d", None)
        )
        self.check_stopper_cyl_label.setText(
            QCoreApplication.translate("MainWindow", "STOPPER CYL", None)
        )
        self.clean_fixed_position_CYL_up_btn.setText(
            QCoreApplication.translate("MainWindow", "\u4e0a\u5347", None)
        )
        self.clean_stopper_cyl_label.setText(
            QCoreApplication.translate("MainWindow", "STOPPER CYL", None)
        )
        self.clean_fixed_position_CYL_label.setText(
            QCoreApplication.translate("MainWindow", "\u5b9a\u4f4d\u7f6e CYL", None)
        )
        self.clean_label.setText(
            QCoreApplication.translate("MainWindow", "\u6d17\u6de8", None)
        )
        self.clean_stopper_cyl_up_btn.setText(
            QCoreApplication.translate("MainWindow", "\u4e0a\u5347", None)
        )
        self.clean_fixed_position_CYL_down_btn.setText(
            QCoreApplication.translate("MainWindow", "\u4e0b\u964d", None)
        )
        self.clean_stopper_cyl_down_btn.setText(
            QCoreApplication.translate("MainWindow", "\u4e0b\u964d", None)
        )
        self.pomp_check_CYL_open_btn.setText(
            QCoreApplication.translate("MainWindow", "\u6253\u958b", None)
        )
        self.pomp_label.setText(QCoreApplication.translate("MainWindow", "POMP", None))
        self.pomp_power_label.setText(
            QCoreApplication.translate("MainWindow", "\u96fb\u6e90", None)
        )
        self.pomp_check_CYL_close_btn.setText(
            QCoreApplication.translate("MainWindow", "\u95dc\u9589", None)
        )
        self.pomp_check_CYL_label.setText(
            QCoreApplication.translate("MainWindow", "\u6aa2\u67e5 CYL", None)
        )
        self.pomp_power_close_btn.setText(
            QCoreApplication.translate("MainWindow", "\u95dc\u9589", None)
        )
        self.pomp_power_open_btn.setText(
            QCoreApplication.translate("MainWindow", "\u6253\u958b", None)
        )
        self.sub_title.setText(
            QCoreApplication.translate("MainWindow", "\u52d5\u4f5c\u8a2d\u5b9a", None)
        )
        self.airValue_value_open_btn.setText(
            QCoreApplication.translate("MainWindow", "\u6253\u958b", None)
        )
        self.air_value_close_btn.setText(
            QCoreApplication.translate("MainWindow", "\u95dc\u9589", None)
        )
        self.air_value_label.setText(
            QCoreApplication.translate("MainWindow", "AIR VALVE", None)
        )
        self.air_value_open_btn.setText(
            QCoreApplication.translate("MainWindow", "\u6253\u958b", None)
        )
        self.airValue_value_label.setText(
            QCoreApplication.translate("MainWindow", "VALVE", None)
        )
        self.airValue_value_close_btn.setText(
            QCoreApplication.translate("MainWindow", "\u95dc\u9589", None)
        )
        self.air_value_title_label.setText(
            QCoreApplication.translate("MainWindow", "Air Value", None)
        )
        self.power_status_label.setText("")
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab),
            QCoreApplication.translate("MainWindow", "\u52d5\u4f5c\u8a2d\u5b9a", None),
        )
        self.measured_value_label.setText(
            QCoreApplication.translate("MainWindow", "\u5be6\u6e2c\u503c", None)
        )
        self.ng_count_label.setText(
            QCoreApplication.translate("MainWindow", "NG \u6578\u91cf", None)
        )
        self.end_face_angle_label.setText(
            QCoreApplication.translate("MainWindow", "\u7aef\u9762\u89d2\u5ea6", None)
        )
        self.end_face_width_label.setText(
            QCoreApplication.translate("MainWindow", "\u7aef\u9762\u5bec\u5ea6", None)
        )
        self.end_face_angle_measured_value_lineEdit.setText("")
        self.production_cycle_label.setText(
            QCoreApplication.translate("MainWindow", "\u751f\u7522\u9031\u671f", None)
        )
        self.count_label.setText(
            QCoreApplication.translate("MainWindow", "\u8a08\u6578", None)
        )
        self.production_count_label.setText(
            QCoreApplication.translate(
                "MainWindow", "\u751f\u7522\u7e3d\u6578\u91cf", None
            )
        )
        self.sub_title2.setText(
            QCoreApplication.translate("MainWindow", "\u6e2c\u91cf\u986f\u793a", None)
        )
        self.decision_value_label.setText(
            QCoreApplication.translate("MainWindow", "\u5224\u5b9a\u503c", None)
        )
        self.list_item_label.setText(
            QCoreApplication.translate("MainWindow", "\u9805\u76ee", None)
        )
        self.target_value_label.setText(
            QCoreApplication.translate("MainWindow", "\u76ee\u6a19\u503c", None)
        )
        self.total_production_count_lineEdit.setText("")
        self.right_angle_degree_label.setText(
            QCoreApplication.translate("MainWindow", "\u76f4\u89d2\u5ea6", None)
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_2),
            QCoreApplication.translate("MainWindow", "\u6e2c\u91cf\u986f\u793a", None),
        )
        self.sub_title3.setText(
            QCoreApplication.translate("MainWindow", "\u6e2c\u91cf\u8a2d\u5b9a", None)
        )
        self.max_allowed_value_label.setText(
            QCoreApplication.translate(
                "MainWindow", "\u6700\u5927\u5bb9\u8a31\u503c", None
            )
        )
        self.min_allowed_value_label.setText(
            QCoreApplication.translate(
                "MainWindow", "\u6700\u5c0f\u5bb9\u8a31\u503c", None
            )
        )
        self.steel_pipe_thickness_label.setText(
            QCoreApplication.translate("MainWindow", "\u92fc\u7ba1\u539a\u5ea6", None)
        )
        self.list_item_label_2.setText(
            QCoreApplication.translate("MainWindow", "\u9805\u76ee", None)
        )
        self.steel_pipe_length_label.setText(
            QCoreApplication.translate("MainWindow", "\u92fc\u7ba1\u9577\u5ea6", None)
        )
        self.label_38.setText(
            QCoreApplication.translate("MainWindow", "\u76ee\u6a19\u503c", None)
        )
        self.production_id_label.setText(
            QCoreApplication.translate("MainWindow", "\u751f\u7522\u7de8\u865f", None)
        )
        self.steel_pipe_diameter_label.setText(
            QCoreApplication.translate("MainWindow", "\u92fc\u7ba1\u76f4\u5f91", None)
        )
        self.end_face_angle_label_2.setText(
            QCoreApplication.translate("MainWindow", "\u7aef\u9762\u89d2\u5ea6", None)
        )
        self.end_face_width_label_2.setText(
            QCoreApplication.translate("MainWindow", "\u7aef\u9762\u5bec\u5ea6", None)
        )
        self.right_angle_degree_label_2.setText(
            QCoreApplication.translate("MainWindow", "\u76f4\u89d2\u5ea6", None)
        )
        self.production_count_label_2.setText(
            QCoreApplication.translate(
                "MainWindow", "\u751f\u7522\u7e3d\u6578\u91cf", None
            )
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_6),
            QCoreApplication.translate("MainWindow", "\u6e2c\u91cf\u8a2d\u5b9a", None),
        )
        self.current_status_label.setText(
            QCoreApplication.translate("MainWindow", "\u7576\u524d\u72c0\u614b", None)
        )
        self.sub_title4.setText(
            QCoreApplication.translate(
                "MainWindow", "\u611f\u6e2c\u5668\u72c0\u614b", None
            )
        )
        self.sensor_names_label.setText(
            QCoreApplication.translate(
                "MainWindow", "\u611f\u6e2c\u5668\u540d\u7a31", None
            )
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_3),
            QCoreApplication.translate(
                "MainWindow", "\u611f\u6e2c\u5668\u72c0\u614b", None
            ),
        )
        self.steel_pipe_id_label.setText(
            QCoreApplication.translate("MainWindow", "\u92fc\u7ba1\u7de8\u865f", None)
        )
        self.anomaly_time_label.setText(
            QCoreApplication.translate("MainWindow", "\u7570\u5e38\u6642\u9593", None)
        )
        self.status_label.setText(
            QCoreApplication.translate("MainWindow", "\u72c0\u614b", None)
        )
        self.sub_title5.setText(
            QCoreApplication.translate("MainWindow", "\u7570\u5e38\u7d00\u9304", None)
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_4),
            QCoreApplication.translate("MainWindow", "\u7570\u5e38\u7d00\u9304", None),
        )
        self.end_face_angle_label_3.setText(
            QCoreApplication.translate("MainWindow", "\u7aef\u9762\u89d2\u5ea6", None)
        )
        self.anomaly_time_label_2.setText(
            QCoreApplication.translate("MainWindow", "\u7570\u5e38\u6642\u9593", None)
        )
        self.right_angle_degree_label_3.setText(
            QCoreApplication.translate("MainWindow", "\u76f4\u89d2\u5ea6", None)
        )
        self.steel_pipe_id_label_2.setText(
            QCoreApplication.translate("MainWindow", "\u92fc\u7ba1\u7de8\u865f", None)
        )
        self.end_face_width_label_3.setText(
            QCoreApplication.translate("MainWindow", "\u7aef\u9762\u5bec\u5ea6", None)
        )
        self.status_label_2.setText(
            QCoreApplication.translate("MainWindow", "\u72c0\u614b", None)
        )
        self.sub_title6.setText(
            QCoreApplication.translate("MainWindow", "\u8cc7\u6599\u4fdd\u5b58", None)
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_5),
            QCoreApplication.translate("MainWindow", "\u8cc7\u6599\u4fdd\u5b58", None),
        )

    # retranslateUi
