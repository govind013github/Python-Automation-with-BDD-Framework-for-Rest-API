import csv

# Read CSV FILE in python.
with open('utilities/loanapp.csv') as csvFile:  # using here relative path of file location.
    csvReader = csv.reader(csvFile, delimiter=',')
    # print(csvReader)
    # print(list(csvReader))
    names = []
    stats = []
    for row in csvReader:
        names.append(row[0])
        stats.append(row[1])

print(names)
print(stats)

Index = names.index('Tim')
loanStatus = stats[Index]
print('loan status: ' + loanStatus)

# Write CSV FILE in python.
with open('utilities/loanapp.csv', 'a') as wFile:
    write = csv.writer(wFile)
    write.writerow(["Bob", "rejected"])
