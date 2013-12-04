def path_sot(path,distance):
	src = path[0]
	cost = 0
	for i in range(0,len(path)):
		dest = path[i]
		cost = cost + distance[src-1][dest-1]
	return cost

def show_tour(path):
	string = ""
	string = string + str(path[0])
	for i in range(1,len(path)):
		string = string +"->"+str(path[i])
	return string

def merge(tour1,tour2):
	print "Merging tours"
	string = show_tour(tour1) +" , "+show_tour(tour2)
	print string
	new_path = []
	for i in range(0,len(tour1)-1):
		new_path.append(tour1[i])
	for i in range(1,len(tour2)):
		new_path.append(tour2[i])
	string = show_tour(new_path)
	print string
	return new_path

def select_edge(no_of_cities,base,distance):
	select_order = []
	for i in range(no_of_cities):
		if (i+1) is not base:
			for j in range(no_of_cities):
				if j is not i and j+1 is not base:
					savings = distance[base-1][i]+distance[base-1][j]-distance[i][j]
					temp = (i+1,j+1,savings)
					temp1 = (j+1,i+1,savings)
					if temp1 not in select_order:
						select_order.append(temp)
	select_order.sort(key= lambda x:x[2])
	select_order.reverse()
	return select_order

def savings_heuristic(base,no_of_cities,distance):
	tours = []
	result = []
	order = select_edge(no_of_cities,base,distance)
	while len(result) < (no_of_cities+1):
		choice = order[0]
		order.remove(order[0])
		if len(result) is 0:
			tour1 = [base,choice[0],base]
			tour2 = [base,choice[1],base]
		else:
			tour1 = result
			if (choice[0] in result and choice[1] in result) or (choice[0] not in result and choice[1] not in result):
				continue
			if choice[0] in result:
				if choice[1] not in result:
					tour2 = [base,choice[1],base]
			elif choice[1] in result:
				if choice[0] not in result:
					tour2 = [base,choice[0],base]
		result = merge(tour1,tour2)
	print "Best path is"
	for i in range(0,len(result)-1):
		print result[i],
	print 
	print "Cost of path "+str(path_sot(result,distance))
