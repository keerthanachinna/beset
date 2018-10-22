#include <stdio.h>
#include<conio.h>

void main()
{
    int m=2, n=0,num;
    clrscr();
    printf("enter the number:");
    scanf("%d",&num);
    
    if(num==m*n)
    {
        printf("yes");
    }else{
        printf("no");
    }
    getch();
}
