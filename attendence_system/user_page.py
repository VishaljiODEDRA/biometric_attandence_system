from cmath import nan
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import pandas as pd
from datetime import datetime


def user_page2(self):
    self.student_att_info = pd.read_csv(
        "/Users/vishaljiodedra/OneDrive - Birmingham City University/Cloud Based Attendence System/Student Attendence Report/"
        + self.name + ".csv")
    self.back_button1 = QtWidgets.QPushButton(self)
    self.back_button1.setGeometry(QtCore.QRect(40, 40, 101, 51))
    self.back_button1.setStyleSheet(
        "QPushButton{\n"
        "    font: 500 48pt \"Futura\";\n"
        "    background-color: rgb(193, 193, 193);\n"
        "    border-radius: 15px;\n"
        "}\n"
        "QPushButton:pressed{\n"
        "    background-color: rgb(255, 255, 255);\n"
        "}\n"
        "")
    self.back_button1.setObjectName("back_button1")
    self.back_button1.setText("←")
    self.back_button1.clicked.connect(self.go_back_to_login)
    self.back_button1.show()
    #
    self.image1 = QtWidgets.QLabel(self)
    self.image1.setGeometry(QtCore.QRect(180, 40, 150, 150))
    self.image1.setText("")
    self.image1.setPixmap(QtGui.QPixmap(self.clicked_img_path))
    self.image1.setScaledContents(True)
    self.image1.setObjectName("image1")
    self.image1.show()
    #
    self.name_label = QtWidgets.QLabel(self)
    self.name_label.setGeometry(QtCore.QRect(360, 40, 711, 51))
    self.font = QtGui.QFont()
    self.font.setFamily("Futura")
    self.font.setPointSize(34)
    self.name_label.setFont(self.font)
    self.name_label.setObjectName("name_label")
    self.name_label.setText(self.name)
    self.name_label.show()
    #
    self.email_label = QtWidgets.QLabel(self)
    self.email_label.setGeometry(QtCore.QRect(360, 75, 711, 51))
    self.font = QtGui.QFont()
    self.font.setFamily("Futura")
    self.font.setPointSize(16)
    self.email_label.setFont(self.font)
    self.email_label.setObjectName("email_label")
    self.email_label.setText(self.email)
    self.email_label.show()
    #
    self.course_label = QtWidgets.QLabel(self)
    self.course_label.setGeometry(QtCore.QRect(180, 225, 711, 51))
    self.font = QtGui.QFont()
    self.font.setFamily("Futura")
    self.font.setPointSize(28)
    self.course_label.setFont(self.font)
    self.course_label.setObjectName("course_label")
    self.course_label.setText("Course  :")
    self.course_label.show()
    #
    self.biometric_face = QtWidgets.QPushButton(self)
    self.biometric_face.setGeometry(QtCore.QRect(360, 125, 200, 50))
    self.biometric_face.setStyleSheet(
        "QPushButton{\n"
        "    font: 500 22pt \"Futura\";\n"
        "    background-color: rgb(193, 193, 193);\n"
        "    border-radius: 15px;\n"
        "}\n"
        "QPushButton:pressed{\n"
        "    background-color: rgb(255, 255, 255);\n"
        "}")
    self.biometric_face.setObjectName("biometric_face")
    self.biometric_face.setText("Biometric Face")
    self.biometric_face.show()
    self.biometric_face.clicked.connect(self.Biometric_face1)
    #
    a = 70
    self.student_course = self.stu_course.split("#")
    self.course_buttons = []
    for self.course in self.student_course:
        self.course_button = QtWidgets.QPushButton(self)
        self.course_button.setGeometry(QtCore.QRect(325, 155 + a, 400, 50))
        self.course_button.setStyleSheet(
            "QPushButton{\n"
            "    font: 500 28pt \"Futura\";\n"
            "    background-color: rgb(193, 193, 193);\n"
            "    border-radius: 15px;\n"
            "}\n"
            "QPushButton:pressed{\n"
            "    background-color: rgb(255, 255, 255);\n"
            "}")
        self.course_button.setObjectName("course_button")
        self.course_button.setText(self.course)
        self.course_button.setCheckable(True)
        self.course_button.clicked.connect(self.course_page)
        self.course_button.show()
        self.course_buttons.append(self.course_button)
        a += 70

    #
    self.atte_label = QtWidgets.QLabel(self)
    self.atte_label.setGeometry(QtCore.QRect(180, 150 + a, 711, 51))
    self.font = QtGui.QFont()
    self.font.setFamily("Futura")
    self.font.setPointSize(28)
    self.atte_label.setFont(self.font)
    self.atte_label.setObjectName("atte_label")
    self.atte_label.setText("Attendence  :")
    self.atte_label.show()
    #
    pr_count = 0
    total = 0
    for name, values in self.student_att_info.iteritems():
        for value in values:
            if value == 1:
                pr_count += 1
                total += 1
            elif value == 0:
                total += 1
    x = ((pr_count - 1) * 100) / (total - 2)
    y = str("%.2f" % round(x, 2)) + " %"
    self.atten_percentage = QtWidgets.QLabel(self)
    self.atten_percentage.setGeometry(QtCore.QRect(380, 150 + a, 150, 50))
    self.font = QtGui.QFont()
    self.font.setFamily("Futura")
    self.font.setPointSize(28)
    self.atten_percentage.setFont(self.font)
    self.atten_percentage.setObjectName("atten_percentage")
    self.atten_percentage.setText(y)
    self.atten_percentage.show()


def value_course_page(self):
    for b in self.course_buttons:
        for j in self.student_course:
            if b.isChecked() == True and b.text() == j:
                self.course_title_on_page = j
