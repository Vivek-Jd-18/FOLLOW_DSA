# Second Largest
# Difficulty: EasyAccuracy: 26.72%Submissions: 710K+Points: 2
# Given an array arr, return the second largest distinct element from an array. If the second largest element doesn't exist then return -1.

# Examples:

# Input: arr = [12, 35, 1, 10, 34, 1]
# Output: 34
# Explanation: The largest element of the array is 35 and the second largest element is 34.
# Input: arr = [10, 10]
# Output: -1
# Explanation: The largest element of the array is 10 and the second largest element does not exist so answer is -1.
# Expected Time Complexity: O(n)
# Expected Auxiliary Space: O(1)

# Constraints:
# 2 ≤ arr.size() ≤ 105
# 1 ≤ arri ≤ 105

# problem link:     https://www.geeksforgeeks.org/problems/second-largest3735/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=second-largest


def second_largest_ele(arr):
    largest, second_largest = arr[0], -1

    for i in range(len(arr)):
        if arr[i] > largest:
            largest, second_largest = arr[i], largest
        if arr[i] > second_largest and arr[i] < largest:
            second_largest = arr[i]
    
    return second_largest

# arr = [3,6,8,4,9,10,3,56,34,78]
# arr = [2,4,6,8,9,3,1]
# arr = [12, 35, 1, 10, 34, 1]
arr = [12, 35, 1, 10, 34, 1]
print(second_largest_ele(arr))