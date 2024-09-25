# Sorted Array Search
# Difficulty: BasicAccuracy: 48.03%Submissions: 270K+Points: 1
# Given an array arr[] sorted in ascending order of size N and an integer K. Check if K is present in the array or not.


# Example 1:

# Input:
# N = 5, K = 6
# arr[] = {1,2,3,4,6}
# Output: 1
# Exlpanation: Since, 6 is present in 
# the array at index 4 (0-based indexing),
# output is 1.
 

# Example 2:

# Input:
# N = 5, K = 2
# arr[] = {1,3,4,5,6}
# Output: -1
# Exlpanation: Since, 2 is not present 
# in the array, output is -1.
 

# Your Task:
# You don't need to read input or print anything. Complete the function searchInSorted() which takes the sorted array arr[], its size N and the element K as input parameters and returns 1 if K is present in the array, else it returns -1. 


# Expected Time Complexity: O(Log N)
# Expected Auxiliary Space: O(1)


# problem link: https://www.geeksforgeeks.org/problems/who-will-win-1587115621/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=who-will-win


def linear_search(arr: list[int], k:int) -> int:
    for i in range(len(arr)):
        if arr[i] == k:
            return i
    
    return -1


arr = [1,2,3,4,6]; k = 6
print(linear_search(arr, k))

arr = [1,3,4,5,6]; k = 2
print(linear_search(arr, k))