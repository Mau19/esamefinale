#!/usr/bin/python 
import fileinput

indexPizza = 0
indexQty = 1

data = {}
for line in fileinput.input():
	values = line.split('\t')
	Pizza = values[indexPizza]
	Quantity = int(values[indexQty])
	tmp = {Pizza:Quantity}
	if Pizza in data:
		data[Pizza] = data[Pizza] + tmp[Pizza]
	else:
		data.update(tmp)
print(data)