import openpyxl

def readexcel():
    wb = openpyxl.load_workbook(filename="efatura.xlsx")
    ws = wb.get_sheet_by_name('EFatura')

    for cellvalue in range(0, ws.max_row):
        print(ws.cell(row=cellvalue+1, column=1).value)


if __name__ == '__main__':
    readexcel()
