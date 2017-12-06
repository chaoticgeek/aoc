#/usr/bin/python

spreadsheet = "2.spreadsheet.txt"

def calculateChecksum(spreadsheet):
    checksum = 0
    spreadsheetList = openSpreadsheet(spreadsheet)
    for row in spreadsheetList:
        checksum += calculateRowChecksum(row)
    return checksum

def calculateRowChecksum(row):
    return max(row) - min(row)

def openSpreadsheet(spreadsheet):
    spreadsheetList = []
    with open(spreadsheet) as file:
        for line in file:
            spreadsheetList.append(list(map(int, line.split("\t"))))
    return spreadsheetList

def calculateChecksum2(spreadsheet):
    spreadsheetList = openSpreadsheet(spreadsheet)
    checksum = 0
    for row in spreadsheetList:
        checksum += calculateRowChecksum2(sorted(row, key=int, reverse=True))
    return checksum

def calculateRowChecksum2(row):
    for k, v in enumerate(row):
        for x in enumerate(row[k+1:]):
            if v % x[1] == 0:
                return int(v/x[1])
    return 0

if __name__ == '__main__':
    print("Spreadsheet checksum is {}".format(calculateChecksum(spreadsheet)))
    print("Spreadsheet checksum2 is {}".format(calculateChecksum2(spreadsheet)))
