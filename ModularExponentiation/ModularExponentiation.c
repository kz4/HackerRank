#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

char* intToBinary(unsigned long long n);
void inplace_rev( char * s );

unsigned long long multiplyMod(unsigned long long a, unsigned long long b, unsigned long long m) {
    unsigned long long r = 0;
    a %= m;
    b %= m;
    
    while (b > 0) {
        if (b & 1){
            if (((m-r) > a))
                r = r+a;
            else
                r = r+a-m;
        }
        b >>= 1;
        if (b){
            if (((m-a) > a))
                a = a+a;
            else
                a = a+a-m;
        }
    }
    
    return r;
}

int main(int argc, const char * argv[])
{
    unsigned long long a = 0;
	unsigned long long x = 0;
	unsigned long long n = 0;
	unsigned long long result = 1;
	scanf("%llu %llu %llu",&a, &x, &n);

    char * binary = intToBinary(x);
    printf("%s\n", binary);
    
    while (x > 0){
        if (x % 2 == 1){
            //result = (result * a) % n;
            result = multiplyMod(result, a, n);
        }
        printf("%llu\n", a % n);
        x = x >> 1;
        a = multiplyMod(a, a, n);
    }
    printf("%llu\n", result);
    return 0;
}

char * intToBinary(unsigned long long temp){
    int i = 0;
    char binary[100000];
    while(temp > 0){
        binary[i++] = (temp % 2 + 48);
        temp = temp/2;
    }
    binary[i] = '\0';
    
    inplace_rev(binary);
    
    return strdup(binary);
}

void inplace_rev( char * s) {
    char t, *e = s + strlen(s);
    while ( --e > s ) { t = *s;*s++=*e;*e=t; }
}
