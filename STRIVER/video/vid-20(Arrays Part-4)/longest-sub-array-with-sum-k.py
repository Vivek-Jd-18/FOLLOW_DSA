# Longest Sub-Array with Sum K
# Difficulty: MediumAccuracy: 24.64%Submissions: 438K+Points: 4
# Given an array arr containing n integers and an integer k. Your task is to find the length of the longest Sub-Array with the sum of the elements equal to the given value k.

# Examples:

# Input : n = 6, arr[] = {10, 5, 2, 7, 1, 9}, k = 15
# Output : 4
# Explanation: The sub-array is {5, 2, 7, 1}.
# Input : n= 3, arr[] = {-1, 2, 3}, k = 6
# Output : 0
# Explanation: There is no such sub-array with sum 6.
# Expected Time Complexity: O(n).
# Expected Auxiliary Space: O(n).

# Constraints:
# 1<=n<=105
# -105<=arr[i], K<=105


# problem link: https://www.geeksforgeeks.org/problems/longest-sub-array-with-sum-k0809/1

# # Brute-Force approach 

# def longest_sub_array(arr: list[int], k:int) -> int:
#     longest_len = 0
#     for i in range(len(arr)):
#         sum = 0
#         for j in range(i, len(arr)):
#             sum = sum + arr[j] 
#             if(sum == k):
#                 longest_len = max(longest_len, j-i+1)
    
#     return longest_len

# n = 6; arr = [10, 5, 2, 7, 1, 9]; k = 15
# print(longest_sub_array(arr,k))
# # Output : 4

# n= 3; arr = [-1, 2, 3]; k = 6
# print(longest_sub_array(arr,k))
# # Output : 0


# Better approach 

# def longest_sub_array(arr: list[int], k:int) -> int:
#     longest_len = 0
#     for i in range(len(arr)):
#         sum = 0
#         for j in range(i, len(arr)):
#             sum = sum + arr[j] 
#             if(sum == k):
#                 longest_len = max(longest_len, j-i+1)
    
#     return longest_len

# n = 6; arr = [10, 5, 2, 7, 1, 9]; k = 15
# print(longest_sub_array(arr,k))
# # Output : 4

# n= 3; arr = [-1, 2, 3]; k = 6
# print(longest_sub_array(arr,k))
# # Output : 0


# # brute force ----------------------------------------------------------------
# def main(arr:list[int], k: int) -> int:
#     longest_len = 0
#     for i in range(len(arr)):
#         sum = 0
#         for j in range(i, len(arr)):
#             sum += arr[j]
#             if(sum == k):
#                 longest_len = max(longest_len, j-i+1)
    
#     return longest_len


# n = 6; arr = [10, 5, 2, 7, 1, 9]; k = 15
# print(main(arr,k))
# # # Output : 4

# n= 3; arr = [-1, 2, 3]; k = 6
# print(main(arr,k))
# # # Output : 0

# Time Complexity: O(n^2)
# Space Complexity: O(1)


# Better approach -------------------------------------------------------------
# def better(arr: list[int], k:int) -> int:
#     hash_map = {}
#     _sum = 0
#     longest_len = 0

#     for i in range(len(arr)):
#         _sum += arr[i]

#         # if sum is equal to k
#         if(_sum == k):
#             longest_len = max(longest_len, i+1)
        
#         rem = _sum - k
#         if(rem in hash_map):
#             _len = i - hash_map[rem]
#             longest_len = max(longest_len, _len)
#         if _sum not in hash_map:
#             hash_map[_sum] = i 
    
#     return longest_len         


# n = 6; arr = [10, 5, 2, 7, 1, 9]; k = 15
# print(better(arr,k))
# # # Output : 4

# n= 3; arr = [-1, 2, 3]; k = 6
# print(better(arr,k))
# # # Output : 0

# Time Complexity: O(n)
# Space Complexity: O(n)







# Optimal approach -------------------------------------------------------------

def optimal(arr:list[int], k:int) -> int:    
    left, right = 0, 0
    longest_len = 0 
    _sum = arr[0]

    while right < len(arr):
        while left <= right and _sum > k:
            _sum-=arr[left]
            left+=1
        
        if(_sum == k):
            longest_len = max(longest_len , right - left + 1)
        
        right+=1
        if(right < len(arr)):
            _sum += arr[right]
    return longest_len
        


n = 6; arr = [10, 5, 2, 7, 1, 9]; k = 15
print(optimal(arr,k))
# # Output : 4

n= 3; arr = [-1, 2, 3]; k = 6
print(optimal(arr,k))

# time complexity:  0(2n)

