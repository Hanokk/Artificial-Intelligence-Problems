#include<stdio.h>
int main(int argc, char const *argv[])
{
	int places;
	printf("Enter the total no of places");
	scanf("%d",&places);
	int a[places][places],i,j,hash[places];
	printf("give the adjacency matrix\n");
	for (i = 0; i < places; i++)
	{
		hash[i]=0;
		for (j = 0; j < places; j++)
		{
			scanf("%d",&a[i][j]);
		}
	}
	hash[0]=1;
	printf("0\n");
	int min,next,k=0;
	for (i = 1; i < places; i++)
	{
		min=99999;
		for (j = 0; j < places; j++)
		{
			if (hash[j]==0 && j!=k && a[k][j]<min)
			{
				min=a[k][j];
				k=j;
			}
		}
		hash[k]=1;
		printf("%d\n",k);
	}
	return 0;
}
