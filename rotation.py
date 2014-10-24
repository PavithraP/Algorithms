n = int(raw_input("Enter the value of n"))
x=0
a=[[] for i in range(n)]
yArr=[i for i in range(n)]
for i in range(n):
	str1=raw_input()
	a[i] = str1.split(" ")
	a[i] = [int(j) for j in a[i]]

for i in range(n/2):
	yArr=[j for j in range(i,n-i)]
	x=i
	for y in yArr:
		if y!= -1:
			destX = i
			destY = y
			prev = a[destX][destY]
			while True:
				destAX= destY
				destAY = n-destX-1
				temp = a[destAX][destAY]
				a[destAX][destAY] = prev
				prev = temp
				destX = destAX
				destY = destAY
				if destX== x:
					yArr[destY-i]=-1
				if x==destX and y==destY:
					break


for i in range(n):
	print a[i]
