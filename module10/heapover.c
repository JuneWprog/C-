#include<stdio.h>
#include<string.h>
#include<stdlib.h>

#define BUFSIZE 1

int main(int argc, char **argv) {
char *buf = malloc(BUFSIZE);
printf("the address of buf %p\n", buf);
strcpy(buf,argv[1] );
free(buf);
}