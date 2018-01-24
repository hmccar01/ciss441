import csv
import json

with open("GT.csv") as GT:
	readCSV = csv.reader(GT, delimiter=',')
	
	GTData = list(readCSV)

for line in range(10):
	print(GTData[line][:4])
	
print()
for line in range(30,10,-1):
	print(json.dumps(GTData[line][:4]))
	
with open("GT.json", "w") as GTjson:
	json.dump(GTData, GTjson)
