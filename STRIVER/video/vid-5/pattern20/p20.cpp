//0 *        * -> (4-0)*2 = 8
//1 **      ** -> (4-1)*2 = 6
//2 ***    *** -> (4-2)*2 = 4
//3 ****  **** -> (4-3)*2 = 2
//4 ********** -> (4-4)*2 = 0
//5 ****  **** -> (4-3)*2 = 2
//6 ***    *** -> (4-3)*2 = 2
//7 **      ** -> (4-3)*2 = 2
//8 *        * -> (4-3)*2 = 2

// formula: 
// stuff (i+1)
// space (row-i)*2
// stuff (i+1)


#include <iostream>
using namespace std;

int main()
{
    int row = 5;

    //upper part 
    for (char i = 0; i < row; i++){
        // space
        for(int j = 0; j< (i+1); j++){
            cout<<"*";
        }
        // stuff
        for(int j = 0; j< (row-i)*2; j++){
            cout<<"-";
        }

        // space
        for(int j = 0; j< (i+1); j++){
            cout<<"*";
        }

        cout<<endl;
    }

    //lower part 
    for (char i = row; i >= 0; i--){
        // space
        for(int j = 0; j< (i+1); j++){
            cout<<"*";
        }
        // stuff
        for(int j = 0; j< (row-i)*2; j++){
            cout<<"-";
        }

        // space
        for(int j = 0; j< (i+1); j++){
            cout<<"*";
        }

        cout<<endl;
    }
    return 0;
}