//  * * * * *
//   * * * *
//    * * *
//     * *
//      *

#include <iostream>
using namespace std;

int main()
{
    int row = 3;

    for (int i = 0; i <= row; i++)
    {
        // space
        for (int j = 0; j < i; j++)
        {
            cout << "  ";
        }
        // starts
        for (int j = 0; j < 2 * row - (2 * i + 1); j++)
        {
            cout << "* ";
        }
        // space
        for (int j = 0; j < i; j++)
        {
            cout << "  ";
        }
        cout << endl;
    }
    return 0;
}