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

# def merge(arr: list[int], start: int, mid:int, end: int):
#     temp: list[int] = []

#     left = start
#     right = mid + 1

#     while(left <= mid and right <= end):
#         if arr[left] <= arr[right]:
#             temp.append(arr[left])
#             left+=1
#         else:
#             temp.append(arr[right])
#             right+=1
    
#     while left <= mid:
#         temp.append(arr[left])
#         left+=1
    
#     while right <= end:
#         temp.append(arr[right])
#         right+=1

#     for i in range(start, end+1):
#         arr[i] = temp[i - start]


# def divider(arr: list[int], start: int, end: int):
#     if start >= end: return
#     mid = (start+end)//2
#     divider(arr, start, mid)
#     divider(arr, mid+1, end)

#     # merge
#     merge(arr, start, mid, end)



# arr = [3,2,1]
# # arr = [3,2,6,4,1,2,5]   
# print("Array before: ",arr)
# divider(arr,0 ,len(arr)-1)
# print("Array after:",arr)


























# ----------------------------------------------------------------------------------------------------



def merge(arr: list[int], start:int, mid:int, end:int):
    temp:list[int] = []

    left = start
    right = mid + 1

    while left <= mid and right <= end:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left+=1
        else:
            temp.append(arr[right])
            right+=1
        
    while left <= mid:
        temp.append(arr[left])
        left+=1

    while right <= end:
        temp.append(arr[right])
        right+=1

    for i in range(start, end+1):
        arr[i] = temp[i - start]

def divider(arr: list[int], start:int, end:int):
   
    if start >= end: 
        return

    mid = (start+end) // 2
    divider(arr, start, mid)
    divider(arr, mid+1, end)

    # merge
    merge(arr, start, mid, end)


arr = [2,4,6,1,3,5,9,2,1] 
print("before: ",arr)
divider(arr,0 , len(arr)-1)
print("after: ",arr)