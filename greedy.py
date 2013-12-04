def path_sot(path,distance):
	src = path[0]
	cost = 0
	for i in range(0,len(path)):
		dest = path[i]
		cost = cost + distance[src-1][dest-1]
	return cost

def edge_list(distance):
	edge = []
	for row in distance:
		for item in row:
			if item[1] is not item[0]:
				if (item[1],item[0],distance) not in edge:
					edge.append(item)
	edge.sort(key = lambda x:x[2])
	return edge
	
def show_path(path):
	print str(path[0]),
	for i in range(1,len(path)):
		print "->"+str(path[i]),
	print "" 

def merge_path(path1,path2):
	new_path = []
	for item in path1:
		new_path.append(item)
	for item in path2:
		new_path.append(item)
	return new_path

def check_cycle(path):
	closed = []
	for city in path:
		if city in closed:
			return False
		else:
			closed.append(city)
	return True

def update_tour(partial_tours,edge):
	city1 = edge[0]+1
	city2 = edge[1]+1
	temp1 = []
	for i in range(len(partial_tours)):
		if city1  in partial_tours[i]:
			break
	for j in range(len(partial_tours)):
		if city2  in partial_tours[j]:
			if j is not i:
				break
	city1_pos = len(partial_tours[i])-1
	city2_pos = 0
	if city1 is not partial_tours[i][city1_pos] and city2 is not partial_tours[j][city2_pos]:
		if city1 not in partial_tours[i] and city2 not in partial_tours[j]:
			temp1 = [city1,city2]
	if city1 is partial_tours[i][city1_pos]:
		if city2 is partial_tours[j][city2_pos]:
			if j is not i:
				temp1 = merge_path(partial_tours[i],partial_tours[j])
				path1 = partial_tours[i]
				path2 = partial_tours[j]
				partial_tours.remove(path1)
				partial_tours.remove(path2)
		else:
			if city2 not in partial_tours[j]:
				temp1 = merge_path(partial_tours[i],[city2])
				path1 = partial_tours[i]
				partial_tours.remove(path1)
	elif city2 is partial_tours[j][city2_pos]:
		if city1 is not partial_tours[i][city1_pos]:
			if city1 not in partial_tours[i]:
				temp1 = merge_path([city1],partial_tours[j])
				path2 = partial_tours[j]
				partial_tours.remove(path2)
	if len(temp1) is not 0:
		partial_tours.append(temp1)
	return partial_tours

def greedy(cities,distance,new_distance):
	edges = edge_list(distance)	
	result = []
	while len(edges) > 0:
		for item in result:
			if len(item) is cities:
				break
		edge = edges[0]
		city1 = edge[0]+1
		city2 = edge[1]+1
		print "Edge being considered"
		print str(city1) +"->"+str(city2)
		edges.remove(edges[0])
		if len(result) is 0:
			result.append([edge[0]+1,edge[1]+1])
		else:
			result = update_tour(result,edge)
		for item in result:
			show_path(item)
	print result
	print "The best path is"
	for item in result:
		if len(item) is cities:
			show_path(item)
			temp = item
			break
	print "Cost of tour is "+str(path_sot(temp,new_distance))
