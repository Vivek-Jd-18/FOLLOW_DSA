// A
// BB
// CCC
// DDDD
// EEEEE

#include <iostream>
using namespace std;

int main()
{
    int row = 4;

    for (char i = 'A'; i <= row + 'A'; i++)
    {
        for (char j = 'A'; j <= i; j++)
        {
            cout << i;
        }
        cout << endl;
    }

    return 0;
}