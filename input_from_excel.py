from openpyxl import load_workbook
import os.path
import sqlite3, sys

class InputExcel:
    def __init__(self, name):
        wb = load_workbook(filename = name, read_only=True)
        ws = wb["file"]


if __name__ == "__main__":
    if len(sys.argv) is 1:
        print("Please input an excel filename (Usage: python input_from_excel.py test.xlsx)")
    elif not os.path.isfile(sys.argv[1]):
        print(sys.argv[1],"does not exist.")
    else:
        InputExcel(sys.argv[1])
