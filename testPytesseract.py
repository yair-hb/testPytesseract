import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

imagen = cv2.imread('imgColores.jpg')
imagen2 = cv2.imread('imgBN.jpg')
text = pytesseract.image_to_string(imagen, lang='spa')
text2 = pytesseract.image_to_string(imagen2,lang='spa')
print ('Texto: ', text)
print ('Texto2: ',text2)

cv2.imshow('imagen',imagen)
cv2.imshow('imagen2', imagen2)
cv2.waitKey(0)
cv2.destroyAllWindows()

