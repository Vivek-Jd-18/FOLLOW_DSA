# 283. Move Zeroes
# Easy
# Topics
# Companies
# Hint
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

 

# Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:

# Input: nums = [0]
# Output: [0]
 

# Constraints:

# 1 <= nums.length <= 104
# -231 <= nums[i] <= 231 - 1
 

# Follow up: Could you minimize the total number of operations done?

# problem link: https://leetcode.com/problems/move-zeroes/description/

def move_zeros(arr: list[int])->None:
    if len(arr) == 0:return arr

    i, j = 0, 1

    # while(j < len(arr)):
    #     if(arr[j] != 0):
    #         arr[i], arr[j] = arr[j], arr[i]
    #         i+=1
    #     j+=1

    while(j<len(arr)):
        if(arr[j] != 0 and arr[i] == 0):
            arr[i], arr[j] = arr[j], arr[i]
            i+=1
        j+=1


# nums = [0,1,0,3,12]
# nums = [1,2]
nums = [1,0,1]
move_zeros(nums)
print(nums)

[0,1,0,3,12]
[1,0,0,3,12]
[1,3,0,0,12]
[1,3,12,0,0]