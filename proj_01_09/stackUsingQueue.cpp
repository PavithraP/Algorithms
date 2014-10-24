#include<iostream>
#include<stdlib.h>
using namespace std;

class queue
{
	int firstQueueFront;
	int firstQueueBack;
	int secondQueueFront;
	int secondQueueBack;
	int *firstQueue;
	int *secondQueue;
public:
	void insert();
	void print();
	int push(int);
	int pop();
};
void queue::insert()
{
	cout<<"Enter the number of elements\n";
	firstQueueFront = 0;
	secondQueueFront = 0;
	secondQueueBack = -1;
	cin>>firstQueueBack;
	firstQueue=(int *)malloc(sizeof(int)*firstQueueBack);
	secondQueue=(int *)malloc(sizeof(int)*firstQueueBack);
	cout<<"Enter the elements\n";
	for(int i=0;i<firstQueueBack;i++)
		cin>>firstQueue[i];
	cout<<"\n";
}
void queue::print()
{
	cout<<"Elements are\n";
	for(int i=firstQueueFront;i<firstQueueBack;i++)
		cout<<firstQueue[i]<<" ";
	for(int i=secondQueueFront;i<secondQueueBack;i++)
		cout<<secondQueue[i]<<" ";
	cout<<"\n";
	
}

int queue::push(int val)
{
	if(firstQueueFront>firstQueueBack && secondQueueFront >secondQueueBack)
		return -1;

	if(firstQueueFront > firstQueueBack)
		secondQueue[secondQueueBack++]=val;
	else
		firstQueue[firstQueueBack++]=val;

}

int queue::pop()
{

	if(firstQueueFront>firstQueueBack && secondQueueFront >secondQueueBack)
		return -1;

	if(firstQueueFront > firstQueueBack)
	{
		firstQueueFront = 0;
		firstQueueBack = 0;
		while(secondQueueFront <= secondQueueBack)
			firstQueue[firstQueueBack++]=secondQueue[secondQueueFront++];
	--firstQueueBack;
	cout<<"val is "<<firstQueue[--firstQueueBack]<<"\n";
	}
	else
	{
		secondQueueFront = 0;
		secondQueueBack = 0;
		while(firstQueueFront <= firstQueueBack)
			secondQueue[secondQueueBack++]=firstQueue[firstQueueFront++];
	--secondQueueBack;
	cout<<"val is "<<secondQueue[--secondQueueBack]<<"\n";
	}

}

int main()
{
	queue queue1;
	int choice,val;
	while(1)
	{
	 cout<<"Enter the choice\n1:Insert\n2:Push\n3:Pop\n4:Print\n5:Exit\n";
	cin>>choice;
	switch(choice)
	{
		case 1:	queue1.insert();break;
		case 2:	cout<<"Ente the value to push";
			cin>>val;
			queue1.push(val);break;
		case 3:	queue1.pop();break;
		case 4: queue1.print();break;
		case 5: return 0;
	}
	}
}
