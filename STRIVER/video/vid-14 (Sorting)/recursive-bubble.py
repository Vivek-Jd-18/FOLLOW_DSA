# Given an Integer n and a list arr. Sort the array using bubble sort algorithm.

# Examples :

# Input: n = 5, arr[] = {4, 1, 3, 9, 7}
# Output: 1 3 4 7 9
# Input: n = 10, arr[] = {10, 9, 8, 7, 6, 5, 4, 3, 2, 1}
# Output: 1 2 3 4 5 6 7 8 9 10

# Your Task : 
# You don't have to read input or print anything. Your task is to complete the function bubblesort() which takes the array and it's size as input and sorts the array using bubble sort algorithm.

# Expected Time Complexity: O(n^2).
# Expected Auxiliary Space: O(1).

# Constraints:
# 1 <= n <= 103
# 1 <= arr[i] <= 103

# problem link : 

def bubble(arr, n):
    
    swapped = False
    for i in range(0, n-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            swapped = True

    if(swapped == False): return

    bubble(arr, n-1) 


arr = [4, 1, 3, 9, 7]
n = len(arr)

bubble(arr, n)
print(arr)