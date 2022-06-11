from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtChart import QChart, QChartView, QPieSeries, QPieSlice
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt
import pandas as pd
from datetime import datetime


def module_page1(self):
    self.student_att_info = pd.read_csv(
        "/Users/vishaljiodedra/OneDrive - Birmingham City University/Cloud Based Attendence System/Student Attendence Report/"
        + self.name + ".csv")
    #
    self.series = QPieSeries()
    pr_count = 0
    ab_count = 0
    print(self.module_title_on_page)
    for name, values in self.student_att_info.iteritems():
        if name == self.module_title_on_page:
            for value in values:
                for value in values:
                    if value == 1:
                        pr_count += 1
                    elif value == 0:
                        ab_count += 1

    #adding slice
    self.series.append("Present", pr_count - 1)
    self.series.append("Absent", ab_count - 1)
    self.slice = QPieSlice()
    self.slice = self.series.slices()[0]
    self.slice.setExploded(True)
    self.slice.setLabelVisible(True)
    self.slice.setPen(QPen(Qt.darkGreen, 2))
    self.slice.setBrush(Qt.green)

    self.chart = QChart()
    self.chart.legend().hide()
    self.chart.addSeries(self.series)
    self.chart.createDefaultAxes()
    self.chart.setAnimationOptions(QChart.SeriesAnimations)

    self.chart.legend().setVisible(True)
    self.chart.legend().setAlignment(Qt.AlignBottom)

    chartview = QChartView(self.chart)
    chartview.setRenderHint(QPainter.Antialiasing)

    self.setCentralWidget(chartview)
    #
    self.back_button3 = QtWidgets.QPushButton(self)
    self.back_button3.setGeometry(QtCore.QRect(40, 40, 101, 51))
    self.back_button3.setStyleSheet(
        "QPushButton{\n"
        "    font: 500 48pt \"Futura\";\n"
        "    background-color: rgb(193, 193, 193);\n"
        "    border-radius: 15px;\n"
        "}\n"
        "QPushButton:pressed{\n"
        "    background-color: rgb(255, 255, 255);\n"
        "}\n"
        "")
    self.back_button3.setObjectName("back_button3")
    self.back_button3.setText("←")
    self.back_button3.show()
    self.back_button3.clicked.connect(self.go_back_course_page)
    #
    self.module_label_on_page = QtWidgets.QLabel(self)
    self.module_label_on_page.setGeometry(QtCore.QRect(150, 40, 650, 50))
    self.font = QtGui.QFont()
    self.font.setFamily("Futura")
    self.font.setPointSize(30)
    self.module_label_on_page.setFont(self.font)
    self.module_label_on_page.setObjectName("module_label_on_page")
    self.module_label_on_page.setText(self.module_title_on_page)
    self.module_label_on_page.show()
    #
    self.atten_report_label = QtWidgets.QLabel(self)
    self.atten_report_label.setGeometry(QtCore.QRect(170, 80, 300, 50))
    self.font = QtGui.QFont()
    self.font.setFamily("Futura")
    self.font.setPointSize(24)
    self.atten_report_label.setFont(self.font)
    self.atten_report_label.setObjectName("atten_report_label")
    self.atten_report_label.setText("Attendence Report:")
    self.atten_report_label.show()
    #
    self.module_present_button = QtWidgets.QPushButton(self)
    self.module_present_button.setGeometry(QtCore.QRect(600, 500, 200, 30))
    self.module_present_button.setStyleSheet(
        "QPushButton{\n"
        "    font: 500 20pt \"Futura\";\n"
        "    background-color: rgb(193, 193, 193);\n"
        "    border-radius: 10px;\n"
        "}\n"
        "QPushButton:pressed{\n"
        "    background-color: rgb(255, 255, 255);\n"
        "}\n"
        "")
    self.module_present_button.setObjectName("module_present_button")
    self.module_present_button.setText("Mark Present")
    self.module_present_button.setCheckable(True)
    self.module_present_button.show()
    self.module_present_button.clicked.connect(self.present_button_pressed)
    #
    self.present_button_label = QtWidgets.QLabel(self)
    self.present_button_label.setGeometry(QtCore.QRect(200, 500, 400, 30))
    self.font = QtGui.QFont()
    self.font.setFamily("Futura")
    self.font.setPointSize(22)
    self.present_button_label.setFont(self.font)
    self.present_button_label.setObjectName("present_button_label")
    self.present_button_label.setText("you are marked as present.")
