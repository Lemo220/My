import openpyxl

FILE_PATH='./items_price.xlsx'

class ExcelFile:
    def __init__(self) -> None:
        wb = openpyxl.load_workbook(FILE_PATH)
        self.ws = wb.active  # Assuming we're working with the first sheet

    def getExcelFile(self):
        return self.ws
        
    def saveExcelFile(self, file):
        self.ws.save(FILE_PATH)
