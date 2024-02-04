import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def recognize_number(image):
    # Assuming image is a cropped OpenCV image
    custom_config = r"--oem 3 --psm 6 outputbase digits"
    number = pytesseract.image_to_string(Image.fromarray(image), config=custom_config)
    return number
