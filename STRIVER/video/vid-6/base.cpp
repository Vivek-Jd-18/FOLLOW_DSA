// C++ STL divided into:
// 1)Algorithms
// 2)Containers
// 3)Functions
// 4)Iterators


#include <iostream>
using namespace std;

int main()
{
    pair <int, int> p = {1,2};
    cout << p.first << p.second <<endl;


    pair <int, pair <int, int>> p2 = {1,{2,3}};
    cout << p2.first << p2.second.first << p2.second.second << endl;

}