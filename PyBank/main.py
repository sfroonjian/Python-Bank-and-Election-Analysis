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
	# goes through every row in the data set
	for row in csvreader:
		# add each item in the date column to the date list
		date.append(row[0])
		# add each item in the profit/loss column to the profloss list
		profloss.append(int(row[1]))

# goes through the length of the profloss list, subtracts the current value from the next value, and adds that value to the change list
for i in range(len(profloss) -1):
	num = (profloss[i+1]) - (profloss[i])
	change.append(int(num))

# uses built-in functions to find the values of needed variables
totalmonths = len(date)
totalprof = sum(profloss)
lenchange = len(change)
totalchange = sum(change)
average = round((totalchange / lenchange), 2)
maxchange = max(change)
minchange = min (change)

# finds the position in the change list of the max amount
maxposition = change.index(maxchange)
# finds the position in the change list of the min amount
minposition = change.index(minchange)
# matches up the date of the max change by matching indexes
datemax = date[maxposition + 1]
# matches up the date of the min change by matching indexes
datemin = date[minposition + 1]

# writes data to a csv file
with open(output_path, 'w') as outputfile:
	writer = csv.writer(outputfile)
	writer.writerow(["Financial Analysis"])
	writer.writerow(["Total Months:", totalmonths])
	writer.writerow(["Total:", totalprof])
	writer.writerow(["Average Change:", average])
	writer.writerow(["Greatest Increase in Profits:", datemax, maxchange])
	writer.writerow(["Greatest Increase in Profits:", datemin, minchange])

# prints data to terminal
print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(totalmonths))
print("Total: $" + str(totalprof))
print("Average Change: $" + str(average))
print("Greatest Increase in Profits: " + str(datemax) + " ($" + str(maxchange) + ")")
print("Greatest Decrease in Profits: " + str(datemin) + " ($" + str(minchange) + ")")