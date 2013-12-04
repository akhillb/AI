import buildGraph as b
import sys
import os

cities = int(sys.stdin.readline())
space = b.Graph(cities)
for i in range(cities):
	space.makeCity(sys.stdin.readline())
for line in sys.stdin:
	space.distanceInput(line)
