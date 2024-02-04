import random
from pyHM import mouse


def click_in_square(top_left, bottom_right):
    x_click = random.randint(top_left[0], bottom_right[0])
    y_click = random.randint(top_left[1], bottom_right[1])
    mouse.move(x_click, y_click)
    mouse.click()
