# Largest Element in Array
# Difficulty: BasicAccuracy: 67.48%Submissions: 330K+Points: 1
# Given an array, arr. The task is to find the largest element in it.

# Examples:

# Input: arr = [1, 8, 7, 56, 90]
# Output: 90
# Explanation: The largest element of the given array is 90.
# Input: arr = [5, 5, 5, 5]
# Output: 5
# Explanation: The largest element of the given array is 5.
# Input: arr = [10]
# Output: 10
# Explanation: There is only one element which is the largest.
# Expected Time Complexity: O(n)
# Expected Space Complexity: O(1)

# Constraints:
# 1 <= arr.size()<= 106
# 0 <= arr[i] <= 106


# problem link: https://www.geeksforgeeks.org/problems/largest-element-in-array4009/0?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=largest-element-in-array

def largest_ele(arr):
    large = 0
    for i in range(len(arr)):
        if arr[i]>large:
            large = arr[i]
    
    return large


arr = [3,7,8,9,4,6,99,22,123,34,5445,346]
print(largest_ele(arr))