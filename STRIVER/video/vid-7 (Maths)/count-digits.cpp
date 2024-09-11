#include <bits/stdc++.h>
using namespace std;


// time complexity  = log10(n)

int main()
{
    // cout << "Hola!!!"<<endl;
    int N = 2223232;
    int n = N;
    int counts = 0;

    while (n != 0)
    {
        int temp = n % 10;
        if (temp != 0 && N % temp == 0)
        {
            counts++;
        }
        n = n / 10;
    }
    cout << counts << endl;
    return counts;
}