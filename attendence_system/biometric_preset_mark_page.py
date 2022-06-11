from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *
import pandas as pd


def biometric_present(self):
    self.back_but = QtWidgets.QPushButton(self)
    self.back_but.setGeometry(QtCore.QRect(530, 500, 200, 50))
    self.back_but.setStyleSheet("QPushButton{\n"
                                "    font: 500 28pt \"Futura\";\n"
                                "    background-color: rgb(193, 193, 193);\n"
                                "    border-radius: 15px;\n"
                                "}\n"
                                "QPushButton:pressed{\n"
                                "    background-color: rgb(255, 255, 255);\n"
                                "}\n"
                                "")
    self.back_but.setObjectName("back_but")
    self.back_but.setText("Thank You")
    self.back_but.clicked.connect(self.go_back_to_home1)

    #
    self.welcome_name = QtWidgets.QLabel(self)
    self.welcome_name.setGeometry(QtCore.QRect(130, 40, 650, 50))
    self.font = QtGui.QFont()
    self.font.setFamily("Futura")
    self.font.setPointSize(30)
    self.welcome_name.setFont(self.font)
    self.welcome_name.setObjectName("welcome_name")
    self.welcome_name.setText(self.welcome_msg)

    #
    self.image2 = QtWidgets.QLabel(self)
    self.image2.setGeometry(QtCore.QRect(200, 120, 150, 150))
    self.image2.setText("")
    self.image2.setPixmap(QtGui.QPixmap(self.biometric_face))
    self.image2.setScaledContents(True)
    self.image2.setObjectName("image2")

    #
    self.image3 = QtWidgets.QLabel(self)
    self.image3.setGeometry(QtCore.QRect(550, 120, 150, 150))
    self.image3.setText("")
    self.image3.setPixmap(QtGui.QPixmap(self.clicked_img_path1))
    self.image3.setScaledContents(True)
    self.image3.setObjectName("image3")

    #
    self.image4 = QtWidgets.QLabel(self)
    self.image4.setGeometry(QtCore.QRect(380, 120, 150, 150))
    self.image4.setText("")
    self.image4.setPixmap(
        QtGui.QPixmap(
            "/Users/vishaljiodedra/OneDrive - Birmingham City University/Cloud Based Attendence System/Images/double_aerrow.png"
        ))
    self.image4.setScaledContents(True)
    self.image4.setObjectName("image4")

    #
    self.labl = QtWidgets.QLabel(self)
    self.labl.setGeometry(QtCore.QRect(280, 315, 500, 30))
    self.font = QtGui.QFont()
    self.font.setFamily("Futura")
    self.font.setPointSize(26)
    self.labl.setFont(self.font)
    self.labl.setObjectName("labl")
    self.labl.setText("Your Biometric Face Matched.")

    #
    self.labl1 = QtWidgets.QLabel(self)
    self.labl1.setGeometry(QtCore.QRect(270, 380, 500, 30))
    self.font = QtGui.QFont()
    self.font.setFamily("Futura")
    self.font.setPointSize(26)
    self.labl1.setFont(self.font)
    self.labl1.setObjectName("labl1")
    self.labl1.setText("Thank You for attending lecture.")

    #
    self.present_bt_labl = QtWidgets.QLabel(self)
    self.present_bt_labl.setGeometry(QtCore.QRect(490, 440, 400, 30))
    self.font = QtGui.QFont()
    self.font.setFamily("Futura")
    self.font.setPointSize(22)
    self.present_bt_labl.setFont(self.font)
    self.present_bt_labl.setObjectName("present_bt_labl")
    self.present_bt_labl.setText("you are marked as present.")
    #
    self.present_bt_labl.show()
    self.back_but.show()
    self.welcome_name.show()
    self.image2.show()
    self.image3.show()
    self.image4.show()
    self.labl.show()
    self.labl1.show()