// 1
// 2 3 
// 4 5 6
// 7 8 9 10

#include <iostream>
using namespace std;

int main()
{
    int row = 4;

    int iter = 1;
    for (int i = 1; i <= row; i++)
    { 
        for (int j = 1; j <= i; j++)
        {
            cout << iter << " ";
            iter++;
        }
        cout<<endl;
    }

    return 0;
}