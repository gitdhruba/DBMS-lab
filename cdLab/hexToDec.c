// C program to demonstrate hexadecimal to decimal 
// conversion using format specifier 

#include <stdio.h> 

int main() 
{ 

	int n; 
	// taking input from user
    long arr[8][5]=
{
{0x7fffffffd6c0, 0x00000000,      0x00000000 ,     0x00000000,      0x00007fff},
{0x7fffffffd6d0, 0x00000000,      0x00007fff ,     0xb72ca000,      0x82f6cbcd},
{0x7fffffffd6e0, 0xffffffff,      0x00000000 ,     0x00000400,      0x00000000},
{0x7fffffffd6f0, 0x00000400,      0x00000000 ,     0xf7ca52d5,      0x00007fff},
{0x7fffffffd700, 0x00000000,      0x00000000 ,     0x00000000,      0x00000000},
{0x7fffffffd710, 0x00000400,      0x00000000 ,     0xf7e1b780,      0x00007fff},
{0x7fffffffd720, 0x00000d68,      0x00000000 ,     0xf7c7eba4,      0x00007fff},
{0x7fffffffd730, 0x00000018,      0x00000000 ,     0x00000004,      0x00000000}};
	// printing the decimal number 
    for (int i = 0; i < 8; i++)
    {
        for (int j = 0; j < 5; j++)
        {
            printf("%ld ", arr[i][j]);
        }
        printf("\n");
    }
    
	 
	return 0; 
}
