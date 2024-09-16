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


def divider(arr: list[int]):
    if (len(arr) <=1): 
        return arr

    mid = len(arr) // 2

    l = arr[:mid]
    r = arr[mid:]

    left_li, right_li = divider(l), divider(r)

    # final merge
    return merge(left_li, right_li)


def merge(left_li:list[int], righty_li:list[int]):
    temp:list[int] = []
    left_pointer, right_pointer = 0, 0

    while left_pointer < len(left_li) and right_pointer < len(righty_li):
        if left_li[left_pointer] <= righty_li[right_pointer]:
            temp.append(left_li[left_pointer])
            left_pointer+=1
        else:
            temp.append(righty_li[right_pointer])
            right_pointer+=1
        
    left_rem, right_rem = left_li[left_pointer:], righty_li[right_pointer:]

    return temp + left_rem + right_rem

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