#include <bits/stdc++.h>
using namespace std;

int printAllDivisors(int N)
{
    int n = N;
    int sum = 0;

    for (int i = 1; i <= N; i++)
    {   
        int local_sum = 0;
        for (int j = 1; j * j <= i; j++)
        {
            if (i % j == 0)
            {
                local_sum += j;
                if ((i / j) != j)
                {
                    local_sum += i/j;
                }
            }
        }
        sum += local_sum;
    }
    return sum;
}

int main()
{
    int N = 5;
    cout << printAllDivisors(N) << endl;

    return 0;
}