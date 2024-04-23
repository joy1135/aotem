import cv2
import numpy as np

def  text_rec(file_path):
    return 
    
   

def main():
    img = cv2.imread('images/img2.jpg', cv2.IMREAD_GRAYSCALE)
    img = cv2.Canny(img, 120, 120)

    kernel = np.ones((5, 5), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)
    #img = cv2.bitwise_and(img,)
    cv2.imshow('img',img)
    cv2.waitKey(0)
    cv2.imwrite('images/img2_gray.jpg', img)



if __name__ == "__main__":
    main()