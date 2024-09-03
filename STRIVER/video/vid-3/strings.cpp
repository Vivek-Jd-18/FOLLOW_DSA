#include <iostream>
using namespace std;

int main()
{
    string name = "Lewandowski";
    int len = name.size();
    cout << name << endl;
    name[len - 1] = 'a';

    cout << name;
    cout << endl;
    return 0;
}