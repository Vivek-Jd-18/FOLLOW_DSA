#include <bits/stdc++.h>
using namespace std;

// time complexity  = O(log(x))

int rev_number(int N)
{
    int n = N;
    long long int rev_num = 0;

    if (N < 0)
        n = -n;

    while (n != 0)
    {
        int temp = n % 10;
        rev_num = (rev_num * 10) + temp;
        n = n / 10;
    }

    if (rev_num > INT_MAX || rev_num < INT_MIN)
        return 0;

    if (N < 0)
        return -rev_num;
    else
        return rev_num;
}

int main()
{
    int N = 123;
    cout << rev_number(N) << endl;
    return 0;
}