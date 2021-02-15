#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define BUFFSIZE 100



int main(int argc, char *argv[])
{
  
  char*pAllocated1 =(char*) malloc (BUFFSIZE );
  char*pAllocated2 = (char*) malloc (BUFFSIZE );
  char*pAllocated3 = (char*) malloc (BUFFSIZE );
   // allocate one page
  printf("First  memory block allocated 0x%p\n", pAllocated1);
  printf("Second memory block allocated 0x%p\n", pAllocated2);
  printf("Third  memory block allocated 0x%p\n", pAllocated3);
  strcpy(pAllocated2,"BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB");
  free(pAllocated2);

}