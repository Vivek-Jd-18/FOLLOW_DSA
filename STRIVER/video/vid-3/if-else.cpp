#include <iostream>
using namespace std;

int main()
{
    int age;
    cout << "Enter your age: ";
    cin >> age;

    if (age >= 100)
    {
        cout << "are you still alive?, but how and why?" << endl;
        return 0;
    }
    if (age < 18)
    {
        cout << "Not eligible to vote";
    }
    else
    {
        cout << "Eligible to vote";
    }
    cout << endl;
    return 0;
}