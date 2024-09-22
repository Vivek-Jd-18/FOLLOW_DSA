// Quick Sort
// Difficulty: MediumAccuracy: 55.23%Submissions: 223K+Points: 4
// Quick Sort is a Divide and Conquer algorithm. It picks an element as a pivot and partitions the given array around the picked pivot.
// Given an array arr[], its starting position is low (the index of the array) and its ending position is high(the index of the array).

// Note: The low and high are inclusive.

// Implement the partition() and quickSort() functions to sort the array.

// Example 1:

// Input:
// N = 5
// arr[] = { 4, 1, 3, 9, 7}
// Output:
// 1 3 4 7 9
// Example 2:

// Input:
// N = 9
// arr[] = { 2, 1, 6, 10, 4, 1, 3, 9, 7}
// Output:
// 1 1 2 3 4 6 7 9 10
// Your Task:
// You don't need to read input or print anything. Your task is to complete the functions partition()  and quickSort() which takes the array arr[], low and high as input parameters and partitions the array. Consider the last element as the pivot such that all the elements less than(or equal to) the pivot lie before it and the elements greater than it lie after the pivot.

// Expected Time Complexity: O(N*logN)
// Expected Auxiliary Space: O(logN)

// Constraints:
// 1 <= N <= 103
// 1 <= arr[i] <= 104

// problem link: https://www.geeksforgeeks.org/problems/quick-sort/1

// #include <bits/stdc++.h>
// using namespace std;

// int quick(vector<int> &arr, int low, int high)
// {
//     int pivot = arr[low];
//     int i = low;
//     int j = high;

//     while (i < j)
//     {
//         while (arr[i] <= pivot && i < high)
//         {
//             i++;
//         }
//         while (arr[j] >= pivot && j > low)
//         {
//             j--;
//         }
//         if (i < j)
//         {
//             int temp = arr[i];
//             arr[i] = arr[j];
//             arr[j] = temp;
//         }
//     }
//     int temp2 = arr[j];
//     arr[j] = arr[low];
//     arr[low] = temp2;

//     return j;
// }

// void divider(vector<int> &arr, int low, int high)
// {
//     if (low < high)
//     {
//         int pivot = quick(arr, low, high);

//         divider(arr, low, pivot - 1);
//         divider(arr, pivot + 1, high);
//     }
// }

// int main()
// {
//     int n = 16;
//     // vector<int> arr = {2, 5, 3, 7, 4, 9, 8, 1, 2};
//     vector<int> arr = {1,2,5,32,5,7,8,43,12,54,87,9,23,124,22,9099};
//     cout << "quick sort demo: " << endl
//          << "Before: " << endl;
//     for (auto i : arr)
//     {
//         cout << i << " ";
//     }
//     cout << endl;
//     divider(arr, 0, n - 1);
//     cout << "After: " << endl;
//     for (auto i : arr)
//     {
//         cout << i << " ";
//     }
//     cout << endl;
// }

// -------------------------------------------------- practice --------------------------------------------------

#include <bits/stdc++.h>
using namespace std;

int quick(vector<int> &arr, int low, int high)
{
    int pivot = arr[low];
    int i = low;
    int j = high;

    while (i < j)
    {
        while (arr[i] <= pivot && i < high)
        {
            i++;
        }

        while (arr[j] >= pivot && j > low)
        {
            j--;
        }
        if (i < j)
        {
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }
    }
    int temp = arr[j];
    arr[j] = arr[low];
    arr[low] = temp;
    return j;
}

void divider(vector<int> &arr, int low, int high)
{
    if (low < high)
    {
        int pivot = quick(arr, low, high);

        divider(arr, low, pivot - 1);
        divider(arr, pivot + 1, high);
    }
}

int main()
{
    vector<int> arr = {3, 6, 8, 9, 3, 5, 1, 0};
    int n = arr.size();
    cout << "Array before:" << endl;
    for (auto i : arr)
    {
        cout << i << " ";
    }
    cout << endl;
    divider(arr, 0, n - 1);
    cout << "Array after:" << endl;
    for (auto i : arr)
    {
        cout << i << " ";
    }
    cout << endl;
    cout << endl;
}