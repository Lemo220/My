import pyautogui
import random

def click_in_square(top_left, bottom_right):
    x_click = random.randint(top_left[0], bottom_right[0])
    y_click = random.randint(top_left[1], bottom_right[1])
    pyautogui.click(x_click, y_click)