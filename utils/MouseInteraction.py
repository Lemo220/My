import random
import pyautogui
from constants.resolution_1920x1080 import CLEAR_NAME_CORDS


def click_in_square(top_left, bottom_right):
    x_click = random.randint(top_left[0], bottom_right[0])
    y_click = random.randint(top_left[1], bottom_right[1])
    pyautogui.moveTo(
        x_click,
        y_click,
    )
    pyautogui.click()


def clearName():
    CLEAR_NAME_CORDS
    x_click = random.randint(CLEAR_NAME_CORDS["posx1"], CLEAR_NAME_CORDS["posx2"])
    y_click = random.randint(CLEAR_NAME_CORDS["posy1"], CLEAR_NAME_CORDS["posy2"])
    pyautogui.moveTo(x_click, y_click)
    pyautogui.click()
