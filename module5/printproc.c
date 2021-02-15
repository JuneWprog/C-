#include <stdio.h>

void printproc(char state, int ppid, int pgid, unsigned long long mm_start_code, unsigned long long mm_end_code, unsigned long long mm_start_stack, unsigned long long esp, unsigned long long eip)
{
    printf("State:   %21c\n",state);
    printf("ParentPid:%20d\n",ppid);
    printf("ParentGid:%20d\n",pgid);
    printf("StartCode:  0x%016lx\n",mm_start_code);
    printf("EndCode:    0x%016lx\n",mm_end_code);
    printf("StartStack: 0x%016lx\n",mm_start_stack);
    printf("ESP:        0x%016lx\n",esp);
    printf("EIP:        0x%016lx\n",eip);

}