# Face Recognition System 👤📷

This project is a real-time face recognition system using Python, OpenCV, and the `face_recognition` library. It detects and identifies faces from a webcam feed.

## 🔧 Features

- Detects faces from live webcam
- Identifies known faces (like Ank 😎)
- Draws bounding boxes with names

## 🗂 Folder Structure

FaceRecognisation/
│
├── face_recog.py # Main script
├── known_faces/ # Folder with images of known people
│ ├── Ank.jpg
│ └── Gublu.jpg
|

## 🛠 Requirements

- Python 3.x
- OpenCV
- face_recognition
- dlib

Install libraries:

```bash
pip install opencv-python face_recognition

▶️ How to Run
Add clear face images to known_faces/ folder.

Run the script:
python face_recog.py

Look into the webcam — it’ll say your name if recognized!