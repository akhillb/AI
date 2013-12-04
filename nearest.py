def path_sot(path,distance):
	src = path[0]
	cost = 0
	for i in range(0,len(path)):
		dest = path[i]
		cost = cost + distance[src-1][dest-1]
	return cost

def nearest(start,distance,new_distance):
	closed = []
	closed.append(start)
	city = start
	print city,
	while len(closed) < len(distance):
		i = 1
		temp = distance[city-1][i][1] + 1
		while temp in closed:
			i = i + 1
			temp = distance[city-1][i][1] + 1
		city = temp
		closed.append(city)
		print city,
	print 
	print "COst is "+str(path_sot(closed,new_distance))
