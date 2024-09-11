# Given an array arr[] of non-negative integers. Each array element represents the maximum length of the jumps that can be made forward from that element. This means if arr[i] = x, then we can jump any distance y such that y ≤ x.
# Find the minimum number of jumps to reach the end of the array starting from the first element. If an element is 0, then you cannot move through that element.
# Note:  Return -1 if you can't reach the end of the array.

# Examples : 

# Input: arr[] = {1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9}
# Output: 3 
# Explanation:First jump from 1st element to 2nd element with value 3. From here we jump to 5th element with value 9, and from here we will jump to the last. 
# Input: arr = {1, 4, 3, 2, 6, 7}
# Output: 2 
# Explanation: First we jump from the 1st to 2nd element and then jump to the last element.
# Input: arr = {0, 10, 20}
# Output: -1
# Explanation: We cannot go anywhere from the 1st element.
# Expected Time Complexity: O(n)
# Expected Space Complexity: O(1)

# Constraints:
# 0 ≤ arr[i] ≤ 105
# 2 ≤ arr.size() ≤ 106


# problem link: https://www.geeksforgeeks.org/problems/minimum-number-of-jumps-1587115620/1 


def min_jump(arr):
    if(len(arr) == 0 or arr[0] ==0 ):
        return-1
    i = 0
    count = 0

    while(len(arr) >= count+i):
        print(f"i: {i} and count: {count}")
        if(arr[i] == 0):
            break
        count+=1
        i = count + arr[i]
    return count

# print(min_jump([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9])) # requires 3 op

# print(min_jump([9, 10, 1, 2, 3, 4, 8, 0, 0, 0, 0, 0, 0, 0, 1])) # requires 2 op

# print(min_jump([1, 2, 0, 0, 0])) # requires -1 op