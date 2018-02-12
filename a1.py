import csv
import json

with open("GT.csv") as GT:
	readCSV = list(csv.reader(GT, delimiter=','))
	
	keys = readCSV[0]
	data = readCSV[1:]
	
	entries = []
	
	for row in data:
		entries.append(dict(zip(keys, row)))

	print('The last 100 terrorism targes:')
	for attack in entries[-100:]:
		print(attack['target1'])
		
		
	with open("terror.json", "w") as file2:
		json.dump(entries[-100:], file2)
