# Quick Sort
# Difficulty: MediumAccuracy: 55.23%Submissions: 223K+Points: 4
# Quick Sort is a Divide and Conquer algorithm. It picks an element as a pivot and partitions the given array around the picked pivot.
# Given an array arr[], its starting position is low (the index of the array) and its ending position is high(the index of the array).

# Note: The low and high are inclusive.

# Implement the partition() and quickSort() functions to sort the array.

# Example 1:

# Input: 
# N = 5 
# arr[] = { 4, 1, 3, 9, 7}
# Output:
# 1 3 4 7 9
# Example 2:

# Input: 
# N = 9
# arr[] = { 2, 1, 6, 10, 4, 1, 3, 9, 7}
# Output:
# 1 1 2 3 4 6 7 9 10
# Your Task: 
# You don't need to read input or print anything. Your task is to complete the functions partition()  and quickSort() which takes the array arr[], low and high as input parameters and partitions the array. Consider the last element as the pivot such that all the elements less than(or equal to) the pivot lie before it and the elements greater than it lie after the pivot.

# Expected Time Complexity: O(N*logN)
# Expected Auxiliary Space: O(logN)

# Constraints:
# 1 <= N <= 103
# 1 <= arr[i] <= 104

# problem link: https://www.geeksforgeeks.org/problems/quick-sort/1

# def helper(arr:list[int], low:int, high:int):
#     if(low < high):
#         pivot = quick_sort(arr, low, high)

#         helper(arr, low, pivot-1)
#         helper(arr, pivot+1, high)

#     return

# def quick_sort(arr, low, high):
#     pivot = arr[low]
#     i, j = low, high

#     while i < j:
#         while arr[i] <= pivot and i < high:
#             i+=1
        
#         while arr[j] >= pivot and j > low:
#             j-=1

#         if i < j:
#             arr[i], arr[j] = arr[j], arr[i]

#     pivot, arr[j] = arr[j], pivot

#     return j


# # arr = [3,2,6,4,8,1,5]
# arr = [3,5,8,4,2,4,8,9,2,10,22,3,7,33,88,99,23]
# # arr = [3,2,6,4,8,1,5]
# print("Before: ",arr)
# helper(arr,0 , len(arr)-1)
# print("After: ",arr)





# --------------------------------------------------------  practice --------------------------------------------------------

def divider(arr:list[int], low:int, high:int):
    if(low < high):
        pivot = quick_sort(arr, low, high)

        divider(arr, low, pivot-1)
        divider(arr, pivot+1, high)

def quick_sort(arr:list[int], low, high):
    pivot = arr[low]
    i, j = low, high

    while(i < j):
        
        while(arr[i] <= pivot and i < high):
            i+=1
        
        while(arr[j] >= pivot and j > low):
            j-=1

        if(i < j):
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[j], arr[low] = arr[low], arr[j]

    return j


# arr = [2,5,8,9,3,5,1,6,9,10]
arr = [34,5,87,9,23,54,87,32,12,34,54,56,87,900,99,8,6,4,3,1,2,6,8,1]
print("Before: ")
print(arr)
divider(arr, 0, len(arr)-1)
print("After: ")
print(arr)