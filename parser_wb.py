import pandas as pd
import xlrd


def parser_stock():
    file = 'report_2022_8_26.xlsx'
    workbook = xlrd.open_workbook("report_2022_8_26.xlsx")
    # Open the worksheet
    worksheet = workbook.sheet_by_index(0)
    # Iterate the rows and columns
    for i in range(0, 5):
        for j in range(0, 3):
            # Print the cell values with tab space
            print(worksheet.cell_value(i, j), end='\t')
        print('')



if __name__ == '__main__':
    parser_stock()