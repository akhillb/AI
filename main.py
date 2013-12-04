import buildGraph as b
import sys
import os
from random import randint
from nearest import nearest
from greedy import *
from savings import *

print "Input taken from euc_7 file"
input_file = open("euc_100","r")
cities = int(input_file.readline())
space = b.Graph(cities)
for i in range(cities):
	space.makeCity(input_file.readline())
for line in input_file:
	space.distanceInput(line)

print "Enter number of cities"
no_of_cities = int(raw_input())
distance = space.sub_input(no_of_cities)
new_distance = []
i = 0
for row in distance:
	j = 0
	candid = []
	for item in row:
		temp = (i,j,item)
		candid.append(temp)
		j = j+1
	new_distance.append(candid)
	i = i+1

for row in new_distance:
	row.sort(key = lambda x:x[2])

while(True):
	print "Select algorithm"
	print "1. Nearest Neighbour algorithm"
	print "2. Greedy algorithm"
	print "3. Savings Heuristic"
	print "4. Exit"
	choice = raw_input()
	if choice is '1':
		print "--------------Nearest Neighbour--------------"
		print "Choose the starting city"
		temp = raw_input()
		if temp is '':
			print "No input given. Random city choosen"
			start = randint(1,no_of_cities)	
		else:
			start = int(temp)
			if start > no_of_cities:
				print "Input out of range of choosen number of cities. Random city choosen"
				start = randint(1,no_of_cities)
		nearest(start,new_distance,distance)
	elif choice is '2':
		print "--------------Greedy Algorithm--------------"
		paths = greedy(no_of_cities,new_distance,distance)
	elif choice is '3':
		print "--------------Savings Heuristic--------------"
		print "Choose base city"
		temp = raw_input()
		if temp is '':
			print "No input given. Random city choosen"
			base = randint(1,no_of_cities)
		else:
			base = int(temp)
			if base > no_of_cities:
				print "Bad input given. Random city choosen"
				base = randint(1,no_of_cities)
		savings_heuristic(base,no_of_cities,distance)
	elif choice is '4':
		sys.exit(0)
