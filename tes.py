import pytesseract

img = 'images/image.png'
txt = pytesseract.image_to_string(img)
print(txt)