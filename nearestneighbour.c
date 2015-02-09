#include<stdio.h>
int main(int argc, char const *argv[])
{
	int places;
	printf("Enter the total no of places");
	scanf("%d",&places);
	int a[places][places],i,j,hash[places];
	printf("give the adjacency matrix\n");
	for(i=0;i<places;i++)
	{

		hash[i]=0;
}
	for (i = 0; i < places; i++)
	{
		for (j = 0; j < places; j++)
		{
			scanf("%d",&a[i][j]);
		}
	}
	hash[0]=1;
	printf("0\n");
	int min,next=0,k=0;
	for (i = 1; i < places; i++)
	{
		min=99999;
		for (j = 0; j < places; j++)
		{
			if ((hash[j]==0) && (a[k][j]!=0) && (a[k][j]<min))
			{
				min=a[k][j];
				next=j;
				k=j;
				hash[j]=1;
			}
		}
		printf("%d\n",next);
	}
	return 0;
}
