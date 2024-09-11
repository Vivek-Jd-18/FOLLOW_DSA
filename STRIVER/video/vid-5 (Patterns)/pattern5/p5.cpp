//   * * * *
//   * * * 
//   * *
//   *

#include <iostream>
using namespace std;

int main()
{
    int row = 5;

    for (int i = row; i >= 0; i--)
    {
        for (int j = i; j >= 0; j--)
        {
            cout <<"*"<<" ";
        }
        cout << endl;
    }
}