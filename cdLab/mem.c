#include<stdio.h>
int main(){
    int * ptr = (int *) malloc(1e9);
    free(ptr);
    *ptr =10;
    return 0;
}

