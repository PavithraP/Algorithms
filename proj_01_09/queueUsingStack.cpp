#include<iostream>
#include<stdlib.h>
using namespace std;

class stack
{
	int noOfElementsFirstStack;
	int noOfElementsSecondStack;
	int *firstStack;
	int *secondStack;
public:
	void insert();
	void print();
	int push(int);
	int pop();
};
void stack::insert()
{
	cout<<"Enter the number of elements\n";
	cin>>noOfElementsFirstStack;
	firstStack=(int *)malloc(sizeof(int)*noOfElementsFirstStack);
	cout<<"Enter the elements\n";
	for(int i=0;i<noOfElementsFirstStack;i++)
		cin>>firstStack[i];
	cout<<"\n";
}
void stack::print()
{
	cout<<"Elements are\n";
	for(int i=0;i<noOfElementsFirstStack;i++)
		cout<<firstStack[i]<<" ";
	for(int i=noOfElementsSecondStack-1;i>0;i--)
		cout<<secondStack[i]<<" ";
	cout<<"\n";
	
}

int stack::push(int val)
{
	if(noOfElementsFirstStack <=0 && noOfElementsSecondStack <=0)
		return -1;

	if(noOfElementsFirstStack <=0)
	{
		noOfElementsFirstStack = 0;
		while(noOfElementsSecondStack > 0)
			firstStack[noOfElementsFirstStack++]=secondStack[--noOfElementsSecondStack];
		noOfElementsFirstStack--;
	}
	firstStack[noOfElementsFirstStack++]= val;
}

int stack::pop()
{
	if(noOfElementsFirstStack <=0 && noOfElementsSecondStack <=0)
		return -1;

	if(noOfElementsSecondStack <=0)
	{
		noOfElementsSecondStack = 0;
		while(noOfElementsFirstStack >= 0)
			secondStack[noOfElementsSecondStack++]=firstStack[noOfElementsFirstStack--];
	}
	cout<<"val is "<<secondStack[--noOfElementsSecondStack]<<"\n";
}

int main()
{
	stack stack1;
	int choice,val;
	while(1)
	{
	cout<<"Enter the choice\n1:Insert\n2:Push\n3:Pop\n4:Print\n5:Exit\n";
	cin>>choice;
	switch(choice)
	{
		case 1:	stack1.insert();break;
		case 2:	cout<<"Ente the value to push";
			cin>>val;
			stack1.push(val);break;
		case 3:	stack1.pop();break;
		case 4: stack1.print();break;
		case 5: return 0;
	}
	}
}
