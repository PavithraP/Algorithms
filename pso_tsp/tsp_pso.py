from random import randint
import math
graph = [[0,2,-1,12,5],
	[2,0,4,4,-1],
	[-1,4,0,3,3],
	[12,4,3,0,10],
	[5,-1,3,10,0]]

noOfParticles = 20
noOfCities = 5
particle=[[] for i in range(noOfParticles)]
def initiateParticles():
	i = 0
	while i < noOfParticles:
		temp_graph = [[0,2,-1,12,5],
			[2,0,4,4,-1],
			[-1,4,0,3,3],
			[12,4,3,0,10],
			[5,-1,3,10,0]]
		count = 0
		no = randint(0,4)
		temp = no
		particle[i]=[]
		particle[i].append(no)
		while count < noOfCities-1:
			no = randint(0,4)
			if no not in particle[i] and graph[temp][no]!= -1 and graph[temp][no]!= 0:
				for k in range(noOfCities):
					temp_graph[temp][k] = 0
					temp_graph[k][temp] = 0 
				particle[i].append(no)
				temp = no
				count += 1
			elif temp_graph[temp].count(0)+temp_graph[temp].count(-1) == noOfCities:
				i -= 1
				break;
		i += 1

def costCalculation(particle):
	cost = 0
	for i in range(noOfCities-1):
		cost += graph[particle[i]][particle[(i+1)]]
	return cost

def check(part, source ,dest):
	source = int(source)%noOfCities
	dest = int(round(dest,0))%noOfCities
	if source > dest:
		tmp = source
		source = dest
		dest = tmp
	elif source == dest:
		return 0
	if graph[part[dest]][part[source+1]] != -1 :
		if graph[part[source]][part[dest-1]] != -1 :
			if source-1 < 0:
				if dest+1 >= noOfCities:
					return 1
				elif graph[part[source]][part[dest+1]] != -1 :
					return 1
				else:
					return 0	
			elif graph[part[dest]][part[source-1]] != -1:
				if dest+1 >= noOfCities:
					return 1
				elif graph[part[source]][part[dest+1]] != -1 :
					return 1
				else:
					return 0	
			else:
				return 0	
	else:
		return 0	
				  	
def swap(part, source ,dest):
	source = int(source)%noOfCities
	dest = int(round(dest,0))%noOfCities
	#print "part=",part,source,dest
	tmp = part[source]
	part[source] = part[dest]
	part[dest] = tmp
	return part

pRandom = 0.9
pPbest = 0.05
pGbest = 0.05
pBest = [999.0 for i in range(noOfParticles)]
v = [1 for i in range(noOfParticles)]
gBest = 999.0

initiateParticles()
print particle 

for i in range(noOfParticles):
	present = costCalculation(particle[i])
	if present < pBest[i]:
		pBest[i] = present
	if present < gBest:
		gBest = present
iterations = 1000
change = 0
flag = 0

while( iterations > 0):
	merged = 0
	for i in range(noOfParticles):
		cost = costCalculation(particle[i])
		print "before change =",particle[i],"cost =",pBest[i]
		prevV = v[i]
		v[i] = pRandom * v[i] + pPbest * (pBest[i] - cost) + pGbest * (gBest - cost)
		isSwappable = check(particle[i],prevV,(prevV+v[i]))
		if isSwappable == 1:
			temp_part = swap(particle[i],prevV,(prevV+v[i]))
			cost = costCalculation( temp_part )
			if cost < pBest[i]:
				particle[i] = temp_part
				pBest[i] = cost
				print "after change =",particle[i],"cost =",cost
				change += 1
			if cost < gBest:
				gBest = cost
		if gBest == pBest[i]:
			merged += 1
		print "\n"
		
	print "merged",merged
	if merged > noOfParticles / 2:
		iterations = 0
	pRandom *= 0.95
	pPbest *= 1.01
	pGbest = 1 - (pRandom + pPbest) 
	flag += 1
	print "change***************",change

print change
print "flag =",flag
