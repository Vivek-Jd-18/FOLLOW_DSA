# Union of Two Sorted Arrays
# Difficulty: MediumAccuracy: 31.39%Submissions: 319K+Points: 4
# Given two sorted arrays of size n and m respectively, find their union. The Union of two arrays can be defined as the common and distinct elements in the two arrays. Return the elements in sorted order.

# Example 1:

# Input: 
# n = 5, arr1[] = {1, 2, 3, 4, 5}  
# m = 5, arr2 [] = {1, 2, 3, 6, 7}
# Output: 
# 1 2 3 4 5 6 7
# Explanation: 
# Distinct elements including both the arrays are: 1 2 3 4 5 6 7.
# Example 2:

# Input: 
# n = 5, arr1[] = {2, 2, 3, 4, 5}  
# m = 5, arr2[] = {1, 1, 2, 3, 4}
# Output: 
# 1 2 3 4 5
# Explanation: 
# Distinct elements including both the arrays are: 1 2 3 4 5.
# Example 3:

# Input:
# n = 5, arr1[] = {1, 1, 1, 1, 1}
# m = 5, arr2[] = {2, 2, 2, 2, 2}
# Output: 
# 1 2
# Explanation: 
# Distinct elements including both the arrays are: 1 2.
# Your Task: 
# You do not need to read input or print anything. Complete the function findUnion() that takes two arrays arr1[], arr2[], and their size n and m as input parameters and returns a list containing the union of the two arrays.

# Expected Time Complexity: O(n+m).
# Expected Auxiliary Space: O(n+m).

# Constraints:
# 1 <= n, m <= 105
# -109 <= arr1[i], arr2[i] <= 109


# problem link: https://www.geeksforgeeks.org/problems/union-of-two-sorted-arrays-1587115621/1


def union_of_two_arr(a1: list[int], a2: list[int])->list[int]:
    i, j = 0, 0
    temp: list[int] = []

    # while one of the array gets empty

    while i < len(a1) and j < len(a2):
        # if a1[i] is smaller
        if a1[i] < a2[j]:
            if len(temp) == 0 or temp[len(temp)-1] != a1[i]:
                temp.append(a1[i])
            i+=1
        # if a2[j] is smaller
        else:
            if len(temp) == 0 or temp[len(temp)-1] != a2[j]:
                temp.append(a2[j])
            j+=1

    # filling up remaining elements
    while i < len(a1):
        if len(temp) == 0 or temp[len(temp)-1] != a1[i]:
            temp.append(a1[i])
        i+=1

    while j < len(a2):
        if len(temp) == 0 or temp[len(temp)-1] != a2[j]:
            temp.append(a2[j])
        j+=1

    return temp



# n1 = [1, 2, 3, 4, 5]
# n2 = [1, 2, 3, 6, 7]

n1 = [-7, 8]
n2 = [-8, -3, 8]

print(union_of_two_arr(n1, n2))