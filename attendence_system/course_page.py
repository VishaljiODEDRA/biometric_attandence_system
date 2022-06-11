from PyQt5 import QtCore, QtGui, QtWidgets


def course_page1(self):
    self.back_button2 = QtWidgets.QPushButton(self)
    self.back_button2.setGeometry(QtCore.QRect(40, 40, 101, 51))
    self.back_button2.setStyleSheet(
        "QPushButton{\n"
        "    font: 500 48pt \"Futura\";\n"
        "    background-color: rgb(193, 193, 193);\n"
        "    border-radius: 15px;\n"
        "}\n"
        "QPushButton:pressed{\n"
        "    background-color: rgb(255, 255, 255);\n"
        "}\n"
        "")
    self.back_button2.setObjectName("back_button2")
    self.back_button2.setText("←")
    self.back_button2.show()
    self.back_button2.clicked.connect(self.go_back_to_user_page)
    #
    self.module_label = QtWidgets.QLabel(self)
    self.module_label.setGeometry(QtCore.QRect(170, 100, 100, 50))
    self.font = QtGui.QFont()
    self.font.setFamily("Futura")
    self.font.setPointSize(24)
    self.module_label.setFont(self.font)
    self.module_label.setObjectName("module_label")
    self.module_label.setText("Modules:")
    self.module_label.show()
    #

    self.course_label_on_page = QtWidgets.QLabel(self)
    self.course_label_on_page.setGeometry(QtCore.QRect(150, 40, 400, 50))
    self.font = QtGui.QFont()
    self.font.setFamily("Futura")
    self.font.setPointSize(32)
    self.course_label_on_page.setFont(self.font)
    self.course_label_on_page.setObjectName("course_label_on_page")
    self.course_label_on_page.setText(self.course_title_on_page)
    self.course_label_on_page.show()
    #
    a = 50
    self.module_buttons = []
    for name, values in self.df2.iteritems():
        if str(name) == self.course_title_on_page:
            for value in values:
                self.module_button = QtWidgets.QPushButton(self)
                self.module_button.setGeometry(
                    QtCore.QRect(280, 60 + a, 450, 30))
                self.module_button.setStyleSheet(
                    "QPushButton{\n"
                    "    font: 500 20pt \"Futura\";\n"
                    "    background-color: rgb(193, 193, 193);\n"
                    "    border-radius: 10px;\n"
                    "}\n"
                    "QPushButton:pressed{\n"
                    "    background-color: rgb(255, 255, 255);\n"
                    "}\n"
                    "")
                self.module_button.setObjectName("web_design_button")
                self.module_button.setText(value)
                self.module_button.setCheckable(True)
                self.module_button.clicked.connect(self.attendence_report)
                self.module_button.show()
                self.module_buttons.append(self.module_button)
                a += 50


def value_module_page(self):
    for b in self.module_buttons:
        if b.isChecked() == True:
            for name, values in self.df2.iteritems():
                if str(name) == self.course_title_on_page:
                    for value in values:
                        if str(value) == b.text():
                            self.module_title_on_page = str(value)
