from utils.market import ExcelFile
from constants.resolution_1920x1080 import *


def main():

    excel = ExcelFile(MARKET_EXCEL_PATH)
    excel.process_rows()
    excel.save()


if __name__ == "__main__":

    main()
