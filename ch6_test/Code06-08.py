import csv

with open("CSV/singerA.csv", "r", encoding='utf-8') as inFpA :
    with open("CSV/singerB.csv", "r", encoding='utf-8') as inFpB:
        with open("CSV/singerSum-1.csv", "w", encoding='utf-8', newline='') as outFp:
            csvReaderA = csv.reader(inFpA)
            csvReaderB = csv.reader(inFpB)
            csvWriter = csv.writer(outFp)
            header_list = next(csvReaderA)
            header_list = next(csvReaderB)
            csvWriter.writerow(header_list)

            for row_list in csvReaderA:
                csvWriter.writerow(row_list)
            for row_list in csvReaderB:
                csvWriter.writerow(row_list)

print('Save. OK~')