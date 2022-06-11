from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *


def login_page(self):
    #creatinf new widgets for the log in page
    self.msg_label1 = QtWidgets.QLabel(self)
    self.msg_label1.setGeometry(QtCore.QRect(350, 40, 711, 51))
    self.font = QtGui.QFont()
    self.font.setFamily("Futura")
    self.font.setPointSize(36)
    self.msg_label1.setFont(self.font)
    self.msg_label1.setObjectName("msg_label1")
    self.msg_label1.setText("Welcome!")
    self.msg_label1.show()
    #
    self.back_button = QtWidgets.QPushButton(self)
    self.back_button.setGeometry(QtCore.QRect(40, 40, 101, 51))
    self.back_button.setStyleSheet(
        "QPushButton{\n"
        "    font: 500 48pt \"Futura\";\n"
        "    background-color: rgb(193, 193, 193);\n"
        "    border-radius: 15px;\n"
        "}\n"
        "QPushButton:pressed{\n"
        "    background-color: rgb(255, 255, 255);\n"
        "}\n"
        "")
    self.back_button.show()
    self.back_button.setObjectName("back_button")
    self.back_button.setText("←")
    self.back_button.clicked.connect(self.go_back_to_home)
    #
    self.username_label = QtWidgets.QLabel(self)
    self.username_label.setGeometry(QtCore.QRect(210, 236, 141, 41))
    font = QtGui.QFont()
    font.setFamily("Futura")
    font.setPointSize(24)
    self.username_label.setFont(font)
    self.username_label.setObjectName("username_label")
    self.username_label.setText("Username  :")
    self.username_label.show()
    #
    self.password_label = QtWidgets.QLabel(self)
    self.password_label.setGeometry(QtCore.QRect(215, 335, 131, 41))
    font = QtGui.QFont()
    font.setFamily("Futura")
    font.setPointSize(24)
    self.password_label.setFont(font)
    self.password_label.setObjectName("password_label")
    self.password_label.setText("Password  :")
    self.password_label.show()
    #
    self.login_button = QtWidgets.QPushButton(self)
    self.login_button.setGeometry(QtCore.QRect(510, 460, 211, 71))
    self.login_button.setStyleSheet(
        "QPushButton{\n"
        "    font: 500 36pt \"Futura\";\n"
        "    background-color: rgb(193, 193, 193);\n"
        "    border-radius: 15px;\n"
        "}\n"
        "QPushButton:pressed{\n"
        "    background-color: rgb(255, 255, 255);\n"
        "}")
    self.login_button.setObjectName("login_button")
    self.login_button.setText("Log in")
    self.login_button.show()
    self.login_button.clicked.connect(self.user_page1)
    #
    self.username_input = QtWidgets.QLineEdit(self)
    self.username_input.setGeometry(QtCore.QRect(370, 230, 250, 40))
    self.username_input.setStyleSheet("font: 500 18pt \"Futura\";\n"
                                      "background-color: rgb(193, 193, 193);\n"
                                      "border-radius: 5px;")
    self.username_input.setObjectName("username_input")
    self.username_input.show()
    #
    self.password_input = QtWidgets.QLineEdit(self)
    self.password_input.setGeometry(QtCore.QRect(370, 330, 250, 40))
    self.password_input.setStyleSheet("font: 500 18pt \"Futura\";\n"
                                      "background-color: rgb(193, 193, 193);\n"
                                      "border-radius: 5px;")
    self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)
    self.password_input.setObjectName("password_input")
    self.password_input.show()
