# 169. Majority Element
# Easy
# Topics
# Companies
# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

# Example 1:

# Input: nums = [3,2,3]
# Output: 3
# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2
 

# Constraints:

# n == nums.length
# 1 <= n <= 5 * 104
# -109 <= nums[i] <= 109
 

# Follow-up: Could you solve the problem in linear time and in O(1) space?



def main(arr:list[int]):
    # first check most ocuuring constantly
    count = 0
    ele = -1
    for i in range(len(arr)):
        if(count == 0):
            count = 1
            ele = arr[i]
        elif arr[i] == ele:
            count+=1
        else:
            count-=1

    # check if it appeared (> n/2) in arr or not
        count2 = 0
        for i in range(len(arr)):
            if(ele == arr[i]):
                count2+=1
        if count2 > len(arr)//2:
            return ele
        else:
            return -1
        


# Example 1:
nums = [3,2,3]
print(main(nums))
# Output: 3

# Example 2:
nums = [2,2,1,1,1,2,2]
print(main(nums))
# Output: 2

# time complexity: O(n)