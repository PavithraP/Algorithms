from collections import deque
firstQueue=deque([])
secondQueue=deque([])
def pushval(val):
	if len(secondQueue) != 0:
		secondQueue.append(val)
	else:
		firstQueue.append(val)
	
def prnt():
	if len(firstQueue)!=0:
		print firstQueue
	else:
		print secondQueue

def pop():
	if len(firstQueue)!=0:
		while len(firstQueue)!=1:
			secondQueue.append(firstQueue.popleft())
		print firstQueue.popleft()
	else :
		while len(secondQueue)!=1:
			firstQueue.append(secondQueue.popleft())
		print secondQueue.popleft()
	
while True:
	print "Enter the choice"
	choice = int(raw_input())
	if choice == 1:
		pushval(int(raw_input("Enter the value")))		
	if choice == 2:
		pop()
	if choice == 3:
		prnt()
	if choice == 4:
		break;

