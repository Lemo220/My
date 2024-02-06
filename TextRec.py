import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def recognize_number(image):
    # Assuming image is a cropped OpenCV image
    custom_config = r"--oem 3 --psm 6 -c tessedit_char_whitelist=0123456789"
    number_str = pytesseract.image_to_string(
        Image.fromarray(image), config=custom_config
    )

    # Usunięcie wszystkich znaków oprócz cyfr
    filtered_number_str = "".join(filter(str.isdigit, number_str))

    return filtered_number_str


def recognize_text(image):
    # Assuming image is a cropped OpenCV image
    # Konwersja obrazu OpenCV (numpy array) do formatu obrazu PIL
    image_pil = Image.fromarray(image)
    # Konfiguracja do rozpoznawania tylko liter
    custom_config = r"--oem 3 --psm 6 -c tessedit_char_whitelist=abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    text = pytesseract.image_to_string(image_pil, config=custom_config)
    return text
