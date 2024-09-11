// ********
// ***  ***
// **    **
// *      *
// *      *
// **    **
// ***  ***
// ********

// formula: 
// space (row-i)
// stuff (2*i)
// space (row-i)


#include <iostream>
using namespace std;

int main()
{
    int row = 5;

    //upper part 
    for (char i = 0; i < row; i++){
        // space
        for(int j = 0; j< row-i; j++){
            cout<<"*";
        }
        // stuff
        for(int j = 0; j< (2*i); j++){
            cout<<"-";
        }

        // space
        for(int j = 0; j< row-i; j++){
            cout<<"*";
        }

        cout<<endl;
    }

    //lower part 
    for (char i = row; i >= 0; i--){
        // space
        for(int j = 0; j< row-i; j++){
            cout<<"*";
        }
        // stuff
        for(int j = 0; j< (2*i); j++){
            cout<<"-";
        }

        // space
        for(int j = 0; j< row-i; j++){
            cout<<"*";
        }

        cout<<endl;
    }

    return 0;
}