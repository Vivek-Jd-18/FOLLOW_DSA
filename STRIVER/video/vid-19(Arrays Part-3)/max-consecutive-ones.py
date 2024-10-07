# 485. Max Consecutive Ones
# Easy
# Topics
# Companies
# Hint
# Given a binary array nums, return the maximum number of consecutive 1's in the array.

# Example 1:

# Input: nums = [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
# Example 2:

# Input: nums = [1,0,1,1,0,1]
# Output: 2
 

# Constraints:

# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.

# problem link :https://leetcode.com/problems/max-consecutive-ones/description/

def max_consecutive_ones(arr: list[int])-> int:
    maxOccurance = 0
    count = 0

    for i in range(len(arr)):
        if arr[i] == 1:
            count+=1
        else:
            if count > maxOccurance:
                maxOccurance = count
            count = 0
        
    return max(maxOccurance, count)


nums = [1,1,0,1,1,1]
print(max_consecutive_ones(nums))
# Output: 3

nums = [1,0,1,1,0,1]
print(max_consecutive_ones(nums))
# Output: 2