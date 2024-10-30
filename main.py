import cv2

img = cv2.imread("car.jpg")
height, width, _ = img.shape #Получаем размер изображения
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)#перевод изображения в серый
treash = cv2.threshold(gray_img, 0, 255, cv2.THRESH_OTSU)[1] #Отбор черного цвета

