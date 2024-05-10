import cv2
import numpy as np
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

img_color = cv2.imread("images/img17.jpg")
img = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

RATIO = img.shape[0] * 0.2

#cv2.imshow('img',img)
#cv2.waitKey(0)

img = cv2.bilateralFilter(img, 5, 30, 60)

trimmed = img[int(RATIO) :, int(RATIO) : img.shape[1] - int(RATIO)]
img_color = img_color[int(RATIO) :, int(RATIO) : img.shape[1] - int(RATIO)]

#cv2.imshow('Blurred and Trimmed',trimmed)
#cv2.waitKey(0)

edged = cv2.adaptiveThreshold(trimmed, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 5, 5)

cv2.imshow("Edged", edged)
cv2.waitKey(0)


kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 5))
dilated = cv2.dilate(edged, kernel, iterations=1)
dilated = cv2.bitwise_not(dilated)

cv2.imshow("Dilated", dilated)
cv2.waitKey(0)

txt = pytesseract.image_to_string(dilated, config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789.')
print(txt)

dilated = cv2.bitwise_not(dilated)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 1))
dilated = cv2.dilate(dilated, kernel, iterations=1)
dilated = cv2.bitwise_not(dilated)

cv2.imshow("Dilated x2", dilated)
cv2.waitKey(0)

txt = pytesseract.image_to_string(dilated, config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789.')

print(txt)

dilated = cv2.bitwise_not(dilated)
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2, 1),)
eroded = cv2.erode(dilated, kernel, iterations=1)
eroded = cv2.bitwise_not(eroded)

#cv2.imshow("Eroded", eroded)
#cv2.waitKey(0)

txt = pytesseract.image_to_string(eroded, config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789.')
print(txt)