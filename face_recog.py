import cv2
import face_recognition
import os

# Load all known faces from 'known_faces' folder
known_faces = []
known_names = []

for file in os.listdir("FaceRecognisation/known_faces"):
    img_path = f"FaceRecognisation/known_faces/{file}"
    img = face_recognition.load_image_file(img_path)
    encodings = face_recognition.face_encodings(img)

    if len(encodings) == 0:
        print(f"⚠️ No face found in {file}")
        continue

    encoding = encodings[0]
    known_faces.append(encoding)
    known_names.append(os.path.splitext(file)[0])  # Remove .jpg/.png from name

# Start webcam
video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()
    if not ret:
        break

    # Resize frame for faster processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    # Detect faces and encode
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(known_faces, face_encoding)
        name = "Unknown"

        if True in matches:
            match_index = matches.index(True)
            name = known_names[match_index]

        # Scale back to original frame size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Draw box and label
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 255, 0), cv2.FILLED)
        cv2.putText(frame, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_DUPLEX, 1.0, (0, 0, 0), 1)

    cv2.imshow('Face Recognition - Press Q to Quit', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
