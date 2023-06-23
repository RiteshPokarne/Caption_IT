import numpy as np
import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
def convert(img_path):
    image = cv2.imread(img_path)
    new_image = np.zeros(image.shape, image.dtype)
    alpha = 1.4 # contrast control
    beta = 0 
    for y in range(image.shape[0]):
        for x in range(image.shape[1]):
            for c in range(image.shape[2]):
                new_image[y,x,c] = np.clip(alpha*image[y,x,c] + beta, 0, 255)

    thresh1=grayscaling(new_image)
    text = pytesseract.image_to_string(thresh1)
    return text


def grayscaling(new_image):
    kernel = np.ones((1, 1), np.uint8)
    new_image = cv2.dilate(new_image, kernel, iterations=1)
    new_image = cv2.erode(new_image, kernel, iterations=1)
    gray_image = cv2.cvtColor(new_image, cv2.COLOR_BGR2GRAY)
    ret,thresh1 = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)
    return thresh1
