import cv2
from ScreenCapture import ScreenCapture
from TextRec import recognize_number
from MouseInteraction import click_in_square
from KeyboardInteraction import type_text
from utils.excel import ExcelFile
from constants import SEARCH_INPUT_CORDS



def main():
    capture = ScreenCapture()
    
    try:
        while True:
          frame = capture.get_frame()
          inputText(SEARCH_INPUT_CORDS)
          if 0xFF == ord('r'):
              cropped_image = frame[422:444, 1070:1150]
              text = recognize_number(cropped_image)
              print(text)
          if  0xFF == ord('q'):
            capture.stop()
            break
                  
    finally:
        capture.stop()
        cv2.destroyAllWindows()

def inputText(topLeft, bottomRight):
    click_in_square(topLeft, bottomRight)
    type_text("Hello, World!")

if __name__ == "__main__":
    main()