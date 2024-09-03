//  1 2 3 4 
//  1 2 3
//  1 2 
//  1

#include <iostream>
using namespace std;

int main()
{
    int row = 5;

    for (int i = 1; i <= row; i++)
    {
        for (int j = 1; j <=  row-i; j++)
        {
            cout <<j<<" ";
        }
        cout << endl;
    }
}