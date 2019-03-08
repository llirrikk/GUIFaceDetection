from tkinter import *
from tkinter import messagebox as mb
from tkinter import filedialog as fd
import cv2
import sys
from os import chdir, mkdir, path
from random import choice, randint

root = Tk()
root.title("Обнаружение лиц на изображении")

cascPath = "haarcascade.xml"
faceCascade = cv2.CascadeClassifier(cascPath)


def check(pathtoimg, image, gray, faces):
    answer = mb.askyesno(title="Вопрос", message="Обрезать лица?")
    if answer == True:

        filename = path.splitext(pathtoimg)[0]
        mkdir(filename + "_output")
        i=0
        for (x, y, w, h) in faces:
            sub_img = image[y : y + h, x : x + w]
            i=i+1
            chdir(filename + "_output") 
            cv2.imwrite(str(i) + ".jpg", sub_img)
            chdir("../")
            int(i)
        exit()
    else: exit()


def about():

    pathtoimg = fd.askopenfilename()
    image = cv2.imread(pathtoimg)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))


    for (x, y, w, h) in faces:
        sub_img = image[y: y + h, x: x + w]
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow("Found {0} faces".format(len(faces)), image)
    cv2.waitKey(0)
    check(pathtoimg, image, gray, faces)

	

Label(text="Выберете изображение", width=50, height=3, font=("Helvetica", 16)).grid(columnspan=2)
Button(text="Обнаружить", width=20, command=about).grid(row=1, column=1)
root.resizable(False, False)

root.mainloop()
