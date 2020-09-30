import csv
popu2010 = []
valErr = ['--', 'NA']
exceptions = ['Country', 'World', 'Africa', 'Asia & Oceania', 'Europe', 'North America', 'Eurasia', 'Middle East', 'Central & South America']

with open("../populationbycountry19802010millions.csv") as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        if row[-1] not in valErr and row[0] not in exceptions:
            popu2010.append([float(row[-1]), row[0]])

popu2010.sort(reverse = True)
print(popu2010[:5])