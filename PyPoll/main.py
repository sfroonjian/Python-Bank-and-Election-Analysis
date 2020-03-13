import os
import csv

csvpath = os.path.join("election_data.csv")
output_path = os.path.join("output.csv")

voterid = []
country = []
candidate = []

with open(csvpath) as csvfile:
	csvreader = csv.reader(csvfile, delimiter = ',')
	csv_header = next(csvreader)
	for row in csvreader:
		voterid.append(row[0])
		country.append(row[1])
		candidate.append(row[2])

khan = 0
correy = 0
li = 0
otooley = 0

for i in range(len(candidate)):
	if candidate[i] == "Khan":
		khan += 1
	elif candidate[i] == "Correy":
		correy += 1
	elif candidate[i] == "Li":
		li += 1
	elif candidate[i] == "O'Tooley":
		otooley += 1

if (khan > correy) and (khan > li) and (khan > otooley):
	winner = "Khan"
elif (correy > khan) and (correy > li) and (correy > otooley):
	winner = "Correy"
elif (li > correy) and (li > khan) and (li > otooley):
	winner = "Li"
else:
	winner = "O'Tooley"

totalvotes = len(voterid)
kpercent = round(((khan / totalvotes) * 100), 3)
cpercent = round(((correy / totalvotes) * 100), 3)
lpercent = round(((li / totalvotes) * 100), 3)
opercent = round(((otooley / totalvotes) * 100), 3)

with open(output_path, 'w') as outputfile:
	writer = csv.writer(outputfile)
	writer.writerow(["Election Results"])
	writer.writerow(["Total Votes:", totalvotes])
	writer.writerow(["Khan:", kpercent, khan])
	writer.writerow(["Corret:", cpercent, correy])
	writer.writerow(["Li:", lpercent, li])
	writer.writerow(["O'Tooley:", opercent, otooley])
	writer.writerow(["Winner:", winner])

print("Election Results")
print("----------------------------")
print("Total Votes: " + str(totalvotes))
print("----------------------------")
print("Khan: " + str(kpercent) + "% (" + str(khan) + ")")
print("Correy: " + str(cpercent) + "% (" + str(correy) + ")")
print("Li: " + str(lpercent) + "% (" + str(li) + ")")
print("O'Tooley: " + str(opercent) + "% (" + str(otooley) + ")")
print("----------------------------")
print("Winner: " + winner)