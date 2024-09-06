#include <bits/stdc++.h>
using namespace std;

int printAllDivisors(int N)
{
    int n = N;
    int sum = 0;

    for (int i = 1; i * i <= N; i++)
    {
        for (int j = 1; j * j <= N; j++)
        {
            if (i % j == 0)
            {
                sum = sum + j;
                if ((N / j) != j)
                {
                    sum = sum + j;
                }
            }
        }
    }
    return sum;
}

int main()
{
    int N = 5;
    cout << printAllDivisors(N) << endl;

    return 0;
}