//    A
//   ABA
//  ABCBA
// ABCDCBA


#include <iostream>
using namespace std;

int main()
{
    int row = 4;

    for (char i = 0; i < row; i++){

        // space
        for(int j=0; j< row-i-1; j++){
            cout<<"-";
        }

        // stuff
        char ch = 'A';
        int brk = ((2*i)+1)/2;
        for(int j=1; j<= (2*i)+1; j++){
            cout<<ch;
            if(j<=brk) ch++;
            else ch--;
        }        

        // space
        for(int j=0; j< row-i-1; j++){
            cout<<"-";
        }

        cout<<endl;
    }

    return 0;
}