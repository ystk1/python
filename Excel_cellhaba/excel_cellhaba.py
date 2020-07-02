'''
    sheet_width.py
    purpose: make new xlsx and set width automatically
'''

import openpyxl as xl


# set input file name
inputfile = 'test.xlsx'

# read input xlsx
wb1 = xl.load_workbook(filename=inputfile)
ws1 = wb1.worksheets[0]

# set column width
for col in ws1.columns:
    max_length = 0
    column = col[0].column

    for cell in col:
        if len(str(cell.value)) > max_length:
            max_length = len(str(cell.value))

    adjusted_width = (max_length + 2) * 1.2
    ws1.column_dimensions[column].width = adjusted_width

# save xlsx file
wb1.save(inputfile)



# # set column width
# for col in ws1.columns:
#     max_length = 0
#     column = col[0].column

#     for cell in col:
#         if len(str(cell.value)) > max_length:
#             max_length = len(str(cell.value))

#     adjusted_width = (max_length + 2) * 1.2