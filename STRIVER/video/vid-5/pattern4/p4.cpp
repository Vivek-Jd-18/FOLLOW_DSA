//  1
//  2 2
//  3 3 3
//  4 4 4 4

#include <iostream>
using namespace std;

int main()
{
    int row = 5;

    for (int i = 1; i <= row; i++)
    {
        for (int j = 1; j <= i; j++)
        {
            cout << i<<" ";
        }
        cout << endl;
    }
}