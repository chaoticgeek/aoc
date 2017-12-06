#/usr/bin/python

spreadsheet = "2.spreadsheet.txt"

def calculateChecksum(spreadsheet):
	checksum = 0
	with open(spreadsheet) as file:
		for line in file:
			row = line.split("\t")
			row = list(map(int, row))
			checksum += calculateRowChecksum(row)
	return checksum

def calculateRowChecksum(row):
	return max(row) - min(row)

if __name__ == '__main__':
	print("Spreadsheet checksum is {}".format(calculateChecksum(spreadsheet)))