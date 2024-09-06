// You are given a 3-digit number n, Find whether it is an Armstrong number or not.

// An Armstrong number of three digits is a number such that the sum of the cubes of 
// its digits is equal to the number itself. 371 is an Armstrong number since 33 + 73 + 13 = 371. 

// Examples

// Input: n = 153
// Output: true
// Explanation: 153 is an Armstrong number since 13 + 53 + 33 = 153. Hence answer is "true".

// Input: n = 372
// Output: false
// Explanation: 372 is not an Armstrong number since 33 + 73 + 23 = 378. Hence answer is "false".


#include <bits/stdc++.h>
using namespace std;

// time complexity  =

bool isArmstrong(int N)
{
    int n = N;
    int arm = 0;

    while (n != 0)
    {
        int temp = n % 10;
        arm = arm + (temp*temp*temp);
        n = n / 10;
    }
    cout<<arm<<endl;
    return (N == arm);
}

int main()
{
    int N = 153;
    cout << isArmstrong(N) << endl;
    return 0;
}