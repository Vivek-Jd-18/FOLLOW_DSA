// ABCDE
// ABCD
// ABC
// AB
// A

#include <iostream>
using namespace std;

int main()
{
    int row = 4;

    for (int i = row; i >= 0; i--)
    { 
        for (char j = 'A'; j<= 'A'+ i; j++){
            cout<<j;
        }
        cout<<endl;
    }

    return 0;
}