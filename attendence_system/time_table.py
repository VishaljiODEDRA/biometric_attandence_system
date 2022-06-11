from cmath import nan
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from datetime import datetime
import pandas as pd


def time_table(self):
    self.time_table_back_button = QtWidgets.QPushButton(self)
    self.time_table_back_button.setGeometry(QtCore.QRect(40, 40, 101, 51))
    self.time_table_back_button.setStyleSheet(
        "QPushButton{\n"
        "    font: 500 48pt \"Futura\";\n"
        "    background-color: rgb(193, 193, 193);\n"
        "    border-radius: 15px;\n"
        "}\n"
        "QPushButton:pressed{\n"
        "    background-color: rgb(255, 255, 255);\n"
        "}\n"
        "")
    self.time_table_back_button.setObjectName("time_table_back_button")
    self.time_table_back_button.setText("←")
    self.time_table_back_button.clicked.connect(self.time_table_go_back)
    self.time_table_back_button.show()
    #
    self.prev_button = QtWidgets.QPushButton(self)
    self.prev_button.setGeometry(QtCore.QRect(150, 40, 130, 50))
    self.prev_button.setStyleSheet(
        "QPushButton{\n"
        "    font: 500 25pt \"Futura\";\n"
        "    background-color: rgb(193, 193, 193);\n"
        "    border-radius: 15px;\n"
        "}\n"
        "QPushButton:pressed{\n"
        "    background-color: rgb(255, 255, 255);\n"
        "}\n"
        "")
    self.prev_button.setObjectName("prev_button")
    self.prev_button.setText("Previ.")
    self.prev_button.clicked.connect(self.previous_date)
    self.prev_button.show()
    #
    self.next_button = QtWidgets.QPushButton(self)
    self.next_button.setGeometry(QtCore.QRect(650, 40, 130, 50))
    self.next_button.setStyleSheet(
        "QPushButton{\n"
        "    font: 500 25pt \"Futura\";\n"
        "    background-color: rgb(193, 193, 193);\n"
        "    border-radius: 15px;\n"
        "}\n"
        "QPushButton:pressed{\n"
        "    background-color: rgb(255, 255, 255);\n"
        "}\n"
        "")
    self.next_button.setObjectName("next_button")
    self.next_button.setText("Next")
    self.next_button.clicked.connect(self.tomorrow_date)
    self.next_button.show()
    #
    self.today_date = datetime.now()
    self.present_bt_labl = QtWidgets.QLabel(self)
    self.present_bt_labl.setGeometry(QtCore.QRect(370, 45, 250, 40))
    self.font = QtGui.QFont()
    self.font.setFamily("Futura")
    self.font.setPointSize(26)
    self.present_bt_labl.setFont(self.font)
    self.present_bt_labl.setObjectName("present_bt_labl")
    self.present_bt_labl.setText(self.today_date.strftime("%B %d, %Y"))
    self.present_bt_labl.show()
    #
    self.lec_time_labels = []
    j = 40
    for name, values in self.time_table_data.iteritems():
        if str(name) == self.present_bt_labl.text():
            for value in values:
                if value == nan:
                    break
                else:
                    time = value.split("#")
                    self.lec_time_label = QtWidgets.QLabel(self)
                    self.lec_time_label.setGeometry(
                        QtCore.QRect(150, 100 + j, 700, 40))
                    self.font = QtGui.QFont()
                    self.font.setFamily("Futura")
                    self.font.setPointSize(22)
                    self.lec_time_label.setFont(self.font)
                    self.lec_time_label.setObjectName("lec_time_label")
                    self.lec_time_label.setText(
                        str(time[0] + " - " + time[1] + " - " + time[2]))
                    self.lec_time_labels.append(self.lec_time_label)
                    self.lec_time_label.show()
                    j += 40
            break
