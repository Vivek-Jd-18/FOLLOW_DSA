# Intersection of two sorted arrays
# Difficulty: EasyAccuracy: 42.53%Submissions: 52K+Points: 2
#  Given two sorted arrays arr1[] and arr2[]. Your task is to return the intersection of both arrays.

# Intersection of two arrays is said to be elements that are common in both arrays. The intersection should not count duplicate elements.

# Note: If there is no intersection then return an empty array.

# Examples:

# Input: arr1[] = [1, 2, 3, 4], arr2[] = [2, 4, 6, 7, 8]
# Output: [2, 4]
# Explanation: 2 and 4 are only common elements in both the arrays.
# Input: arr1[] = [1, 2, 2, 3, 4], arr2[] = [2, 2, 4, 6, 7, 8]
# Output: [2, 4]
# Explanation: 2 and 4 are the only common elements.
# Input: arr1[] = [1, 2], arr2[] = [3, 4]
# Output: []
# Explanation: No common elements.
# Expected Time Complexity: O(n + m)
# Expected Auxiliary Space: O(min(n,m))

#  Constraints:
# 1 <= arr1.size(),arr2.size() <= 105
# 1 <= arr1[i], arr2[i] <= 106

# problem link: https://www.geeksforgeeks.org/problems/intersection-of-two-sorted-array-1587115620/0

def intersection_of_two_arr(arr1, arr2):
    i, j = 0,0
    inter_array = []

    while i < len(arr1) and j < len(arr2):
        if(arr1[i]<arr2[j]):
            i+=1
        elif(arr2[j]<arr1[i]):
            j+=1    
        else:
            if len(inter_array) == 0 or inter_array[len(inter_array)-1] != arr1[i]:
                inter_array.append(arr1[i])
            i+=1
            j+=1
    return inter_array    


arr1 = [1, 2, 3, 4]
arr2 = [2, 4, 6, 7, 8]

print(intersection_of_two_arr(arr1, arr2))


