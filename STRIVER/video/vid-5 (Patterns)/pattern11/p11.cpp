// 1
// 0 1
// 1 0 1
// 0 1 0 1
// 1 0 1 0 1

#include <iostream>
using namespace std;

int main()
{
    int row = 4;

    int start = 1;
    for (int i = 0; i < row; i++)
    {   
        if (i%2 == 0) start = 1;
        else start = 0;
        for (int j = 0; j <= i; j++)
        {
            cout << start <<" ";
            start = 1 - start;
        }
        cout << endl;
    }

    return 0;
}