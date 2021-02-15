#include <stdio.h>

int funtop(int a, int b, char *s)
{
    int sum;
    sum=a+b;
    printf("a+b is %d\n",sum);
    while(1)
    {
        sleep(1);
    }
}
int main (int argc,char*argv[])
{
    unsigned long stacktop;
    stacktop=(unsigned long)argv;
    stacktop+=4096;
    stacktop&=~0xfff;
    fprintf(stderr,"StackAtMain=%16p,next page=%016lx\n",argv,stacktop);
    fprintf(stderr,"Mypid=%d\n",getpid());
    funtop(4,5,"hi");
}
