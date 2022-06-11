import cv2
import numpy as np


def Biometric_face():
    #open camera for video capture
    cap = cv2.VideoCapture(0)

    #haarascade classifier file
    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")

    #dataset file location
    skip = 0
    #storing face data and label in a list
    face_data = []
    dataset_path = "/Users/vishaljiodedra/OneDrive - Birmingham City University/Cloud Based Attendence System/dataset_path/"

    file_name = "vishal"

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

            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 3)
        cv2.imshow("faces", frame)

        key_pressed = cv2.waitKey(1) & 0xFF

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    face_data = np.array(face_data)
    face_data = face_data.reshape((face_data.shape[0], -1))

    np.save(dataset_path + file_name, face_data)
    print(f'Dataset saved at {dataset_path+file_name}.npy')

    cap.release()
    cv2.destroyAllWindows()


#Biometric_face()