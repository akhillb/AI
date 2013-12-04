from operator import attrgetter

class City(object):
	def __init__(self,city_id,x,y):
		self.city_id = city_id
		self.x = x
		self.y = y 
	
	def displayCity(self):
		print "City "+str(self.city_id) +" Position : (" + str(self.x) +","+str(self.y)+")"
	
class Edge(object):
	def __init__(self,city1,city2,dist):
			self.city1=city1
			self.city2=city2
			self.dist=dist

class Graph(object):
	def __init__(self,city_count):
		self.city = []
		self.distance = []

	def makeCity(self,string):
		temp = string.split(' ')
		city = City(len(self.city)+1,float(temp[0]),float(temp[1]))
		self.city.append(city)
	
	def distanceInput(self,string):
		temp = string.strip()
		temp = temp.split(' ')
		temp = map(float, temp)
		self.distance.append(temp)

	def getDistance(self,city1,city2):
		return self.distance[city1-1][city2-1]

	def displayCities(self):
		for city in self.city:
			city.displayCity()
	
	def showDistances(self):
		for row in self.distance:
			print row

	def sub_input(self,cities):
		new_distance = []
		for x in range(cities):
			temp = []
			for y in range(cities):
				temp.append(self.distance[x][y])
			new_distance.append(temp)
		return new_distance
