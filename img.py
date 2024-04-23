import cv2
import numpy as np
from matplotlib import pyplot as plt
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'


img = cv2.imread("images/img10.jpg") #загрузка фотографии 

img_g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
lwr = np.array([83], dtype=np.uint8)
upr = np.array([203], dtype=np.uint8)

# Apply inRange function
msk = cv2.inRange(img_g, lwr, upr)

# Display the mask

img_g = cv2.GaussianBlur(img_g, (5,5), 0) #блюр для урощениия картинки
edges = cv2.Canny(img_g, 10, 120) #контуры
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,3))
closed = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)
dilation = cv2.dilate(edges,kernel,iterations=1)

res = 255 - cv2.bitwise_and(dilation, msk)



txt = pytesseract.image_to_string(res, config="--psm 6 digits")
print(''.join(t for t in txt if t.isalnum()))

cv2.imshow('img' , res)
cv2.waitKey(0)