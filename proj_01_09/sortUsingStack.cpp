#include<iostream>
#include<stdlib.h>
using namespace std;

class stack
{
	int noOfElements;
	int *stackElements;
public:
	void insert();
	void print();
	int sort();
};
void stack::insert()
{
	cout<<"Enter the number of elements\n";
	cin>>noOfElements;
	stackElements=(int *)malloc(sizeof(int)*noOfElements);
	cout<<"Enter the elements\n";
	for(int i=0;i<noOfElements;i++)
		cin>>stackElements[i];
	cout<<"\n";
}
void stack::print()
{
	cout<<"Elements are\n";
	for(int i=0;i<noOfElements;i++)
		cout<<stackElements[i]<<" ";
	cout<<"\n";
}

int stack::sort()
{       int tempNo=0;
	if(noOfElements <=0 )
		return -1;
	int *tempStack=(int *)malloc(sizeof(int)*noOfElements);
	noOfElements--;
	while(noOfElements >0 )
	{
		if(stackElements[noOfElements] > stackElements[noOfElements -1])
		{
			tempStack[tempNo++]=stackElements[noOfElements-1];
			stackElements[noOfElements-1]=stackElements[noOfElements];
			int storedNoOfElements=tempNo;
			int valAdded=tempStack[tempNo-1];
			if(valAdded<tempStack[tempNo-2])
			{
				tempNo--;
				while(valAdded < tempStack[tempNo-1] && tempNo > 0)
				{
					stackElements[++noOfElements]=tempStack[tempNo-1];
					tempNo--;
				}
				tempStack[tempNo++]=valAdded;
				for(int i=tempNo;i<storedNoOfElements;i++)
				tempStack[tempNo++]=stackElements[noOfElements--];
			}
		}
		else
			{
			tempStack[tempNo++]=stackElements[noOfElements];
			
			int storedNoOfElements=tempNo;
			int valAdded=tempStack[tempNo-1];
			if(valAdded<tempStack[tempNo-2])
			{
				tempNo--;
				while(valAdded < tempStack[tempNo-1] && tempNo > 0)
				{
					stackElements[++noOfElements]=tempStack[tempNo-1];
					tempNo--;
				}
				tempStack[tempNo++]=valAdded;
				for(int i=tempNo;i<storedNoOfElements;i++)
				tempStack[tempNo++]=stackElements[noOfElements--];
			}
			}
		noOfElements--;
	}
	tempStack[tempNo]=stackElements[0];
	noOfElements = tempNo+1;
	for(int i=0;i<noOfElements;i++)
		stackElements[i]=tempStack[i];
}
int main()
{
	stack stack1;
	stack1.insert();
	stack1.print();
	stack1.sort();
	stack1.print();
}
