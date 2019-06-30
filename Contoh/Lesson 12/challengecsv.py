import csv

csvData = [['Susan', '32'], ['Mike', '33'], ['Christopher', '80'], ['Bill', '100']]

with open('challenge.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(csvData)

csvFile.close()

with open('challenge.csv', 'r') as csvFile:
    dataFromFile = csv.reader(csvFile)
    for row in dataFromFile:
        print(', '.join(row))