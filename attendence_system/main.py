from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sys
import pandas as pd
from user_page import user_page2, value_course_page
from course_page import course_page1, value_module_page
from module_page import module_page1
from log_in import login_page
from time_table import time_table
from biometric_preset_mark_page import biometric_present
from home import initUI
from open_cam2_with_knn import knn
import cv2
import numpy as np
import os
import face_recognition
from datetime import datetime, timedelta


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.resize(850, 600)
        self.setMinimumSize(QtCore.QSize(850, 600))
        self.setMaximumSize(QtCore.QSize(850, 600))
        self.setWindowTitle("Biometric Attendence System")
        self.time_table_data = pd.read_csv(
            "/Users/vishaljiodedra/OneDrive - Birmingham City University/Cloud Based Attendence System/Room_CZ199.csv"
        )
        self.df = pd.read_csv(
            "/Users/vishaljiodedra/OneDrive - Birmingham City University/Cloud Based Attendence System/student_info.csv"
        )
        self.df2 = pd.read_csv(
            "/Users/vishaljiodedra/OneDrive - Birmingham City University/Cloud Based Attendence System/course_info.csv"
        )
        initUI(self)

    def user_page1(self):
        for self.index, i in self.df.iterrows():
            if self.username_input.text() == str(
                    i['username']) and self.password_input.text() == str(
                        i['password']):
                self.name = i['name']
                self.clicked_img_path = "/Users/vishaljiodedra/OneDrive - Birmingham City University/Cloud Based Attendence System/Images/Student_biometric_face/" + self.name + ".png"
                self.email = i['email']
                self.stu_course = i['stu_course']
                self.back_button.deleteLater()
                self.msg_label1.deleteLater()
                self.username_input.deleteLater()
                self.password_input.deleteLater()
                self.username_label.deleteLater()
                self.password_label.deleteLater()
                self.login_button.deleteLater()
                user_page2(self)
                break
        else:
            self.msg = QMessageBox()
            self.msg.setWindowTitle("Nottice!")
            self.msg.setText("The Username or Password is incorrect!")
            self.msg.setIcon(QMessageBox.Critical)
            self.msg.show()

    def present_button_pressed(self):
        current_date = datetime.now().strftime("%B %d, %Y")
        current_time = datetime.now().strftime("%H:%M")
        col = []
        for name, values in self.time_table_data.iteritems():
            for index, i in self.student_att_info.iterrows():
                for value in values:
                    if str(current_date) == str(
                            i['date']) and str(current_date) == str(name):
                        x = value.split('#')
                        start_time = x[0][0:5]
                        end_time = x[0][9:14]
                        if start_time < current_time < end_time and x[
                                2] == self.module_label_on_page.text():
                            for n, vs in self.student_att_info.iteritems():
                                col.append(n)
                                if n == self.module_label_on_page.text():
                                    self.student_att_info.iloc[
                                        index, col.index(n)] = 1
                                    self.module_present_button.setHidden(True)
                                    self.present_button_label.show()
                                    self.student_att_info.to_csv(
                                        "/Users/vishaljiodedra/OneDrive - Birmingham City University/Cloud Based Attendence System/Student Attendence Report/Nikhil Gogna.csv",
                                        index=False)
                        elif current_time > end_time and x[
                                2] == self.module_label_on_page.text():
                            for n, vs in self.student_att_info.iteritems():
                                col.append(n)
                                if n == self.module_label_on_page.text():
                                    self.student_att_info.iloc[
                                        index, col.index(n)] = 0
                                    self.msg = QMessageBox()
                                    self.msg.setWindowTitle("Nottice!")
                                    self.msg.setText(
                                        "You missed last lecture.")
                                    self.msg.setIcon(QMessageBox.Critical)
                                    self.msg.show()
                        else:
                            self.msg = QMessageBox()
                            self.msg.setWindowTitle("Nottice!")
                            self.msg.setText(
                                "You do not have any lecture in this class at the moment."
                            )
                            self.msg.setIcon(QMessageBox.Critical)
                            self.msg.show()

    def present_button_pressed1(self):
        student_att_info = pd.read_csv(
            "/Users/vishaljiodedra/OneDrive - Birmingham City University/Cloud Based Attendence System/Student Attendence Report/"
            + self.names[int(self.out)] + ".csv")
        course_info = pd.read_csv(
            "/Users/vishaljiodedra/OneDrive - Birmingham City University/Cloud Based Attendence System/course_info.csv"
        )
        current_date = datetime.now().strftime("%B %d, %Y")
        current_time = datetime.now().strftime("%H:%M")
        col = []
        for name, values in self.time_table_data.iteritems():
            for index, i in student_att_info.iterrows():
                for value in values:
                    if str(current_date) == str(
                            i['date']) and str(current_date) == str(name):
                        x = value.split('#')
                        start_time = x[0][0:5]
                        end_time = x[0][9:14]
                        if start_time < current_time < end_time:
                            for n, vs in student_att_info.iteritems():
                                col.append(n)
                                for a, bs in course_info.iteritems():
                                    for b in bs:
                                        if n == b and x[2] == b:
                                            student_att_info.iloc[
                                                index, col.index(n)] = 1
                                            biometric_present(self)
                                            student_att_info.to_csv(
                                                "/Users/vishaljiodedra/OneDrive - Birmingham City University/Cloud Based Attendence System/Student Attendence Report/Nikhil Gogna.csv",
                                                index=False)
                                            break
                        elif current_time > end_time:
                            for n, vs in student_att_info.iteritems():
                                col.append(n)
                                for a, bs in course_info.iteritems():
                                    for b in bs:
                                        if n == b and x[2] == b:
                                            student_att_info.iloc[
                                                index, col.index(n)] = 0
                                            initUI(self)
                                            self.msg = QMessageBox()
                                            self.msg.setWindowTitle("Nottice!")
                                            self.msg.setText(
                                                "You missed last lecture.")
                                            self.msg.setIcon(
                                                QMessageBox.Critical)
                                            self.msg.show()
                        else:
                            initUI(self)
                            self.msg = QMessageBox()
                            self.msg.setWindowTitle("Nottice!")
                            self.msg.setText(
                                "You do not have any lecture in this class at the moment."
                            )
                            self.msg.setIcon(QMessageBox.Critical)
                            self.msg.show()

    def attendence_report(self):
        value_module_page(self)
        for i in self.module_buttons:
            i.deleteLater()
        self.module_label.deleteLater()
        self.course_label_on_page.deleteLater()
        self.back_button2.deleteLater()
        module_page1(self)

    def login_setup_ui(self):
        self.msg_label.deleteLater()
        self.mark_manu.setHidden(True)
        self.start_cam.setHidden(True)
        self.time_table.deleteLater()
        self.image.deleteLater()
        login_page(self)

    def course_page(self):
        value_course_page(self)
        self.back_button1.deleteLater()
        self.biometric_face.deleteLater()
        self.atten_percentage.deleteLater()
        self.atte_label.deleteLater()
        self.course_label.deleteLater()
        for i in self.course_buttons:
            i.deleteLater()
        self.name_label.setHidden(True)
        self.email_label.deleteLater()
        self.image1.deleteLater()
        course_page1(self)

    def go_back_to_login(self):
        self.name_label.deleteLater()
        self.email_label.deleteLater()
        self.back_button1.deleteLater()
        self.course_label.deleteLater()
        self.atte_label.deleteLater()
        self.image1.deleteLater()
        for i in self.course_buttons:
            i.deleteLater()
        self.atten_percentage.deleteLater()
        self.biometric_face.deleteLater()
        login_page(self)

    def go_back_to_user_page(self):
        self.back_button2.deleteLater()
        self.course_label_on_page.deleteLater()
        self.module_label.deleteLater()
        for i in self.module_buttons:
            i.setHidden(True)
        user_page2(self)

    def go_back_course_page(self):
        self.back_button3.deleteLater()
        self.module_label_on_page.deleteLater()
        self.atten_report_label.deleteLater()
        self.chart.deleteLater()
        self.slice.deleteLater()
        self.series.deleteLater()
        self.present_button_label.setHidden(True)
        self.module_present_button.setHidden(True)
        course_page1(self)

    def go_back_to_home1(self):
        self.back_but.deleteLater()
        self.welcome_name.deleteLater()
        self.image2.deleteLater()
        self.image3.deleteLater()
        self.image4.deleteLater()
        self.labl.deleteLater()
        self.labl1.deleteLater()
        self.present_bt_labl.deleteLater()
        initUI(self)

    def go_back_to_home(self):
        self.back_button.deleteLater()
        self.msg_label1.deleteLater()
        self.password_input.deleteLater()
        self.username_input.deleteLater()
        self.login_button.deleteLater()
        self.password_label.deleteLater()
        self.username_label.deleteLater()
        initUI(self)

    def time_table1(self):
        self.msg_label.deleteLater()
        self.mark_manu.setHidden(True)
        self.start_cam.setHidden(True)
        self.time_table.deleteLater()
        self.image.deleteLater()
        time_table(self)

    def time_table_go_back(self):
        self.time_table_back_button.deleteLater()
        self.prev_button.deleteLater()
        self.next_button.deleteLater()
        self.present_bt_labl.deleteLater()
        for i in self.lec_time_labels:
            i.deleteLater()
        initUI(self)

    def Biometric_face1(self):
        #open camera for video capture
        cap = cv2.VideoCapture(0)

        #haarascade classifier file
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +
                                             "haarcascade_frontalface_alt.xml")

        #dataset file location
        skip = 0
        #storing face data and label in a list
        face_data = []
        dataset_path = "/Users/vishaljiodedra/OneDrive - Birmingham City University/Cloud Based Attendence System/dataset_path/"

        file_name = self.name

        while True:
            ret, frame = cap.read()

            #conveting image into grayscale or black&white
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            if ret == False:
                continue

            #detecting multiple faces into the image or frame
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)
            if len(faces) == 0:
                continue

            k = 1
            faces = sorted(faces, key=lambda x: x[2] * x[3], reverse=True)
            skip += 1

            for face in faces[:1]:
                x, y, w, h = face

                offset = 5
                face_offset = frame[y - offset:y + h + offset,
                                    x - offset:x + w + offset]
                face_selection = cv2.resize(face_offset, (100, 100))
                if skip % 10 == 0:
                    face_data.append(face_selection)

                cv2.imshow(str(k), face_selection)
                k += 1

                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 3)
            cv2.putText(
                frame,
                "Stand still infront of camera and after 3 second press 'q' to capture.",
                (80, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 3)
            cv2.imshow("faces", frame)

            if cv2.waitKey(20) & 0xFF == ord('q'):
                cv2.imwrite(self.clicked_img_path, face_offset)
                self.msg1 = QMessageBox()
                self.msg1.setWindowTitle("Nottice!")
                self.msg1.setText(
                    "Your BIOMETRIC FACE is updated, Please relog-in!")
                self.msg1.buttonClicked.connect(self.go_back_to_login)
                self.msg1.show()
                break

        face_data = np.array(face_data)
        face_data = face_data.reshape((face_data.shape[0], -1))

        np.save(dataset_path + file_name, face_data)

        cap.release()
        cv2.destroyAllWindows()

    def face_detection(self):
        self.df = pd.read_csv(
            "/Users/vishaljiodedra/OneDrive - Birmingham City University/Cloud Based Attendence System/student_info.csv"
        )
        #open camera for video capture
        cap = cv2.VideoCapture(0)

        #haarascade classifier file
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +
                                             "haarcascade_frontalface_alt.xml")

        #dataset file location
        dataset_path = "/Users/vishaljiodedra/OneDrive - Birmingham City University/Cloud Based Attendence System/dataset_path/"

        #storing face data and label in a list
        face_data = []
        labels = []
        class_id = 0  #giving labels for every given file
        self.names = {}  #map between id and name

        #preparing the dataset
        for fx in os.listdir(dataset_path):
            if fx.endswith('.npy'):
                self.names[class_id] = fx[:-4]
                data_item = np.load(dataset_path + fx)
                face_data.append(data_item)

                target = class_id * np.ones((data_item.shape[0], ))
                class_id += 1
                labels.append(target)

        face_dataset = np.concatenate(face_data, axis=0)
        face_labels = np.concatenate(labels, axis=0).reshape((-1, 1))

        trainset = np.concatenate((face_dataset, face_labels), axis=1)

        while True:
            ret, frame = cap.read()

            #conveting image into grayscale or black&white
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            if ret == False:
                continue

            #detecting multiple faces into the image or frame
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)

            for face in faces:
                x, y, w, h = face

                #getting the ROI of the image
                offset = 5
                face_section = frame[y - offset:y + h + offset,
                                     x - offset:x + w + offset]
                face_sec = cv2.resize(face_section, (100, 100))

                #calling the knn algorithm
                self.out = knn(trainset, face_sec.flatten())

                #drawing the rectangle in the original image
                cv2.putText(frame, self.names[int(self.out)], (x, y - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2,
                            cv2.LINE_AA)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

                self.clicked_img_path1 = "/Users/vishaljiodedra/OneDrive - Birmingham City University/Cloud Based Attendence System/Clicked Image/" + self.names[
                    int(self.out)] + ".png"
                cv2.imwrite(self.clicked_img_path1, face_section)

            cv2.putText(frame, "If your face is detected, please Press 'q'.",
                        (300, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 3)

            cv2.imshow("Faces", frame)
            if cv2.waitKey(20) & 0xFF == ord('q'):
                for index, i in self.df.iterrows():
                    if self.names[int(self.out)] == str(i['name']):
                        self.biometric_face = "/Users/vishaljiodedra/OneDrive - Birmingham City University/Cloud Based Attendence System/Images/Student_biometric_face/" + str(
                            i['name']) + ".png"
                        known_image = cv2.imread(self.biometric_face)
                        unknown_image = cv2.imread(self.clicked_img_path1)

                        biden_encoding = face_recognition.face_encodings(
                            known_image)[0]
                        unknown_encoding = face_recognition.face_encodings(
                            unknown_image)[0]

                        self.results = face_recognition.compare_faces(
                            [biden_encoding], unknown_encoding)
                        if self.results[0] == True:
                            self.welcome_msg = "Welcome, " + self.names[int(
                                self.out)]
                            self.display_name = str(i['name'])
                            self.msg_label.deleteLater()
                            self.mark_manu.setHidden(True)
                            self.start_cam.setHidden(True)
                            self.time_table.deleteLater()
                            self.image.deleteLater()
                            self.present_button_pressed1()
                        else:
                            self.msg1 = QMessageBox()
                            self.msg1.setWindowTitle("Nottice!")
                            self.msg1.setText(
                                "Your BIOMETRIC FACE didn't match out data, to upadate Please log-in!"
                            )
                            self.msg1.buttonClicked.connect(
                                self.login_setup_ui)
                            self.msg1.show()
                break

        cap.release()
        cv2.destroyAllWindows()

    def tomorrow_date(self):
        self.today_date = self.today_date + timedelta(1)
        self.present_bt_labl.setText(self.today_date.strftime("%B %d, %Y"))
        df = pd.read_csv(
            "/Users/vishaljiodedra/OneDrive - Birmingham City University/Cloud Based Attendence System/Room_CZ199.csv"
        )
        j = 40
        for name, values in df.iteritems():
            if str(name) == self.present_bt_labl.text():
                k = 0
                for value in values:
                    time = value.split("#")
                    self.lec_time_labels[k].show()
                    self.lec_time_labels[k].setText(
                        str(time[0] + " - " + time[1] + " - " + time[2]))
                    k += 1
                    j += 40

    def previous_date(self):
        self.today_date = self.today_date - timedelta(1)
        self.present_bt_labl.setText(self.today_date.strftime("%B %d, %Y"))
        df = pd.read_csv(
            "/Users/vishaljiodedra/OneDrive - Birmingham City University/Cloud Based Attendence System/Room_CZ199.csv"
        )
        j = 40
        for name, values in df.iteritems():
            if str(name) == self.present_bt_labl.text():
                k = 0
                for value in values:
                    time = value.split("#")
                    self.lec_time_labels[k].show()
                    self.lec_time_labels[k].setText(
                        str(time[0] + " - " + time[1] + " - " + time[2]))
                    k += 1
                    j += 40


def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())


window()
