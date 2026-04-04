import openpyxl
import pytest

def get_test_data():
    # loading workbook
    wb = openpyxl.load_workbook("C:\Desktop\Selenium\sample.xlsx")
    ws = wb["Sheet1"]
    data = []

    for i in ws.iter_rows(min_row=2,values_only=True):
        data.append(i)
        
    return data

