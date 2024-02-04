import pyautogui

from MouseInteraction import click_in_square


def type_text(text):
    pyautogui.write(text)

def inputText(topLeft, bottomRight, text):
    click_in_square(topLeft, bottomRight)
    type_text(text)