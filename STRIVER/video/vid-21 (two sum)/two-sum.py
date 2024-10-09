# 1. Two Sum
# Solved
# Easy
# Topics
# Companies
# Hint
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]
 

# Constraints:

# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.
 

# Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

# problem link: https://leetcode.com/problems/two-sum/description/


# def brute_two_sum(arr:list[int], target:int)-> list[int]:
#     for i in range(len(arr)):
#         for j in range(i+1, len(arr)):
#             if(arr[i]+arr[j] == target):
#                 return [i, j]
    
#     return -1



# nums = [2,7,11,15]; target = 9
# print(brute_two_sum(nums, target))
# # Output: [0,1]
# # Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# # Example 2:

# nums = [3,2,4]; target = 6
# print(brute_two_sum(nums, target))
# # Output: [1,2]
# # Example 3:

# nums = [3,3]; target = 6
# print(brute_two_sum(nums, target))
# # Output: [0,1]

# # time complexity: O(n^2)





# def better_two_sum(arr:list[int], target:int)-> list[int]:
#     _hash = {}
#     for i in range(len(arr)):
#         if (target - arr[i]) in _hash:
#             return [_hash[target - arr[i]], i]
        
#         _hash[arr[i]] = i
#     return -1


# nums = [2,7,11,15]; target = 9
# print(better_two_sum(nums, target))
# # Output: [0,1]
# # Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# # Example 2:
# nums = [3,2,4]; target = 6
# print(better_two_sum(nums, target))
# # Output: [1,2]

# # Example 3:
# nums = [3,3]; target = 6
# print(better_two_sum(nums, target))
# # Output: [0,1]

# # time complexity: O(n * log N) , spcae: O(n)










def optimal_two_sum(arr:list[int], target:int)-> list[int]:
    left, right = 0, len(arr)-1
    arr.sort()
    while left < right:
        _sum = arr[left] + arr[right]
        if _sum == target:
            return [left, right]
        elif _sum < target:
            left+=1
        else:
            right-=1
    return -1


nums = [2,7,11,15]; target = 9
print(optimal_two_sum(nums, target))
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:
nums = [3,2,4]; target = 6
print(optimal_two_sum(nums, target))
# Output: [1,2]

# Example 3:
nums = [3,3]; target = 6
print(optimal_two_sum(nums, target))
# Output: [0,1]

# time complexity: O(n) + O(log n) , spcae: O(1)