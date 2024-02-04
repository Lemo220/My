import time
import openpyxl
from KeyboardInteraction import inputText

from MouseInteraction import click_in_square
from ScreenCapture import ScreenCapture
from TextRec import recognize_number
from constants.resolution_1920x1080 import *

class ExcelFile:
    def __init__(self, file_path) -> None:
        self.capture = ScreenCapture()
        self.wb = openpyxl.load_workbook(file_path)
        self.ws = self.wb.active
        self.file_path = file_path

    def process_rows(self):
        previous_values = {"col2": None, "col3": None}  # Słownik przechowujący poprzednie wartości
        row_number = 2  # Zaczynamy od drugiego rzędu
        for row in self.ws.iter_rows(min_row=2, values_only=True):
            print(row)
            item, value_col2, value_col3, *_ = row  # Rozpakowanie wartości z rzędu
            pos = SEARCH_INPUT_CORDS
            inputText((pos["posx1"], pos["posy1"]), (pos["posx2"], pos["posy2"]), item)
            # Sprawdzenie i działanie dla drugiej kolumny
            if value_col2 != previous_values["col2"]:
                self.switchCategory('tier', value_col2)
                previous_values["col2"] = value_col2  # Aktualizacja poprzedniej wartości dla drugiej kolumny

            # Sprawdzenie i działanie dla trzeciej kolumny
            if value_col3 != previous_values["col3"]:
                self.switchCategory('enchant', value_col3)
                print(f"Clicking for value {value_col3} in column 3")  # Placeholder dla demonstracji
                previous_values["col3"] = value_col3  # Aktualizacja poprzedniej wartości dla trzeciej kolumny

            price = self.scanMarket()
            # Zapisanie ceny do piątej kolumny
            self.ws.cell(row=row_number, column=5, value=price)
            row_number += 1  # Przejście do następnego rzędu
        self.save()

    def save(self):
        self.wb.save(self.file_path)

    def scanMarket(self):
        time.sleep(2)
        frame = self.capture.get_frame()
        cropped_image = frame[422:444, 1070:1150]  # Adjust these coordinates as needed
        text = recognize_number(cropped_image)
        return text

    def switchCategory(self, category, position):
        if position == None:
            position =0
        if category == 'tier':
            posx1 = TIER_DROPDOWN_CORDS['posx1']
            posy1 = TIER_DROPDOWN_CORDS['posy2']
            posx2 = TIER_DROPDOWN_CORDS['posx2']
            posy2 = TIER_DROPDOWN_CORDS['posy2']
        elif category == 'enchant':
            posx1 = ENCHANT_DROPDOWN_CORDS['posx1']
            posy1 = ENCHANT_DROPDOWN_CORDS['posy2']
            posx2 = ENCHANT_DROPDOWN_CORDS['posx2']
            posy2 = ENCHANT_DROPDOWN_CORDS['posy2']
        elif category == 'quality':
            posx1 = QUALITY_DROPDOWN_CORDS['posx1']
            posy1 = QUALITY_DROPDOWN_CORDS['posy2']
            posx2 = QUALITY_DROPDOWN_CORDS['posx2']
            posy2 = QUALITY_DROPDOWN_CORDS['posy2']
        print((posx1, posy1), (posx2, posy2))
        click_in_square((posx1, posy1), (posx2, posy2))
        click_in_square((posx1, SUB_ELEMENTS_CORDS[position]['posy1']), (posx2, SUB_ELEMENTS_CORDS[position]['posy2']))
