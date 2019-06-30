import csv

csvData = [['Susan', '32'], ['Mike', '33'], ['Christopher', '80'], ['Bill', '100']]

with open('test.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(csvData)

csvFile.close()