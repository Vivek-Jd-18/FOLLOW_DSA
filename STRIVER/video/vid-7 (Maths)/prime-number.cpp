#include <bits/stdc++.h>
using namespace std;

bool isPrimeOrNot(int N)
{

    int count = 0;

    for (int i = 1; i * i <= N; i++)
    {
        if (N % i == 0)
        {
            count++;
            if ((N / 1 != i))
            {
                count++;
            }
        }
    }
    if (count == 2)
    {
        return 1;
    }
    return 0;
}

int main()
{
    int N = 5;
    cout << isPrimeOrNot(N) << endl;
    return 0;
}
