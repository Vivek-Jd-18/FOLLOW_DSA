//      *
//     * *
//    * * *
//   * * * *
//  * * * * *

#include <iostream>
using namespace std;

int main()
{
    int row = 5;

    for (int i = 0; i < row; i++)
    {
        // space
        for (int j = 0; j < row-i-1; j++)
        {
            cout<<" ";
        }
        // starts
        for (int j = 0; j < 2*i+1; j++)
        {
            cout<<"*";
        }
        // space
        for (int j = 0; j < row-i-1; j++)
        {
            cout<<" ";
        }
        cout<<endl;
    }
    return 0;
}