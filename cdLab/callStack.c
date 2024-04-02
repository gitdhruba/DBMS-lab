#include <stdio.h>

int factorial(int n) {
      return ((n>0)? (n * factorial(n-1)) :1);
}

int fibbonacci(int n) {
   if(n == 0 || n == 1) 
      return n;
   else 
      return (fibbonacci(n-1) + fibbonacci(n-2));
}

int main() {
   int n = 5;
   int i;
	
   printf("Factorial of %d: %d\n" , n , factorial(n));
   printf("Fibbonacci of %d: " , n);
	
   for(i = 0;i<n;i++) {
      printf("%d ",fibbonacci(i));            
   }
}

