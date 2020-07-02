# xlrow_stop_all_empty.py
import openpyxl

def is_empty(cell):
    return cell.value is None or not str(cell.value).strip()

wb = openpyxl.load_workbook("./company_members_test.xlsx")
ws = wb.worksheets[0]

for row in ws.iter_rows(min_row=2):
    if all(is_empty(c) for c in row):
        break
    values = []
    for col in row:
        values.append(col.value)
    print(values)