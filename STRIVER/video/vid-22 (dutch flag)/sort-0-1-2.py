# 75. Sort Colors
# Medium
# Topics
# Companies
# Hint
# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

# You must solve this problem without using the library's sort function.

 

# Example 1:

# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# Example 2:

# Input: nums = [2,0,1]
# Output: [0,1,2]
 

# Constraints:

# n == nums.length
# 1 <= n <= 300
# nums[i] is either 0, 1, or 2.
 

# Follow up: Could you come up with a one-pass algorithm using only constant extra space?


# problem link: https://leetcode.com/problems/sort-colors/description/

# def sort_better(arr: list[int])->None:
#     zeros = 0; 
#     ones = 0; 
#     twos = 0

#     for i in range(len(arr)):
#         if arr[i] == 0:
#             zeros +=1
#         elif arr[i] == 1:
#             ones +=1
#         else:
#             twos +=1
    
#     # zeros
#     for i in range(zeros):
#         arr[i] = 0
#     # ones
#     for i in range(zeros, zeros+ones):
#         arr[i] = 1
#     # twos
#     for i in range(zeros+ones, len(arr)):
#         arr[i] = 2


# # Example 1:
# nums = [2,0,2,1,1,0]
# sort_better(nums)
# print(nums)
# # Output: [0,0,1,1,2,2]

# # Example 2:
# nums = [2,0,1]
# sort_better(nums)
# print(nums)
# # Output: [0,1,2]


# time complexity: O(2n)




def sort_optimal(arr: list[int])->None:

    low, mid, high = 0, 0, len(arr)-1 

    while(mid <= high):
        if arr[mid] == 0 :
            arr[mid], arr[low] = arr[low], arr[mid]
            low+=1
            mid+=1
        elif arr[mid] == 1:
            mid+=1
        else:
            arr[mid],arr[high] = arr[high], arr[mid]
            high-=1 


# Example 1:
nums = [2,0,2,1,1,0]
sort_optimal(nums)
print(nums)
# Output: [0,0,1,1,2,2]

# Example 2:
nums = [2,0,1]
sort_optimal(nums)
print(nums)
# Output: [0,1,2]
 