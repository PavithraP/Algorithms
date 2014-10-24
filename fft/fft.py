from cmath import exp, pi
import math
def fft(x,n,s):
	if n==1:
		return x
#	print "dividing",x,x[0::2],x[1::2]
	even = fft(x[0::2],n/2,s)
#	if len(even) == 2:
	print "print in even",even
	odd = fft(x[1::2],n/2,s)
	print "odd",odd
#	for k in range(s-1):
#		w=math.floor(math.cos(-2*pi*k/4))+1j*math.sin(-2*pi*k/4)
#		even[k]=even[k]+w*odd[k]
#		odd[k]=even[k]-w*odd[k]
#	w=math.floor(math.cos(-2*pi*s/4))+1j*math.sin(-2*pi*s/4)
#	return [even[s]+w*odd[s]]
	return [even[k]+exp(-2j*pi*k/8)*odd[k] for k in range(n/2)]+[even[k]-exp(-2j*pi*k/8)*odd[k] for k in range(n/2)]
	#return [even[k]+math.cos(2*pi*k/8)+1j*math.sin(-2*pi*k/8)*odd[k] for k in range(n/2)]+[even[k]-math.cos(2*pi*k/8)+1j*math.sin(-2*pi*k/8)*odd[k] for k in range(n/2)]
 
 
#*exp(-2j*pi*s/n)]
#print f for f in fft(x,8,1)
#print( ' '.join("%f" % abs(f) 
#               for f in fft([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0],8,1)) )
#for k in range(8):
#	print x[k]
print fft([0.0, 1.0, 2.0, 3.0,4.0,5.0,6.0,7.0],8,0)
#print fft([0.0, 1.0, 2.0, 3.0],4,1)
#print fft([1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0],8,1)


