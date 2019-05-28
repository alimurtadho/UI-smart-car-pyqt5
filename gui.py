# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
import time
import engine

class TTT(QThread):

    progress_update     = pyqtSignal(int)
    mileage_update      = pyqtSignal(int)
    speedometer_update  = pyqtSignal(int)

    def __init__(self, ui):
        super(TTT, self).__init__()
        self.ui = ui
        self.quit_flag          = False
        self.s_depan            = 0
        self.s_belakang         = 0
        self.s_depan_kiri       = 0
        self.s_depan_kanan      = 0
        self.s_kanan            = 0
        self.s_kiri             = 0
        self.jarak_tempuh       = 0
        self.pesan_aksi         = ""

    def loopSensors(self):
        engine.start_engine()

    def getValueSensors(self):
        self.s_depan            = engine.sensor_depan.value
        self.s_belakang         = engine.sensor_belakang.value
        self.s_depan_kiri       = engine.sensor_depan_kiri.value
        self.s_depan_kanan      = engine.sensor_depan_kanan.value
        self.s_kanan            = engine.sensor_kanan.value
        self.s_kiri             = engine.sensor_kiri.value

        self.progress_update.emit(engine.energy.value)
        self.mileage_update.emit(engine.jarak_tempuh.value)
        self.speedometer_update.emit(engine.kecepatan.value)

        self.jarak_tempuh            = engine.jarak_tempuh.value
        self.pesan_aksi_sensor_jarak = engine.pesan_aksi_sensor_jarak.value

        _translate = QtCore.QCoreApplication.translate
        self.ui.txtSensorDepan.setText(_translate("MainWindow", str(self.s_depan)))
        self.ui.txtSensorBelakang.setText(_translate("MainWindow", str(self.s_belakang)))
        self.ui.txtSensorDepanKiri.setText(_translate("MainWindow", str(self.s_depan_kiri)))
        self.ui.txtSensorDepanKanan.setText(_translate("MainWindow", str(self.s_depan_kanan)))
        self.ui.txtSensorKiri.setText(_translate("MainWindow", str(self.s_kiri)))
        self.ui.txtSensorKanan.setText(_translate("MainWindow", str(self.s_kanan)))

        self.ui.txtSensorActionMessage.setText(_translate("MainWindow", self.pesan_aksi_sensor_jarak))

    def run(self):
        while self.jarak_tempuh <= 30000:
            self.loopSensors()
            time.sleep(0.5)
            self.getValueSensors()
            time.sleep(0.5)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1027, 435)
        MainWindow.setStyleSheet("background-color : rgb(85, 87, 83)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 20, 291, 391))
        self.frame.setStyleSheet("background-color:rgb(46, 52, 54);\n"
"border-radius:5px")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setObjectName("frame")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(200, 140, 71, 81))
        self.label_9.setStyleSheet("color : rgb(238, 238, 236)")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(20, 140, 71, 81))
        self.label_4.setStyleSheet("color : rgb(238, 238, 236)")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(110, 220, 71, 81))
        self.label_10.setStyleSheet("color : rgb(238, 238, 236)")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.txtSensorKanan = QtWidgets.QLabel(self.frame)
        self.txtSensorKanan.setGeometry(QtCore.QRect(200, 170, 74, 18))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.txtSensorKanan.setFont(font)
        self.txtSensorKanan.setStyleSheet("color : rgb(238, 238, 236);\n"
"background-color: rgba(0,0,0,0%)")
        self.txtSensorKanan.setAlignment(QtCore.Qt.AlignCenter)
        self.txtSensorKanan.setObjectName("txtSensorKanan")
        self.txtSensorKiri = QtWidgets.QLabel(self.frame)
        self.txtSensorKiri.setGeometry(QtCore.QRect(20, 170, 74, 18))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.txtSensorKiri.setFont(font)
        self.txtSensorKiri.setStyleSheet("color : rgb(238, 238, 236);\n"
"background-color: rgba(0,0,0,0%)")
        self.txtSensorKiri.setAlignment(QtCore.Qt.AlignCenter)
        self.txtSensorKiri.setObjectName("txtSensorKiri")
        self.txtSensorBelakang = QtWidgets.QLabel(self.frame)
        self.txtSensorBelakang.setGeometry(QtCore.QRect(110, 250, 74, 18))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.txtSensorBelakang.setFont(font)
        self.txtSensorBelakang.setStyleSheet("color : rgb(238, 238, 236);\n"
"background-color: rgba(0,0,0,0%)")
        self.txtSensorBelakang.setAlignment(QtCore.Qt.AlignCenter)
        self.txtSensorBelakang.setObjectName("txtSensorBelakang")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(20, 50, 71, 81))
        self.label.setStyleSheet("color : rgb(238, 238, 236)")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.txtSensorDepanKiri = QtWidgets.QLabel(self.frame)
        self.txtSensorDepanKiri.setGeometry(QtCore.QRect(20, 80, 71, 18))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setKerning(True)
        self.txtSensorDepanKiri.setFont(font)
        self.txtSensorDepanKiri.setAutoFillBackground(False)
        self.txtSensorDepanKiri.setStyleSheet("color : rgb(238, 238, 236);\n"
"background-color: rgba(0,0,0,0%)")
        self.txtSensorDepanKiri.setAlignment(QtCore.Qt.AlignCenter)
        self.txtSensorDepanKiri.setObjectName("txtSensorDepanKiri")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(200, 50, 71, 81))
        self.label_8.setStyleSheet("color : rgb(238, 238, 236)")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.txtSensorDepanKanan = QtWidgets.QLabel(self.frame)
        self.txtSensorDepanKanan.setGeometry(QtCore.QRect(200, 80, 74, 18))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.txtSensorDepanKanan.setFont(font)
        self.txtSensorDepanKanan.setStyleSheet("color : rgb(238, 238, 236);\n"
"background-color: rgba(0,0,0,0%)")
        self.txtSensorDepanKanan.setAlignment(QtCore.Qt.AlignCenter)
        self.txtSensorDepanKanan.setObjectName("txtSensorDepanKanan")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(110, 40, 71, 81))
        self.label_7.setStyleSheet("color : rgb(238, 238, 236)")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.txtSensorDepan = QtWidgets.QLabel(self.frame)
        self.txtSensorDepan.setGeometry(QtCore.QRect(110, 70, 74, 18))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.txtSensorDepan.setFont(font)
        self.txtSensorDepan.setStyleSheet("color : rgb(238, 238, 236);\n"
"background-color: rgba(0,0,0,0%);")
        self.txtSensorDepan.setAlignment(QtCore.Qt.AlignCenter)
        self.txtSensorDepan.setObjectName("txtSensorDepan")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 271, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color : rgb(238, 238, 236);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(20, 320, 251, 51))
        self.line.setStyleSheet("background-color:rgb(85, 87, 83)")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.txtSensorActionMessage = QtWidgets.QLabel(self.frame)
        self.txtSensorActionMessage.setGeometry(QtCore.QRect(30, 330, 231, 31))
        self.txtSensorActionMessage.setStyleSheet("color:rgb(238, 238, 236);\n"
"background-color: rgba(0,0,0,0%);")
        self.txtSensorActionMessage.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.txtSensorActionMessage.setObjectName("txtSensorActionMessage")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(330, 20, 521, 391))
        self.frame_2.setStyleSheet("background-color:rgb(46, 52, 54);\n"
"border-radius:5px\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 501, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color : rgb(238, 238, 236);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.txtSpeedometer = QtWidgets.QLabel(self.frame_2)
        self.txtSpeedometer.setGeometry(QtCore.QRect(150, 80, 191, 171))
        font = QtGui.QFont()
        font.setFamily("FreeSans")
        font.setPointSize(100)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.txtSpeedometer.setFont(font)
        self.txtSpeedometer.setStyleSheet("color:rgb(238, 238, 236)")
        self.txtSpeedometer.setAlignment(QtCore.Qt.AlignCenter)
        self.txtSpeedometer.setObjectName("txtSpeedometer")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(230, 230, 51, 21))
        font = QtGui.QFont()
        font.setFamily("FreeSans")
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color:rgb(238, 238, 236)")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setGeometry(QtCore.QRect(30, 330, 161, 41))
        self.frame_3.setStyleSheet("background-color:rgb(40, 40, 40)")
        self.frame_3.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_3.setObjectName("frame_3")
        self.txtMileage = QtWidgets.QLabel(self.frame_3)
        self.txtMileage.setGeometry(QtCore.QRect(0, 10, 161, 20))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(18)
        self.txtMileage.setFont(font)
        self.txtMileage.setStyleSheet("color:rgb(238, 238, 236)")
        self.txtMileage.setAlignment(QtCore.Qt.AlignCenter)
        self.txtMileage.setObjectName("txtMileage")
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(30, 300, 161, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color : rgb(238, 238, 236);")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.line_2 = QtWidgets.QFrame(self.frame_2)
        self.line_2.setGeometry(QtCore.QRect(40, 20, 118, 3))
        self.line_2.setStyleSheet("background-color:rgb(238, 238, 236)")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.frame_2)
        self.line_3.setGeometry(QtCore.QRect(360, 20, 118, 3))
        self.line_3.setStyleSheet("background-color:rgb(238, 238, 236)")
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setGeometry(QtCore.QRect(220, 330, 271, 41))
        self.frame_4.setStyleSheet("background-color:rgb(40, 40, 40)")
        self.frame_4.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_4.setObjectName("frame_4")
        self.energyBar = QtWidgets.QProgressBar(self.frame_4)
        self.energyBar.setGeometry(QtCore.QRect(10, 10, 251, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.energyBar.setFont(font)
        self.energyBar.setStyleSheet("color:rgb(238, 238, 236)")
        self.energyBar.setMaximum(30000)
        self.energyBar.setProperty("value", 30000)
        self.energyBar.setAlignment(QtCore.Qt.AlignCenter)
        self.energyBar.setObjectName("energyBar")
        self.label_11 = QtWidgets.QLabel(self.frame_2)
        self.label_11.setGeometry(QtCore.QRect(230, 300, 251, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color : rgb(238, 238, 236);")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.t = TTT(self)
        self.t.progress_update.connect(self.updateProgressBar)
        self.t.mileage_update.connect(self.updateMileage)
        self.t.speedometer_update.connect(self.updateSpeedometer)
        self.t.start()

    def updateProgressBar(self, value):
        self.energyBar.setValue(value)

    def updateMileage(self, value):
        _translate = QtCore.QCoreApplication.translate
        self.txtMileage.setText(_translate("MainWindow", str(value)).zfill(10))

    def updateSpeedometer(self, value):
        _translate = QtCore.QCoreApplication.translate
        self.txtSpeedometer.setText(_translate("MainWindow", str(value)))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Dashboard Smart Car"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/newPrefix/circle.png\" width=\"70\"/></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/newPrefix/circle.png\" width=\"70\"/></p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/newPrefix/circle.png\" width=\"70\"/></p></body></html>"))
        self.txtSensorKanan.setText(_translate("MainWindow", "0"))
        self.txtSensorKiri.setText(_translate("MainWindow", "0"))
        self.txtSensorBelakang.setText(_translate("MainWindow", "0"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/newPrefix/circle.png\" width=\"70\"/></p></body></html>"))
        self.txtSensorDepanKiri.setText(_translate("MainWindow", "0"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/newPrefix/circle.png\" width=\"70\"/></p></body></html>"))
        self.txtSensorDepanKanan.setText(_translate("MainWindow", "0"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/newPrefix/circle.png\" width=\"70\"/></p></body></html>"))
        self.txtSensorDepan.setText(_translate("MainWindow", "0"))
        self.label_2.setText(_translate("MainWindow", "SENSORS PANEL"))
        self.txtSensorActionMessage.setText(_translate("MainWindow", "......"))
        self.label_3.setText(_translate("MainWindow", "MAIN PANEL"))
        self.txtSpeedometer.setText(_translate("MainWindow", "0"))
        self.label_6.setText(_translate("MainWindow", "km/h"))
        self.txtMileage.setText(_translate("MainWindow", "0000000000"))
        self.label_5.setText(_translate("MainWindow", "MILEAGE IN METER"))
        self.label_11.setText(_translate("MainWindow", "ENERGY"))

import circle_rc

if __name__ == '__main__':
        import sys

        app = QtWidgets.QApplication(sys.argv)
        dashboard = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(dashboard)
        dashboard.show()
        app.exec_()