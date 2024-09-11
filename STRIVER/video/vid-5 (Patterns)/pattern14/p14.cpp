// A
// AB
// ABC
// ABCD
// ABCDE

#include <iostream>
using namespace std;

int main()
{
    int row = 4;

    for (int i = 0; i <= row; i++)
    { 
        for (char j = 'A'; j<= 'A'+ i; j++){
            cout<<j;
        }
        cout<<endl;
    }

    return 0;
}