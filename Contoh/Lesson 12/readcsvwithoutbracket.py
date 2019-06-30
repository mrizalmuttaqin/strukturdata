import csv

fileName = "test.csv"
accessMode = "r"
with open(fileName, accessMode) as csvFile:
    dataFromFile = csv.reader(csvFile)
    for row in dataFromFile:
        print(', '.join(row))