#graph=[[]]
#path = [][]
#distance = [][]
visted=[]
n= int(raw_input("Enter the number of nodes"))
count = 0

graph=[[0 for j in range(n)] for i in range(n)]
for i in range(0, n):
	for j in range(0, n):
		graph[i][j]=int(raw_input())

i=0
while count != n-1:
	minVal = 999
	minNode =0
	for j in range(0, n):
		for k in range(0, n):
			if i!=j:
				graph[i][j] = min(graph[i][j],graph[i][k]+graph[k][j])
				graph[j][i] = min(graph[i][j],graph[i][k]+graph[k][j])
		if i!=j:
			if minVal > graph[i][j]:
				if j not in visted:
					minVal = graph[i][j]
					minNode = j
	i = minNode
	visted.append(i)
	print i
	count= count+1

print "shortest path from 1st node is"
for j in range(0, n):
	print graph[0][j],
