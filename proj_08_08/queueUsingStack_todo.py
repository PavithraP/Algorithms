firstQueue=[]
secondQueue=[]
def pushval(val):
	if len(firstQueue) != 0:
		firstQueue.append(val);
	else:
		while len(secondQueue)!=0:
			firstQueue.append(secondQueue.pop())
		firstQueue.append(val);
	
def prnt():
	if len(firstQueue)!=0:
		print firstQueue
	else:
		print secondQueue

def pop():
	if len(firstQueue) != 0:
		while len(firstQueue)!=1:
			secondQueue.append(firstQueue.pop())
		print firstQueue.pop()
	else:
		print secondQueue.pop();	
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

