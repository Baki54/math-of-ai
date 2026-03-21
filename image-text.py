import pytesseract as pt
import cv2

image=cv2.imread("/home/nayon/Screenshot_2026-02-01-08-23-37-982_com.xiaomi.scanner.jpg")
text=pt.image_to_string(image,lang='eng')
print(text)