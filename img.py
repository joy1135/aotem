import cv2
import numpy as np
from matplotlib import pyplot as plt
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


img = cv2.imread("images/img15.jpg") #загрузка фотографии 


img_g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

lwr = np.array([69], dtype=np.uint8)
upr = np.array([203], dtype=np.uint8)

# Apply inRange function
msk = cv2.inRange(img_g, lwr, upr)

# Display the mask

img_g = cv2.GaussianBlur(img_g, (5,5), 0) #блюр для урощениия картинки

cv2.imshow('img' , img_g)
cv2.waitKey(0)
for i in range(0,14):
    try:
        txt = pytesseract.image_to_string(img_g, config=f'--psm {i} --oem 3 -c tessedit_char_whitelist=0123456789.', lang= 'eng')
        print(i,txt)
    except Exception as e:
        print(i,'error')

edges = cv2.Canny(img_g, 10, 120) #контуры
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
closed = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)
dilation = cv2.dilate(edges,kernel,iterations=1)

res = 255 - cv2.bitwise_and(dilation, msk)



txt = pytesseract.image_to_string(res, config="--psm 6 digits")
print(''.join(t for t in txt if t.isalnum()))

cv2.imshow('img' , img_g)
cv2.waitKey(0)