// 1 - - - - - - 1
// 1 2 - - - - 2 1
// 1 2 3 - - 3 2 1
// 1 2 3 4 4 3 2 1

#include <iostream>
using namespace std;

int main()
{
    int row = 4;

    for (int i = 1; i <= row; i++)
    {

        // layer 1
        for (int j = 1; j <= i; j++)
        {
            cout << j;
        }

        // layer 2
        for (int j = 1; j <= 2 * (row - i); j++)
        {
            cout << " ";
        }

        // layer 3
        for (int j = i; j >= 1; j--)
        {
            cout << j ;
        }
        cout << endl;
    }

    return 0;
}