import csv
import pandas
field_names=['Roll_No', 'Name', 'Age']
stud_dict=[{'Roll_No':'1', 'Name': 'Aparna','Age': 22},
{'Roll_No':'2', 'Name': 'anjali','Age': 22},
{'Roll_No':'3', 'Name': 'jayalekshmi','Age': 22}
]
with open('Names.csv','w') as f:
	writer=csv.DictWriter(f,fieldnames=field_names)
	writer.writeheader()
	writer.writerows(stud_dict)
	
with open("Names.csv",'r') as f:
	data=csv.reader(f)
	for i in data:
		print(i)
data=pandas.read_csv("Names.csv")	
print(data)	
