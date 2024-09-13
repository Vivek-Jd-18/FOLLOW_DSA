# Merge Sort
# Difficulty: MediumAccuracy: 54.1%Submissions: 191K+Points: 4
# Given an array arr[], its starting position l and its ending position r. Sort the array using merge sort algorithm.
# Example 1:

# Input:
# N = 5
# arr[] = {4 1 3 9 7}
# Output:
# 1 3 4 7 9
# Example 2:

# Input:
# N = 10
# arr[] = {10 9 8 7 6 5 4 3 2 1}
# Output:
# 1 2 3 4 5 6 7 8 9 10

# Your Task:
# You don't need to take the input or print anything. Your task is to complete the function merge() which takes arr[], l, m, r as its input parameters and modifies arr[] in-place such that it is sorted from position l to position r, and function mergeSort() which uses merge() to sort the array in ascending order using merge sort algorithm.

# Expected Time Complexity: O(nlogn) 
# Expected Auxiliary Space: O(n)

# Constraints:
# 1 <= N <= 105
# 1 <= arr[i] <= 105

# problem link = https://www.geeksforgeeks.org/problems/merge-sort/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=merge-sort 

# approach 1: Striver's Approach


def merge(left_li:list[int], right_li: list[int]):
    local_li: list[int] = [] 
    i,j = 0, 0

    while(i < len(left_li) and j < len(right_li)):
        if(left_li[i] <= right_li[j]):
            local_li.append(left_li[i])
            i+=1
        else:
            local_li.append(right_li[j])
            j+=1
    
    left_rem, right_rem = left_li[i:], right_li[j:]

    return local_li + left_rem + right_rem
        

def divider(arr: list[int]):
    if(len(arr) <= 1):
        return arr
    
    mid = (len(arr)) // 2

    # l = [:mid]
    # r = [mid:]

    left, right = divider(l), divider(r)
    

arr = [2,4,7,1,5,3]

print("Array before: ",arr)
print("Array after: ",divider(arr))















# def divider(arr: list[int]):
#     le:int = len(arr)
#     if(le <= 1):
#         return arr
    
#     mid:int = le//2

#     l:list[int] = arr[:mid]
#     r:list[int] = arr[mid:]

#     left_list: list[int]; right_list:list[int]
#     left_list, right_list = divider(l), divider(r)

#     return merge(left_list, right_list)



# def merge(left_list:list[int], right_list:list[int]):
#     li:list[int] = []
#     i, j = 0, 0

#     while(i < len(left_list) and j < len(right_list)):
#         if(left_list[i] <= right_list[j]):
#             li.append(left_list[i])
#             i+=1
#         else:
#             li.append(right_list[j])
#             j+=1
    
#     left_rem, right_re = left_list[i:], right_list[j:]

#     return li + left_rem + right_re