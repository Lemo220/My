import pyautogui

from utils.MouseInteraction import click_in_square
import random


def type_text(text):
    pyautogui.write(text, interval=random.uniform(0.01, 0.03))


def inputText(topLeft, bottomRight, text):
    click_in_square(topLeft, bottomRight)
    type_text(text)
