# 53. Maximum Subarray
# Medium
# Topics
# Companies
# Given an integer array nums, find the 
# subarray
#  with the largest sum, and return its sum.

 

# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.
# Example 2:

# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.
# Example 3:

# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
 

# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
 

# Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.


# problem link: https://leetcode.com/problems/maximum-subarray/description/

# def better(arr:list[int]):
#     _max = 0
#     for i in range(len(arr)):
#         _sum = 0
#         for j in range(i, len(arr)):
#             _sum+=arr[j]
#             _max = max(_max, _sum) 
    
#     return _max


# # Example 1:
# nums = [-2,1,-3,4,-1,2,1,-5,4]
# print(better(nums))
# # Output: 6
# # Explanation: The subarray [4,-1,2,1] has the largest sum 6.

# # Example 2:
# nums = [1]
# print(better(nums))
# # Output: 1
# # Explanation: The subarray [1] has the largest sum 1.

# # Example 3:
# nums = [5,4,-1,7,8]
# print(better(nums))
# # Output: 23
# # Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

# # time complexity: O(n^2)






def optimal(arr:list[int]):
    _sum = 0
    _max = 0
    for i in range(len(arr)):
        _sum += arr[i]

        if(_sum > _max):
            _max = _sum
        
        if _sum < 0:
            _sum = 0
    
    if _max > 0:
        return _max
    else:
        return []



# Example 1:
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(optimal(nums))
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.

# Example 2:
nums = [1]
print(optimal(nums))
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.

# Example 3:
nums = [5,4,-1,7,8]
print(optimal(nums))
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

# time complexity: O(n^2)