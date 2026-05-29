import pytesseract as pt
import cv2

image=cv2.imread("scanner.jpg")
text=pt.image_to_string(image,lang='eng')
print(text)
