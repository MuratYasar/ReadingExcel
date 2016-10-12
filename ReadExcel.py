import openpyxl

def readexcel():
    wb = openpyxl.load_workbook(filename="efatura.xlsx", read_only=True)
    ws = wb.get_sheet_by_name('EFatura')

    with open("output.txt", "w") as textfile:
        for row in ws.rows:
            for cell in row:
                textfile.write(cell.value + "\n")

if __name__ == '__main__':
    readexcel()
