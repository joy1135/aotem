import cv2

def  text_rec(file_path):
    return 
    
   

def main():
    img = cv2.imread('img2.jpg', cv2.IMREAD_GRAYSCALE)
    cv2.imshow('img2',img)
    cv2.waitKey(0)
    cv2.imwrite('img2_gray.jpg', img)

if __name__ == "__main__":
    main()