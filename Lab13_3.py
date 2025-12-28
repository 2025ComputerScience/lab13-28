import cv2
import pytesseract

def get_precise_output(image_path):
    
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    custom_config = r'--oem 3 --psm 6 -l eng+chi_tra'
    result = pytesseract.image_to_string(thresh, config=custom_config)
    
    return result.strip()
print(get_precise_output('2.png'))