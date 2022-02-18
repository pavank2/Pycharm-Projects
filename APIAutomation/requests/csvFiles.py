import csv
with open('../config/loanStatus.csv') as csvFile:
        csvReader = csv.reader(csvFile,delimiter=',',quotechar='"')

        names = []
        status = []
        for row in csvReader:
            names.append(row[0])
            status.append(row[1])

index = names.index('Sam')

print(names[index]+" Loan Status is "+status[index])

with open('../config/loanStatus.csv', 'a') as csvWrite:
     csvWrite = csv.writer(csvWrite)
     csvWrite.writerow(["Kim", "Approved"])
