from tkinter import *
from tkinter import messagebox as mb
from tkinter import filedialog as fd
import cv2
from os import chdir, mkdir, path
from PIL import Image, ImageTk

root = Tk()
root.title("Обнаружение лиц на изображении")

cascPath = "haarcascade.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

def check(pathtoimg, image, faces):
#    answer = mb.askyesno(title="Вопрос", message="Обрезать лица?")
#    if answer == True:

    image = cv2.imread(pathtoimg)  # убрать квадраты
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

def end(root2):
    root2.flag = False
    root2.destroy()


def button_fullpath():
    fullpathtoimg = fd.askopenfilenames()

    count = 0
    for i in str(fullpathtoimg):
        if i == "'":
            count += 1
    count = int(count / 2)
    print("paths: ", fullpathtoimg)
    print("number of uploaded images: ", count)

    if count > 1:
        replace = str(fullpathtoimg)\
            .replace("('", "")\
            .replace("', '", "@")\
            .replace("')", "")\

    elif count == 1:
        replace = str(fullpathtoimg)\
            .replace("('", "")\
            .replace("',)", "")

    splitpath = str(replace).split("@")
    i = 0
    for currentimg in splitpath:
        i += 1
        print(i, "/", count, ":    ", currentimg)
        pathtoimg = currentimg

        extension = pathtoimg[-4:].lower()

        if extension != ".jpg" and extension != ".png" and extension != "jpeg":
            mb.showerror("Ошибка", "Должно быть выбрано изображение")
        else:
            image = cv2.imread(pathtoimg)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            faces = faceCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

            for (x, y, w, h) in faces:
                cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

            root2 = Toplevel(root)

            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            image = Image.fromarray(image)
            image = ImageTk.PhotoImage(image)

            Label(root2, image=image, width=1200, height=700).pack(side=TOP)
            Button(root2, text="Сохранить лица", width=50, height=100, font=("Times", "15"), command=lambda: check(pathtoimg, image, faces)).pack(side=BOTTOM)
#                Button(root2, text="Следубщая", command=lambda: next())
            root2.protocol('WM_DELETE_WINDOW',lambda: end(root2))

            root2.flag = True
            while root2.flag:
                root2.update()

def exit():
    raise SystemExit()

Label(text="Выбрать изображение", width=30, height=2, font=("Times", 16)).grid(columnspan=2)
Button(text="Обнаружить", width=30, command=button_fullpath, font="Times").grid(row=1, column=1)
Button(text="Закрыть", width=10, command=exit, font="Times").grid(row=1, column=0)
root.resizable(False, False)

root.mainloop()