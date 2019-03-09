from tkinter import *
from tkinter import messagebox as mb
from tkinter import filedialog as fd
import cv2
from os import chdir, mkdir, path

root = Tk()
root.title("Обнаружение лиц на изображении")

cascPath = "haarcascade.xml"
faceCascade = cv2.CascadeClassifier(cascPath)


def check(pathtoimg, image, faces):
    answer = mb.askyesno(title="Вопрос", message="Обрезать лица?")
    if answer == True:

        filename = path.splitext(pathtoimg)[0]
        mkdir(filename + "_output")
        i = 0
        for (x, y, w, h) in faces:
            sub_img = image[y: y + h, x: x + w]
            i = i + 1
            chdir(filename + "_output")
            cv2.imwrite(str(i) + ".jpg", sub_img)
            chdir("../")
            int(i)
        exit()
    else:
        exit()


def about():
    pathtoimg = fd.askopenfilename()
    extension = pathtoimg[-4:]
    if extension != ".jpg" and extension != ".png" and extension != "jpeg":
    	mb.showerror("Ошибка", "Должно быть выбрано изображение")
    else:	
        image = cv2.imread(pathtoimg) 
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv2.imshow("Found {0} faces".format(len(faces)), image)
        cv2.waitKey(0)
        image = cv2.imread(pathtoimg) #убрать квадраты
        check(pathtoimg, image, faces)

def exit():
    raise SystemExit()

Label(text="Выбрать изображение", width=30, height=2, font=("Helvetica", 16)).grid(columnspan=2)
Button(text="Обнаружить", width=30, command=about).grid(row=1, column=1)
Button(text="Закрыть", width=10, command=exit).grid(row=1, column=0)
root.resizable(False, False)

root.mainloop()
