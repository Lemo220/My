import pyautogui

from MouseInteraction import click_in_square
import random


def type_text(text):
    pyautogui.write(text, interval=random.uniform(0.1, 0.3))


def inputText(topLeft, bottomRight, text):
    click_in_square(topLeft, bottomRight)
    type_text(text)
