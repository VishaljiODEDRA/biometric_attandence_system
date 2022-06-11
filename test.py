'''import face_recognition
import cv2


def abc():

    known_image = cv2.imread(
        "/Users/vishaljiodedra/OneDrive - Birmingham City University/Cloud Based Attendence System/Images/Student_biometric_face/Nikhil Gogna.png"
    )
    unknown_image = cv2.imread(
        "/Users/vishaljiodedra/OneDrive - Birmingham City University/Cloud Based Attendence System/Clicked Image/Nikhil Gogna.png"
    )

    results = face_recognition.compare_faces(
        [face_recognition.face_encodings(known_image)[0]],
        face_recognition.face_encodings(unknown_image)[0])
    return results


if abc() == True:
    print("Images detected")
else:
    print("Images not detected")'''

#Ask someone
'''a = [ 1, "a" , 2 , "b" , "test" , "exam"]
for a[-1] in a:
  print(a[-1])'''

#x = "/Users/vishaljiodedra/OneDrive - Birmingham City University/Cloud Based Attendence System/Images/Student_biometric_face/Nikhil Gogna.png"
#print(x.index('Nikhil Gogna'))
#print(x[120:-4])
'''import face_recognition
import cv2

known_image = cv2.imread("Nikhil Gogna.png")
unknown_image = cv2.imread(
    "/Users/vishaljiodedra/OneDrive - Birmingham City University/Cloud Based Attendence System/Clicked Image/Elon Musk.png"
)

biden_encoding = face_recognition.face_encodings(known_image)[0]
unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

results = face_recognition.compare_faces([biden_encoding], unknown_encoding)
if results[0] == True:
    print("Face matched")
else:
    print("Face not matched")'''
'''import pandas as pd
from datetime import datetime

x = pd.read_csv(
    "/Users/vishaljiodedra/OneDrive - Birmingham City University/Cloud Based Attendence System/Room_CZ199.csv"
)
df = pd.read_csv(
    "/Users/vishaljiodedra/OneDrive - Birmingham City University/Cloud Based Attendence System/Student Attendence Report/Nikhil Gogna.csv"
)

current_date = datetime.now().strftime("%B %d, %Y")
current_time = datetime.now().strftime("%H:%M")
col = []
for name, values in x.iteritems():
    for index, i in df.iterrows():
        for value in values:
            if str(current_date) == str(
                    i['date']) and str(current_date) == str(name):
                x = str(value)
                start_time = x[0:5]
                end_time = x[9:14]
                if start_time < current_time < end_time:
                    for n, vs in df.iteritems():
                        col.append(n)
                        if n == "Computer Systems":
                            print(col.index(n))
                            df.iloc[index, col.index(n)] = 1
                            df.to_csv(
                                "/Users/vishaljiodedra/OneDrive - Birmingham City University/Cloud Based Attendence System/Student Attendence Report/Nikhil Gogna.csv",
                                index=False)'''

a = '09:00 to 11:00#Computer Science#Data Structure & Algorithms'
x = a.split('#')
print(x[0][0:5], x[0][9:14], x[2])
