// Merge Sort
// Difficulty: MediumAccuracy: 54.1%Submissions: 191K+Points: 4
// Given an array arr[], its starting position l and its ending position r. Sort the array using merge sort algorithm.
// Example 1:

// Input:
// N = 5
// arr[] = {4 1 3 9 7}
// Output:
// 1 3 4 7 9
// Example 2:

// Input:
// N = 10
// arr[] = {10 9 8 7 6 5 4 3 2 1}
// Output:
// 1 2 3 4 5 6 7 8 9 10

// Your Task:
// You don't need to take the input or print anything. Your task is to complete the function merge() which takes arr[], l, m, r as its input parameters and modifies arr[] in-place such that it is sorted from position l to position r, and function mergeSort() which uses merge() to sort the array in ascending order using merge sort algorithm.

// Expected Time Complexity: O(nlogn) 
// Expected Auxiliary Space: O(n)

// Constraints:
// 1 <= N <= 105
// 1 <= arr[i] <= 105

// problem link = https://www.geeksforgeeks.org/problems/merge-sort/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=merge-sort 


#include<bits/stdc++.h>

using namespace std;

void merge(vector<int> &arr, int low, int mid, int high){
    vector <int> temp;

    int left = low;
    int right = mid + 1;

    while( left <= mid && right <= high){
        if(arr[left] <= arr[right]){
            temp.push_back(arr[left]);
            left++;
        } else {
            temp.push_back(arr[right]);
            right++;
        }
    }

    while(left <= mid){
        temp.push_back(arr[left]);
        left++;
    }

    while(right <= high){
        temp.push_back(arr[right]);
        right++;
    }

    for(int i = low; i <= high; i++){
        arr[i] = temp[i - low];
    }

}

void divide(vector<int> &arr, int left, int right){
    // divide part
    if(left >= right) return;

    int mid = (left+right) / 2;

    // separate left part
    divide(arr, left, mid);
    // separate right part
    divide(arr, mid + 1, right);

    // merge 
    merge(arr, left, mid, right);

}

int main(){

    cout<<"Hola!, Estudiante de Merge Sort"<<endl;
    
    // vector <int> arr = {3,2,6,4,1,2,5};o
    vector <int> arr = {1,2,1};
    cout<<"Array Before: ";
    for(auto a: arr){
        cout<<a<<" ";
    }

    divide(arr,0, arr.size() - 1);
    cout<<endl;
    cout<<"Array After: ";
    for(auto a: arr){
        cout<<a<<" ";
    }

    cout<<endl;
    return 0;    
}