# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitledVWXGlg.ui'
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
    QHBoxLayout,
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
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tabWidget.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(9)
        self.tabWidget.setFont(font)
        self.tabWidget.setIconSize(QSize(16, 16))
        self.tab_home = QWidget()
        self.tab_home.setObjectName("tab_home")
        self.frame_4 = QFrame(self.tab_home)
        self.frame_4.setObjectName("frame_4")
        self.frame_4.setGeometry(QRect(20, 20, 914, 291))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_4)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_26 = QGridLayout()
        self.gridLayout_26.setObjectName("gridLayout_26")
        self.horizontalSpacer_35 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.gridLayout_26.addItem(self.horizontalSpacer_35, 0, 10, 1, 1)

        self.end_angle_target = QLineEdit(self.frame_4)
        self.end_angle_target.setObjectName("end_angle_target")
        self.end_angle_target.setReadOnly(True)

        self.gridLayout_26.addWidget(self.end_angle_target, 6, 3, 1, 1)

        self.horizontalSpacer_17 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.gridLayout_26.addItem(self.horizontalSpacer_17, 0, 2, 1, 1)

        self.horizontalSpacer_25 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.gridLayout_26.addItem(self.horizontalSpacer_25, 0, 4, 1, 1)

        self.sensor_B_label_2 = QLabel(self.frame_4)
        self.sensor_B_label_2.setObjectName("sensor_B_label_2")
        font1 = QFont()
        font1.setFamilies(["Cascadia Code"])
        font1.setPointSize(14)
        self.sensor_B_label_2.setFont(font1)

        self.gridLayout_26.addWidget(self.sensor_B_label_2, 4, 1, 1, 1, Qt.AlignHCenter)

        self.final_detection_result_label = QLabel(self.frame_4)
        self.final_detection_result_label.setObjectName("final_detection_result_label")
        self.final_detection_result_label.setFont(font1)

        self.gridLayout_26.addWidget(
            self.final_detection_result_label, 8, 1, 1, 1, Qt.AlignHCenter
        )

        self.right_angle_target = QLineEdit(self.frame_4)
        self.right_angle_target.setObjectName("right_angle_target")
        self.right_angle_target.setReadOnly(True)

        self.gridLayout_26.addWidget(self.right_angle_target, 6, 7, 1, 1)

        self.horizontalSpacer_23 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.gridLayout_26.addItem(self.horizontalSpacer_23, 0, 8, 1, 1)

        self.sensor_A_label = QLabel(self.frame_4)
        self.sensor_A_label.setObjectName("sensor_A_label")
        self.sensor_A_label.setFont(font1)

        self.gridLayout_26.addWidget(self.sensor_A_label, 2, 1, 1, 1, Qt.AlignHCenter)

        self.right_angle_label = QLabel(self.frame_4)
        self.right_angle_label.setObjectName("right_angle_label")
        self.right_angle_label.setFont(font1)

        self.gridLayout_26.addWidget(
            self.right_angle_label, 0, 7, 1, 1, Qt.AlignHCenter
        )

        self.sensor_B_detection_value = QLineEdit(self.frame_4)
        self.sensor_B_detection_value.setObjectName("sensor_B_detection_value")
        self.sensor_B_detection_value.setReadOnly(True)

        self.gridLayout_26.addWidget(self.sensor_B_detection_value, 4, 9, 1, 1)

        self.sensor_B_face_width = QLineEdit(self.frame_4)
        self.sensor_B_face_width.setObjectName("sensor_B_face_width")
        self.sensor_B_face_width.setReadOnly(True)

        self.gridLayout_26.addWidget(self.sensor_B_face_width, 4, 5, 1, 1)

        self.detection_value_target = QLineEdit(self.frame_4)
        self.detection_value_target.setObjectName("detection_value_target")
        self.detection_value_target.setReadOnly(True)

        self.gridLayout_26.addWidget(self.detection_value_target, 6, 9, 1, 1)

        self.target_label = QLabel(self.frame_4)
        self.target_label.setObjectName("target_label")
        self.target_label.setFont(font1)

        self.gridLayout_26.addWidget(self.target_label, 6, 1, 1, 1, Qt.AlignHCenter)

        self.sensor_B_right_angle = QLineEdit(self.frame_4)
        self.sensor_B_right_angle.setObjectName("sensor_B_right_angle")
        self.sensor_B_right_angle.setReadOnly(True)

        self.gridLayout_26.addWidget(self.sensor_B_right_angle, 4, 7, 1, 1)

        self.face_width_width = QLabel(self.frame_4)
        self.face_width_width.setObjectName("face_width_width")
        self.face_width_width.setFont(font1)

        self.gridLayout_26.addWidget(self.face_width_width, 0, 5, 1, 1, Qt.AlignHCenter)

        self.sensor_A_end_angle = QLineEdit(self.frame_4)
        self.sensor_A_end_angle.setObjectName("sensor_A_end_angle")
        self.sensor_A_end_angle.setReadOnly(True)

        self.gridLayout_26.addWidget(self.sensor_A_end_angle, 2, 3, 1, 1)

        self.sensor_B_end_angle = QLineEdit(self.frame_4)
        self.sensor_B_end_angle.setObjectName("sensor_B_end_angle")
        self.sensor_B_end_angle.setReadOnly(True)

        self.gridLayout_26.addWidget(self.sensor_B_end_angle, 4, 3, 1, 1)

        self.face_width_target = QLineEdit(self.frame_4)
        self.face_width_target.setObjectName("face_width_target")
        self.face_width_target.setReadOnly(True)

        self.gridLayout_26.addWidget(self.face_width_target, 6, 5, 1, 1)

        self.horizontalSpacer_18 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.gridLayout_26.addItem(self.horizontalSpacer_18, 0, 6, 1, 1)

        self.sensor_A_right_angle = QLineEdit(self.frame_4)
        self.sensor_A_right_angle.setObjectName("sensor_A_right_angle")
        self.sensor_A_right_angle.setReadOnly(True)

        self.gridLayout_26.addWidget(self.sensor_A_right_angle, 2, 7, 1, 1)

        self.end_angle_label = QLabel(self.frame_4)
        self.end_angle_label.setObjectName("end_angle_label")
        self.end_angle_label.setFont(font1)

        self.gridLayout_26.addWidget(self.end_angle_label, 0, 3, 1, 1, Qt.AlignHCenter)

        self.sensor_A_face_width = QLineEdit(self.frame_4)
        self.sensor_A_face_width.setObjectName("sensor_A_face_width")
        self.sensor_A_face_width.setReadOnly(True)

        self.gridLayout_26.addWidget(self.sensor_A_face_width, 2, 5, 1, 1)

        self.sensor_A_detection_value = QLineEdit(self.frame_4)
        self.sensor_A_detection_value.setObjectName("sensor_A_detection_value")
        self.sensor_A_detection_value.setReadOnly(True)

        self.gridLayout_26.addWidget(self.sensor_A_detection_value, 2, 9, 1, 1)

        self.detection_value_label = QLabel(self.frame_4)
        self.detection_value_label.setObjectName("detection_value_label")
        self.detection_value_label.setFont(font1)

        self.gridLayout_26.addWidget(
            self.detection_value_label, 0, 9, 1, 1, Qt.AlignHCenter
        )

        self.final_detection_result = QLineEdit(self.frame_4)
        self.final_detection_result.setObjectName("final_detection_result")
        self.final_detection_result.setReadOnly(True)

        self.gridLayout_26.addWidget(self.final_detection_result, 8, 9, 1, 1)

        self.horizontalSpacer_47 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.gridLayout_26.addItem(self.horizontalSpacer_47, 0, 0, 1, 1)

        self.verticalSpacer_37 = QSpacerItem(
            20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.gridLayout_26.addItem(self.verticalSpacer_37, 1, 0, 1, 1)

        self.verticalSpacer_48 = QSpacerItem(
            40, 20, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.gridLayout_26.addItem(self.verticalSpacer_48, 9, 0, 1, 1)

        self.verticalSpacer_17 = QSpacerItem(
            20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.gridLayout_26.addItem(self.verticalSpacer_17, 3, 0, 1, 1)

        self.verticalSpacer_36 = QSpacerItem(
            20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.gridLayout_26.addItem(self.verticalSpacer_36, 5, 0, 1, 1)

        self.verticalSpacer_26 = QSpacerItem(
            40, 20, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.gridLayout_26.addItem(self.verticalSpacer_26, 7, 0, 1, 1)

        self.gridLayout.addLayout(self.gridLayout_26, 0, 1, 1, 1)

        self.frame_6 = QFrame(self.tab_home)
        self.frame_6.setObjectName("frame_6")
        self.frame_6.setGeometry(QRect(20, 400, 392, 236))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_6)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_29 = QGridLayout()
        self.gridLayout_29.setObjectName("gridLayout_29")
        self.counter = QLineEdit(self.frame_6)
        self.counter.setObjectName("counter")
        self.counter.setReadOnly(True)

        self.gridLayout_29.addWidget(self.counter, 3, 3, 1, 1)

        self.horizontalSpacer_46 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.gridLayout_29.addItem(self.horizontalSpacer_46, 0, 0, 1, 1)

        self.horizontalSpacer_40 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.gridLayout_29.addItem(self.horizontalSpacer_40, 0, 4, 1, 1)

        self.ng_counter = QLineEdit(self.frame_6)
        self.ng_counter.setObjectName("ng_counter")
        self.ng_counter.setReadOnly(True)

        self.gridLayout_29.addWidget(self.ng_counter, 7, 3, 1, 1)

        self.ng_counter_label = QLabel(self.frame_6)
        self.ng_counter_label.setObjectName("ng_counter_label")
        self.ng_counter_label.setFont(font1)

        self.gridLayout_29.addWidget(self.ng_counter_label, 7, 1, 1, 1, Qt.AlignHCenter)

        self.tatal_label = QLabel(self.frame_6)
        self.tatal_label.setObjectName("tatal_label")
        self.tatal_label.setFont(font1)

        self.gridLayout_29.addWidget(self.tatal_label, 5, 1, 1, 1, Qt.AlignHCenter)

        self.clean_label_14 = QLabel(self.frame_6)
        self.clean_label_14.setObjectName("clean_label_14")
        self.clean_label_14.setFont(font1)

        self.gridLayout_29.addWidget(self.clean_label_14, 0, 3, 1, 1, Qt.AlignHCenter)

        self.counter_label = QLabel(self.frame_6)
        self.counter_label.setObjectName("counter_label")
        self.counter_label.setFont(font1)

        self.gridLayout_29.addWidget(self.counter_label, 3, 1, 1, 1, Qt.AlignHCenter)

        self.total = QLineEdit(self.frame_6)
        self.total.setObjectName("total")
        self.total.setReadOnly(True)

        self.gridLayout_29.addWidget(self.total, 5, 3, 1, 1)

        self.horizontalSpacer_44 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.gridLayout_29.addItem(self.horizontalSpacer_44, 0, 2, 1, 1)

        self.verticalSpacer_52 = QSpacerItem(
            20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.gridLayout_29.addItem(self.verticalSpacer_52, 1, 0, 1, 1)

        self.verticalSpacer_50 = QSpacerItem(
            40, 20, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.gridLayout_29.addItem(self.verticalSpacer_50, 8, 0, 1, 1)

        self.verticalSpacer_49 = QSpacerItem(
            20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.gridLayout_29.addItem(self.verticalSpacer_49, 6, 0, 1, 1)

        self.verticalSpacer_53 = QSpacerItem(
            20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.gridLayout_29.addItem(self.verticalSpacer_53, 4, 0, 1, 1)

        self.gridLayout_4.addLayout(self.gridLayout_29, 0, 0, 1, 1)

        self.frame_7 = QFrame(self.tab_home)
        self.frame_7.setObjectName("frame_7")
        self.frame_7.setGeometry(QRect(530, 400, 316, 154))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_7)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_30 = QGridLayout()
        self.gridLayout_30.setObjectName("gridLayout_30")
        self.verticalSpacer_56 = QSpacerItem(
            20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.gridLayout_30.addItem(self.verticalSpacer_56, 3, 0, 1, 1)

        self.startBtn = QPushButton(self.frame_7)
        self.startBtn.setObjectName("startBtn")

        self.gridLayout_30.addWidget(self.startBtn, 2, 1, 1, 1)

        self.horizontalSpacer_49 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.gridLayout_30.addItem(self.horizontalSpacer_49, 0, 2, 1, 1)

        self.restartBtn = QPushButton(self.frame_7)
        self.restartBtn.setObjectName("restartBtn")

        self.gridLayout_30.addWidget(self.restartBtn, 4, 1, 1, 1)

        self.closeBtn = QPushButton(self.frame_7)
        self.closeBtn.setObjectName("closeBtn")

        self.gridLayout_30.addWidget(self.closeBtn, 4, 3, 1, 1)

        self.horizontalSpacer_48 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.gridLayout_30.addItem(self.horizontalSpacer_48, 0, 0, 1, 1)

        self.pauseBtn = QPushButton(self.frame_7)
        self.pauseBtn.setObjectName("pauseBtn")

        self.gridLayout_30.addWidget(self.pauseBtn, 2, 3, 1, 1)

        self.verticalSpacer_51 = QSpacerItem(
            40, 20, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.gridLayout_30.addItem(self.verticalSpacer_51, 5, 0, 1, 1)

        self.horizontalSpacer_45 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.gridLayout_30.addItem(self.horizontalSpacer_45, 0, 4, 1, 1)

        self.gridLayout_6.addLayout(self.gridLayout_30, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_home, "")
        self.tab_action_setting = QWidget()
        self.tab_action_setting.setObjectName("tab_action_setting")
        self.frame = QFrame(self.tab_action_setting)
        self.frame.setObjectName("frame")
        self.frame.setGeometry(QRect(40, 20, 941, 580))
        self.frame.setMinimumSize(QSize(900, 580))
        self.frame.setMaximumSize(QSize(991, 561))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayoutWidget_5 = QWidget(self.frame)
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")
        self.gridLayoutWidget_5.setGeometry(QRect(20, 110, 491, 26))
        self.gridLayout_18 = QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.gridLayout_18.setContentsMargins(0, 0, 0, 0)
        self.power_btn = QPushButton(self.gridLayoutWidget_5)
        self.power_btn.setObjectName("power_btn")
        self.power_btn.setEnabled(True)

        self.gridLayout_18.addWidget(self.power_btn, 1, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(
            10, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.gridLayout_18.addItem(self.horizontalSpacer_4, 1, 1, 1, 1)

        self.stop_btn = QPushButton(self.gridLayoutWidget_5)
        self.stop_btn.setObjectName("stop_btn")
        self.stop_btn.setEnabled(False)
        self.stop_btn.setCheckable(False)

        self.gridLayout_18.addWidget(self.stop_btn, 1, 2, 1, 1)

        self.auto_mode_btn = QPushButton(self.gridLayoutWidget_5)
        self.auto_mode_btn.setObjectName("auto_mode_btn")
        self.auto_mode_btn.setEnabled(False)

        self.gridLayout_18.addWidget(self.auto_mode_btn, 1, 5, 1, 1)

        self.horizontalSpacer_11 = QSpacerItem(
            10, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.gridLayout_18.addItem(self.horizontalSpacer_11, 1, 6, 1, 1)

        self.manual_mode_btn = QPushButton(self.gridLayoutWidget_5)
        self.manual_mode_btn.setObjectName("manual_mode_btn")
        self.manual_mode_btn.setEnabled(False)

        self.gridLayout_18.addWidget(self.manual_mode_btn, 1, 4, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(
            10, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.gridLayout_18.addItem(self.horizontalSpacer_5, 1, 3, 1, 1)

        self.exit_btn = QPushButton(self.gridLayoutWidget_5)
        self.exit_btn.setObjectName("exit_btn")
        self.exit_btn.setEnabled(False)

        self.gridLayout_18.addWidget(self.exit_btn, 1, 7, 1, 1)

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
        self.check_stopper_cyl_up_btn.setEnabled(False)

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
        self.check_fixed_position_CYL_down_btn.setEnabled(False)

        self.gridLayout_22.addWidget(self.check_fixed_position_CYL_down_btn, 6, 4, 1, 1)

        self.check_fixed_position_CYL_up_btn = QPushButton(self.gridLayoutWidget_7)
        self.check_fixed_position_CYL_up_btn.setObjectName(
            "check_fixed_position_CYL_up_btn"
        )
        self.check_fixed_position_CYL_up_btn.setEnabled(False)

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
        self.check_stopper_cyl_down_btn.setEnabled(False)

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
        self.clean_fixed_position_CYL_up_btn.setEnabled(False)

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
        self.clean_stopper_cyl_up_btn.setEnabled(False)

        self.gridLayout_23.addWidget(
            self.clean_stopper_cyl_up_btn, 3, 2, 1, 1, Qt.AlignHCenter
        )

        self.clean_fixed_position_CYL_down_btn = QPushButton(self.gridLayoutWidget_6)
        self.clean_fixed_position_CYL_down_btn.setObjectName(
            "clean_fixed_position_CYL_down_btn"
        )
        self.clean_fixed_position_CYL_down_btn.setEnabled(False)

        self.gridLayout_23.addWidget(self.clean_fixed_position_CYL_down_btn, 5, 4, 1, 1)

        self.clean_stopper_cyl_down_btn = QPushButton(self.gridLayoutWidget_6)
        self.clean_stopper_cyl_down_btn.setObjectName("clean_stopper_cyl_down_btn")
        self.clean_stopper_cyl_down_btn.setEnabled(False)

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
        self.pomp_check_CYL_open_btn.setEnabled(False)

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
        self.pomp_check_CYL_close_btn.setEnabled(False)

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
        self.pomp_power_close_btn.setEnabled(False)

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
        self.pomp_power_open_btn.setEnabled(False)

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
        self.airValue_value_open_btn.setEnabled(False)

        self.gridLayout_25.addWidget(
            self.airValue_value_open_btn, 4, 2, 1, 1, Qt.AlignHCenter
        )

        self.air_value_close_btn = QPushButton(self.gridLayoutWidget_9)
        self.air_value_close_btn.setObjectName("air_value_close_btn")
        self.air_value_close_btn.setEnabled(False)

        self.gridLayout_25.addWidget(self.air_value_close_btn, 6, 4, 1, 1)

        self.air_value_label = QLabel(self.gridLayoutWidget_9)
        self.air_value_label.setObjectName("air_value_label")
        self.air_value_label.setFont(font1)

        self.gridLayout_25.addWidget(self.air_value_label, 6, 0, 1, 1, Qt.AlignLeft)

        self.air_value_open_btn = QPushButton(self.gridLayoutWidget_9)
        self.air_value_open_btn.setObjectName("air_value_open_btn")
        self.air_value_open_btn.setEnabled(False)

        self.gridLayout_25.addWidget(self.air_value_open_btn, 6, 2, 1, 1)

        self.airValue_value_label = QLabel(self.gridLayoutWidget_9)
        self.airValue_value_label.setObjectName("airValue_value_label")
        self.airValue_value_label.setFont(font1)

        self.gridLayout_25.addWidget(
            self.airValue_value_label, 4, 0, 1, 1, Qt.AlignLeft
        )

        self.airValue_value_close_btn = QPushButton(self.gridLayoutWidget_9)
        self.airValue_value_close_btn.setObjectName("airValue_value_close_btn")
        self.airValue_value_close_btn.setEnabled(False)

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
        self.power_status_label.setGeometry(QRect(20, 60, 431, 31))
        self.tabWidget.addTab(self.tab_action_setting, "")
        self.tab_setting = QWidget()
        self.tab_setting.setObjectName("tab_setting")
        self.frame_3 = QFrame(self.tab_setting)
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
        font2 = QFont()
        font2.setFamilies(["Cascadia Code"])
        font2.setPointSize(20)
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

        self.tabWidget.addTab(self.tab_setting, "")
        self.tab_alarm = QWidget()
        self.tab_alarm.setObjectName("tab_alarm")
        self.frame_5 = QFrame(self.tab_alarm)
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

        self.tabWidget.addTab(self.tab_alarm, "")

        self.horizontalLayout.addWidget(self.tabWidget)

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
        self.sensor_B_label_2.setText(
            QCoreApplication.translate("MainWindow", "B \u93e1\u982d", None)
        )
        self.final_detection_result_label.setText(
            QCoreApplication.translate(
                "MainWindow", "\u6700\u7d42\u6aa2\u6e2c\u7d50\u679c", None
            )
        )
        self.sensor_A_label.setText(
            QCoreApplication.translate("MainWindow", "A \u93e1\u982d", None)
        )
        self.right_angle_label.setText(
            QCoreApplication.translate("MainWindow", "\u76f4\u89d2\u5ea6", None)
        )
        self.target_label.setText(
            QCoreApplication.translate("MainWindow", "\u76ee\u6a19\u503c", None)
        )
        self.face_width_width.setText(
            QCoreApplication.translate("MainWindow", "\u7aef\u9762\u5bec\u5ea6", None)
        )
        self.end_angle_label.setText(
            QCoreApplication.translate("MainWindow", "\u7aef\u9762\u89d2\u5ea6", None)
        )
        self.detection_value_label.setText(
            QCoreApplication.translate("MainWindow", "\u6aa2\u6e2c\u503c", None)
        )
        self.ng_counter_label.setText(
            QCoreApplication.translate("MainWindow", "NG \u6578\u91cf", None)
        )
        self.tatal_label.setText(
            QCoreApplication.translate(
                "MainWindow", "\u751f\u7522\u7e3d\u6578\u91cf", None
            )
        )
        self.clean_label_14.setText(
            QCoreApplication.translate("MainWindow", "\u6578\u91cf", None)
        )
        self.counter_label.setText(
            QCoreApplication.translate("MainWindow", "\u8a08\u6578", None)
        )
        self.startBtn.setText(
            QCoreApplication.translate("MainWindow", "\u958b\u59cb", None)
        )
        self.restartBtn.setText(
            QCoreApplication.translate("MainWindow", "\u91cd\u555f", None)
        )
        self.closeBtn.setText(
            QCoreApplication.translate("MainWindow", "\u95dc\u9589", None)
        )
        self.pauseBtn.setText(
            QCoreApplication.translate("MainWindow", "\u66ab\u505c", None)
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_home),
            QCoreApplication.translate("MainWindow", "\u9996\u9801", None),
        )
        self.power_btn.setText(
            QCoreApplication.translate("MainWindow", "\u96fb\u6e90", None)
        )
        self.stop_btn.setText(
            QCoreApplication.translate("MainWindow", "\u505c\u6b62", None)
        )
        self.auto_mode_btn.setText(
            QCoreApplication.translate("MainWindow", "\u81ea\u52d5\u6a21\u5f0f", None)
        )
        self.manual_mode_btn.setText(
            QCoreApplication.translate("MainWindow", "\u624b\u52d5\u6a21\u5f0f", None)
        )
        self.exit_btn.setText(
            QCoreApplication.translate("MainWindow", "\u9000\u51fa", None)
        )
        self.check_label.setText(
            QCoreApplication.translate("MainWindow", "\u6aa2\u67e5\u88fd\u7a0b", None)
        )
        self.check_fixed_position_CYL_label.setText(
            QCoreApplication.translate(
                "MainWindow", "Position \u78c1\u7c27\u958b\u95dc", None
            )
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
            QCoreApplication.translate(
                "MainWindow", "STOPPER \u78c1\u7c27\u958b\u95dc", None
            )
        )
        self.clean_fixed_position_CYL_up_btn.setText(
            QCoreApplication.translate("MainWindow", "\u4e0a\u5347", None)
        )
        self.clean_stopper_cyl_label.setText(
            QCoreApplication.translate(
                "MainWindow", "STOPPER \u78c1\u7c27\u958b\u95dc", None
            )
        )
        self.clean_fixed_position_CYL_label.setText(
            QCoreApplication.translate(
                "MainWindow", "Position \u78c1\u7c27\u958b\u95dc", None
            )
        )
        self.clean_label.setText(
            QCoreApplication.translate("MainWindow", "\u6e05\u6d17\u88fd\u7a0b", None)
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
        self.pomp_label.setText(QCoreApplication.translate("MainWindow", "PUMP", None))
        self.pomp_power_label.setText(
            QCoreApplication.translate("MainWindow", "\u96fb\u6e90", None)
        )
        self.pomp_check_CYL_close_btn.setText(
            QCoreApplication.translate("MainWindow", "\u95dc\u9589", None)
        )
        self.pomp_check_CYL_label.setText(
            QCoreApplication.translate("MainWindow", "\u96f7\u5c04\u6a5f\u69cb", None)
        )
        self.pomp_power_close_btn.setText(
            QCoreApplication.translate("MainWindow", "\u95dc\u9589", None)
        )
        self.pomp_power_open_btn.setText(
            QCoreApplication.translate("MainWindow", "\u6253\u958b", None)
        )
        self.airValue_value_open_btn.setText(
            QCoreApplication.translate("MainWindow", "\u6253\u958b", None)
        )
        self.air_value_close_btn.setText(
            QCoreApplication.translate("MainWindow", "\u95dc\u9589", None)
        )
        self.air_value_label.setText(
            QCoreApplication.translate("MainWindow", "\u5439\u6c23", None)
        )
        self.air_value_open_btn.setText(
            QCoreApplication.translate("MainWindow", "\u6253\u958b", None)
        )
        self.airValue_value_label.setText(
            QCoreApplication.translate("MainWindow", "\u96fb\u78c1\u95a5", None)
        )
        self.airValue_value_close_btn.setText(
            QCoreApplication.translate("MainWindow", "\u95dc\u9589", None)
        )
        self.air_value_title_label.setText(
            QCoreApplication.translate("MainWindow", "\u96fb\u78c1\u95a5", None)
        )
        self.power_status_label.setText("")
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_action_setting),
            QCoreApplication.translate("MainWindow", "\u52d5\u4f5c\u8a2d\u5b9a", None),
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
            self.tabWidget.indexOf(self.tab_setting),
            QCoreApplication.translate("MainWindow", "\u8a2d\u5b9a", None),
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
            self.tabWidget.indexOf(self.tab_alarm),
            QCoreApplication.translate("MainWindow", "\u7570\u5e38\u7d00\u9304", None),
        )

    # retranslateUi
