#include "iostream"
#include "stdio.h"
#include "stdlib.h"
#include "time.h"

using namespace std;

int data[10000][3] = {0};
int pos=0;

int populator(int usrCount,float splt)
{
	srand (time(NULL));
	cout<<"Split Value = "<<splt*usrCount<<"\n";
	for (int j=0,i = pos; i <= usrCount+pos; ++i,j++)
	{
		data[i][0]=i+1;
		if(splt*usrCount <= j)
		data[i][1]=2;
		else data[i][1]=1;

		data[i][2]= rand() % 2;
	}
	pos=pos+usrCount;
}
float choicefinder()
{
	float like1=0,like2=0;

	for (int i = 1; i < pos; ++i)
	{
		if((data[i][1]==1) && (data[i][2]==1))
			like1++;
		else if((data[i][1]==2) && (data[i][2]==1))
			like2++;
	}

	return like1/(like1+like2);
}

int data_disp()
{
	for (int i = 0; i < pos; ++i)
	{
		if(data[i][0]<10)cout<<"0"<<data[i][0];
		else cout<<data[i][0];
		cout<<"     "<<data[i][1]<<"     ";
		if(data[i][2]==1)cout<<"YES\n";
			else cout<<"NO\n";
	}

	cout<<"Preference Rate\nWebpage 1 = "<<choicefinder()*100<<"\nWebpage 2 = "<<100-choicefinder()*100<<"\n";
}

int main()
{
	int data[10000][3];

	populator(500,0.5);
	data_disp();

	while(1){
	cin.get();
	populator(500,choicefinder());
	data_disp();
	}
}