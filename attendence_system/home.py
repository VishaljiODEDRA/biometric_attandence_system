from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *
from PyQt5.QtCore import QTimer, QTime, Qt


def initUI(self):
    self.msg_label = QtWidgets.QLabel(self)
    self.msg_label.setGeometry(QtCore.QRect(70, 40, 711, 51))
    self.font = QtGui.QFont()
    self.font.setFamily("Futura")
    self.font.setPointSize(36)
    self.msg_label.setFont(self.font)
    self.msg_label.setObjectName("msg_label")
    self.msg_label.setText("Welcome to Biometric Attendence System!")
    #
    self.image = QtWidgets.QLabel(self)
    self.image.setGeometry(QtCore.QRect(390, 150, 411, 231))
    self.image.setText("")
    self.image.setPixmap(
        QtGui.QPixmap(
            "/Users/vishaljiodedra/OneDrive - Birmingham City University/Cloud Based Attendence System/Images/secure_attendance_system.png"
        ))
    self.image.setScaledContents(True)
    self.image.setObjectName("image")
    #
    self.start_cam = QtWidgets.QPushButton(self)
    self.start_cam.setGeometry(QtCore.QRect(50, 220, 251, 91))
    self.start_cam.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
    self.start_cam.setText("Start Camera")
    self.start_cam.setAutoFillBackground(False)
    self.start_cam.setStyleSheet("QPushButton{\n"
                                 "font: 500 24pt \"Futura\";\n"
                                 "background-color: rgb(193, 193, 193);\n"
                                 "border-radius: 15px;\n"
                                 "}\n"
                                 "QPushButton:pressed{\n"
                                 "    background-color: rgb(255, 255, 255);\n"
                                 "}")
    self.start_cam.setObjectName("start_cam")
    self.start_cam.setCheckable(True)
    self.start_cam.clicked.connect(self.face_detection)
    #
    self.mark_manu = QtWidgets.QPushButton(self)
    self.mark_manu.setGeometry(QtCore.QRect(130, 460, 231, 70))
    self.mark_manu.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
    self.mark_manu.setStyleSheet("QPushButton{\n"
                                 "font: 500 24pt \"Futura\";\n"
                                 "background-color: rgb(193, 193, 193);\n"
                                 "border-radius: 15px;\n"
                                 "}\n"
                                 "QPushButton:pressed{\n"
                                 "    background-color: rgb(255, 255, 255);\n"
                                 "}")
    self.mark_manu.setObjectName("mark_manu")
    self.mark_manu.setText("Mark Manually")
    self.mark_manu.setCheckable(True)
    self.mark_manu.clicked.connect(self.login_setup_ui)
    #
    self.time_table = QtWidgets.QPushButton(self)
    self.time_table.setGeometry(QtCore.QRect(500, 460, 200, 70))
    self.time_table.setText("Time-table")
    self.time_table.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
    self.time_table.setStyleSheet("QPushButton{\n"
                                  "font: 500 24pt \"Futura\";\n"
                                  "background-color: rgb(193, 193, 193);\n"
                                  "border-radius: 15px;\n"
                                  "}\n"
                                  "QPushButton:pressed{\n"
                                  "    background-color: rgb(255, 255, 255);\n"
                                  "}")
    self.time_table.setObjectName("time_table")
    self.time_table.clicked.connect(self.time_table1)
    #
    self.room_no_labl = QtWidgets.QLabel(self)
    self.room_no_labl.setGeometry(QtCore.QRect(1, 1, 200, 30))
    self.font = QtGui.QFont()
    self.font.setFamily("Futura")
    self.font.setPointSize(22)
    self.room_no_labl.setFont(self.font)
    self.room_no_labl.setObjectName("room_no_labl")
    self.room_no_labl.setText("Room: CZ199")
    self.room_no_labl.show()
    #
    self.msg_label.show()
    self.start_cam.show()
    self.mark_manu.show()
    self.image.show()
    self.time_table.show()
