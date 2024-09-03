#include <iostream>
using namespace std;

void takeName()
{
    cout << "Gone" << endl;
}

void passByValue(int arr[1])
{
    arr[0] += 100;
    cout << "within function: " << arr[0] << endl;
    return;
}

void passByReference(int &n)
{
    n += 10;
    cout << "within function: " << n << endl;
    return;
}

int main()
{
    // takeName();

    int arr[1] = {10};
    passByValue(arr);
    // passByReference(n);
    cout << "outside function: " << arr[0] << endl;
    return 0;
}