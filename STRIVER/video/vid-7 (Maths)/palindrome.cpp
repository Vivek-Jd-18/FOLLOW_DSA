#include <bits/stdc++.h>
using namespace std;

// time complexity  =

bool isPalindrome(int N)
{
    int n = N;
    int pal = 0;

    while (n != 0)
    {
        int temp = n % 10;
        pal = (pal * 10) + temp;
        n = n / 10;
    }

    return (N == pal);
}

int main()
{
    int N = 123;
    cout << isPalindrome(N) << endl;
    return 0;
}