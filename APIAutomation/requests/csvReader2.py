import csv

with open('../config/loanStatus.csv') as csvFile:
    csvReader=csv.reader(csvFile,delimiter=',',quotechar='"')

    col1 = []
    col2 = []

    for row in csvReader:
        col1.append(row[0])
        col2.append(row[1])

    print(col1.index("Tim"))

with open('../config/loanStatus.csv','a',newline='') as csvFile:
    csvWriter = csv.writer(csvFile,delimiter=',')
    csvWriter.writerow(["Bert","Rejected"])

