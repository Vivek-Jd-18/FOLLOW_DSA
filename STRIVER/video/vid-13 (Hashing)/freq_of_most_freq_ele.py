# 1838. Frequency of the Most Frequent Element
# Medium
# Topics
# Companies
# Hint
# The frequency of an element is the number of times it occurs in an array.

# You are given an integer array nums and an integer k. In one operation, you can choose an index of nums and increment the element at that index by 1.

# Return the maximum possible frequency of an element after performing at most k operations.

 

# Example 1:

# Input: nums = [1,2,4], k = 5
# Output: 3
# Explanation: Increment the first element three times and the second element two times to make nums = [4,4,4].
# 4 has a frequency of 3.
# Example 2:

# Input: nums = [1,4,8,13], k = 5
# Output: 2
# Explanation: There are multiple optimal solutions:
# - Increment the first element three times to make nums = [4,4,8,13]. 4 has a frequency of 2.
# - Increment the second element four times to make nums = [1,8,8,13]. 8 has a frequency of 2.
# - Increment the third element five times to make nums = [1,4,13,13]. 13 has a frequency of 2.
# Example 3:

# Input: nums = [3,9,6], k = 2
# Output: 1


# problem link:https://leetcode.com/problems/frequency-of-the-most-frequent-element/description/


def freq_of_most_feq_ele(arr, k):
    freq = 0
    for i in range(len(arr)-1):
        temp_freq = 0
        if(arr[i] != arr[i+1]):
            for j in range(k+1):
                if(arr[i]+j == arr[i+1]):
                    temp_freq+=1
                    break
        freq+=temp_freq
    
    return freq + 1


# nums = [1,2,4]; k = 5
# print(freq_of_most_feq_ele(nums, k))


nums = [1,4,8,13]; k = 5
print(freq_of_most_feq_ele(nums, k))


# nums = [3,9,6], k = 2
# print(freq_of_most_feq_ele(nums, k))
