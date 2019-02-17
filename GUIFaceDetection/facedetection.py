import cv2
import sys
from os import chdir                         # модуль для сохранения обрезанных фотографий
from random import choice, randint           # модуль для псевдослучайных чисел (чтобы имена обрезанных фотографий не повторялись)

#def randname(length):
#    valid_letters='qwertyuioplkjhgfdsazxcvbnm0123456789'
#    return ''.join((choice(valid_letters) for i in range(length)))

# Принимаем аргументы 
imagePath = sys.argv[1]         # картинка
cascPath = "haarcascade.xml"    # хаар каскад (признаки Хаара)

img = cv2.imread(imagePath,0)
height, width = img.shape[:2]

# Создаем хаар каскад
faceCascade = cv2.CascadeClassifier(cascPath)

# Read the image
image = cv2.imread(imagePath)                   # чтение изображения
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # перевод в серые оттенки 

# Detect faces in the image
faces = faceCascade.detectMultiScale( # используем метод detectMultiScale
    gray,               # первым параметром передаем изображение в серых оттенках
    scaleFactor=1.1,    # указывкаем процент масштабирования
    minNeighbors=5,     # указываем интенсивность обнаружения лица
    minSize=(30, 30)    # указываем минимальный размер лица
    #flags = cv2.CV_HAAR_SCALE_IMAGE
)

print("Found {0} faces.".format(len(faces))) # вывод количества лиц в консоль
i=0
# Рисуем квадрат вокруг лиц и обрезаем их в папку
for x, y, w, h in faces:
    sub_img = image[y : y + h, x : x + w]
    i=i+1
    chdir("Extracted") 
    cv2.imwrite(str(i) + ".jpg", sub_img) # случайное имя файла для изображений
    chdir("../")
    cv2.circle(
    	img=image,
    	center = (x+30, y+30), 
    	radius = 40, 
    	color = (0,225,0) , 
    	thickness = 2) # зеленый круг вокруг лица cv2.circle(img, center, radius, color, thickness=1, lineType=8, shift=0)
    int(i)

cv2.imshow("Found {0} faces".format(len(faces)), image)
cv2.waitKey(0)
