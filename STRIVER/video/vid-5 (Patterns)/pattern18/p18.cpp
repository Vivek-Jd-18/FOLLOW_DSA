// E
// D E
// C D E
// B C D E
// A B C D E 

#include <iostream>
using namespace std;

int main()
{
    int row = 5;

    for (char i = 0; i < row; i++){

        char ch = (row-i-1)+'A';
        for(int j = 0; j<= i; j++){
            cout<<ch<<" ";
            ch++;
        }
        cout<<endl;
    }

    return 0;
}