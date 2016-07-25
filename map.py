#!/usr/bin/python 
import fileinput

indexPizza = 2
indexQty = 6

for line in fileinput.input():
	values = line.split(';')
	Pizza = values[indexPizza]
	Quantity = values[indexQty]
	print(('{0}\t{1}'.format(Pizza,Quantity)).replace('\n',''))
