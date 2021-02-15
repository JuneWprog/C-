#include <stdio.h>
#include<string.h>
#include<stdlib.h>


int funbot(int a, int b, char *str);

int funtop(int a, int b, char *str)
{
    a=a*2;
    b=b*9;
    
    int fun=funbot(a,b,str);
    return fun;    
}
int funbot(int a, int b, char *str)
{   printf ("%s\n",str);
    int sum=a+b;
    unsigned long long *p;

    char fname[30];
    printf("At Fun_top: %p\n",funtop);
    printf("At Fun_bot: %p\n",funbot);
    
    int pid =getpid();
    printf("Mypid=%d\n",pid);
    sprintf(fname,"/proc/%d/maps",pid);
    printf("fname %s\n",fname);
    FILE *file = fopen(fname, "r");
    char line[256];
    char * token1;
    char * token2;
    while (fgets(line, sizeof(line), file)) 
    {
    if (strstr(line, "stack") != NULL) {
        
        printf("%s",line);
        token1=strtok(line,"-");
        token2=strtok(NULL," ");
        printf("top:%s\n",token2);
        break;
        }
    }
    fclose(file);
    unsigned long long ultoken1;
    sscanf(token1, "%llx", &ultoken1);
    unsigned long long ultoken2;
    sscanf(token2,"%llx",&ultoken2);
    unsigned long long * stackbase=(unsigned long long *)ultoken1;
    unsigned long long * stacktop=(unsigned long long*)ultoken2;

    int i, j, myval;
    char character;
    for (p=&a;p<stacktop;p++){
        printf ("%p    0x%016x     ",p,*p);
        for(j=0;j<64;j+=8)
	    {
	        character=(*p>>j)&(0xff);
	        //if (character<='Z'&& character>='A' ||character>='a' && character<='z')
	        printf("%c",character);
	    } 
      printf("\n");

    }
    return sum;
} 

int main (int argc, char* argv[])
{    
    funtop(5,3,"nice!");
    printf("At    Main: %p\n",main);

return 0;
}