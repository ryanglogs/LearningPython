import xlrd
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime

path = "stats1.xlsx"

inputWorkbook = xlrd.open_workbook(path)

inputWorksheet = inputWorkbook.sheet_by_index(0)

#x = datetime.datetime.now()
#print(x.strftime("%X"))

print("Rows: ", inputWorksheet.nrows)
print("Cols: ", inputWorksheet.ncols)

shoe_size_male = []
height_male = []
shoe_size_female = []
height_female = []
age = []
health_rating = []
for i in range(inputWorksheet.nrows):
	#for x in range(inputWorksheet.ncols):
		#print(inputWorksheet.cell_value(i,x), end = ' ')
	if(inputWorksheet.cell_value(i,1) != "Age" and inputWorksheet.cell_value(i,9) != "Health_Rating"):
		age.append(inputWorksheet.cell_value(i,1))
		health_rating.append(inputWorksheet.cell_value(i,9))
	if(inputWorksheet.cell_value(i,2) == "M"):
		shoe_size_male.append(inputWorksheet.cell_value(i, 3))
		height_male.append(inputWorksheet.cell_value(i, 4))
	elif(inputWorksheet.cell_value(i,2) == "F"):
		shoe_size_female.append(inputWorksheet.cell_value(i, 3))
		height_female.append(inputWorksheet.cell_value(i, 4))


#print(shoe_size_female)
#print(height_female)
#print(shoe_size_male)
#print(height_male)
#print(age)
#print(health_rating)

age_cats = []
age_quant = []
age_cats = set(age)

for num in age_cats:
	#print(num,": ", age.count(num))
	age_quant.append(age.count(num))

age = list(age_cats)

health_quant = []
for num in health_rating:
	health_quant.append(health_rating.count(num))
	
#print(age_cats)
#print(age_quant)
#print(age)	

plt.figure(figsize=(12,4))
plt.subplot(131)
plt.scatter(shoe_size_male, height_male)
plt.subplot(131)
plt.scatter(shoe_size_female, height_female)
plt.subplot(132)
plt.bar(age, age_quant)
plt.subplot(133)
plt.bar(health_rating, health_quant)
plt.suptitle('Stats Data')
plt.show()

#y = datetime.datetime.now()
#print(y.strftime("%X"))
