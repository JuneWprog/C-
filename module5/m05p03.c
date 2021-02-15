#include <stdio.h>
#include<string.h>
#include<stdlib.h>
/*Problem 3:
Write short program in C, m05p03.c, which will contain 3 functions with following prototypes:
int main(int argc, char **argv[]);
int funtop(int a, int b, char *str);
int funbot(int a, int b, char *str);
main() will call funtop(), with parameter values you choose. funtop() will multiply its integer
parameters by some constant you choose, and call funbot(). It will simply return the result of funbot().
funbot() will print the str, add the two integer parameters together and return the result.
Each function will print its location in memory. The innermost function will print the contents of the
stack, everything from current stack position to the top of the stack. Hint: to find top of the stack, read
file /proc/[pid]/maps, look for [stack].
*/


// to use asm functions (assembly code)
extern int asmfunc();

int funbot(int a, int b, char *str);
//function get sp 16-bit/esp 32-bit/rsp 64-bit
unsigned long long *getsp( void )
{
    unsigned long long * rsp;
   
    asm ("movq %%rsp, %0" : "=r" (rsp) );
    
    return rsp;
}


int funtop(int a, int b, char *str)
{
    a=a*2;
    b=b*9;
    
    int fun=funbot(a,b,str);
    return fun;
}
int funbot(int a,int b, char *str)
{   
    unsigned long long sum=a+b;
    
    unsigned long long * p;

    char fname[30];
    int pid =getpid();
    printf("Mypid=      %d\n",pid);
    sprintf(fname,"/proc/%d/maps",pid);     //to pid value in the file path
    //printf("filename:   %s\n",fname);      
    FILE *file = fopen(fname, "r");
    char line[256];
    char * token1;
    char * token2;
    while (fgets(line, sizeof(line), file))    //read file to 256-character-long lines 
    {
    if (strstr(line, "stack") != NULL) {        //looking for substring-- find the line contains substring "stack" 
        token1=strtok(line,"-");                //split line (string) to 2 substring, substr1=token1, substr2=NULL 
        //printf("%s\n",token1);                  //token1 = the first substring before "-" 
        token2=strtok(NULL," ");                 //split substring NULL, take 1st subsubstring before space 
        //printf("stacktop:   %s\n",token2);
        break;
        }
    }
    fclose(file);
    unsigned long long ultoken1;
    sscanf(token1, "%llx", &ultoken1);                  //cast char* to ull
    unsigned long long ultoken2;
    sscanf(token2,"%llx",&ultoken2);
    //unsigned long long* stackbase=(unsigned long long *)ultoken1;   //cast ull to ull pointer
    unsigned long long* stacktop=(unsigned long long *)ultoken2;

    //printf("p: %p,\n",p);
    unsigned long long *p1=getsp();                   //get the current stack pointer (sp/esp/rsp)
    //printf("rsp=        %p\n",p1);
    int j;
    char character;
    for (p=p1;p<stacktop;p++){                        //print stack from current sp to stacktop         
        printf ("%p    0x%016x      ",p,*p);
        for(j=0;j<64;j+=8)
	    {
	        character=(*p>>j)&(0xff);
	        printf("%c",character);
	    } 
      printf("\n");

    }
    printf ("%s\n",str);
    printf("At Fun_top: %p\n",funtop);
    printf("At Fun_bot: %p\n",funbot);
    printf("stacktop:   %s\n",token2);
    printf("rsp=        %p\n",p1);

    return sum;
} 

int main (int argc, char* argv[])
{    
    
    funtop(5,3,"nice!");
    printf("At Main:    %p\n",main);
    

return 0;
}