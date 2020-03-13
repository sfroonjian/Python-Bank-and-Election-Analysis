import os
import csv

csvpath = os.path.join("budget_data.csv")
output_path = os.path.join("output.csv")

date = []
profloss = []
change = []

with open(csvpath) as csvfile:
	csvreader = csv.reader(csvfile, delimiter = ',')
	csv_header = next(csvreader)
	for row in csvreader:
		date.append(row[0])
		profloss.append(int(row[1]))

for i in range(len(profloss) -1):
	num = (profloss[i+1]) - (profloss[i])
	change.append(int(num))

totalmonths = len(date)
totalprof = sum(profloss)
lenchange = len(change)
totalchange = sum(change)
average = round((totalchange / lenchange), 2)
maxchange = max(change)
minchange = min (change)

maxposition = change.index(maxchange)
minposition = change.index(minchange)
datemax = date[maxposition + 1]
datemin = date[minposition + 1]

with open(output_path, 'w') as outputfile:
	writer = csv.writer(outputfile)
	writer.writerow(["Financial Analysis"])
	writer.writerow(["Total Months:", totalmonths])
	writer.writerow(["Total:", totalprof])
	writer.writerow(["Average Change:", average])
	writer.writerow(["Greatest Increase in Profits:", datemax, maxchange])
	writer.writerow(["Greatest Increase in Profits:", datemin, minchange])

print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(totalmonths))
print("Total: $" + str(totalprof))
print("Average Change: $" + str(average))
print("Greatest Increase in Profits: " + datemax + " ($" + str(maxchange) + ")")
print("Greatest Decrease in Profits: " + datemin + " ($" + str(minchange) + ")")