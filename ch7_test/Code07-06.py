import xlrd
import csv

workbook = xlrd.open_workbook('Excel/singer.xls')

wsheetList = workbook.sheets()
for worksheet in wsheetList :
    with open("Excel/singer_2-" + worksheet.name + ".csv", "w", encoding='utf-8', newline='') as outFp:
        csvWriter = csv.writer(outFp)
        for row in range(worksheet.nrows) :
                row_list = worksheet.row_values(row)
                csvWriter.writerow(row_list)

print("Save. OK~")