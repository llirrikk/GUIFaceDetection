from tkinter import *
import cv2
import sys
from os import chdir
from random import choice, randint

root = Tk()
root.title("Главное окно")


def about():
    cascPath = "haarcascade.xml"

    faceCascade = cv2.CascadeClassifier(cascPath)

    image = cv2.imread(message.get())
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    print("Found {0} faces.".format(len(faces)))

    for x, y, w, h in faces:
        sub_img = image[y: y + h, x: x + w]
        cv2.circle(
        img=image,
        center=(x + 30, y + 30),
        radius=40,
        color=(0, 225, 0),
        thickness=2)

    cv2.imshow("Found {0} faces".format(len(faces)), image)
    cv2.waitKey(0)

message = StringVar()

Label(text="Введите путь к изображению", width=50, height=3).pack()
Entry(textvariable=message, width=60).pack()
Button(text="Обнаружить", width=20, command=about).pack()

root.mainloop()
