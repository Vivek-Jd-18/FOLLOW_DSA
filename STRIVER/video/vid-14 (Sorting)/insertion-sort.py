# Insertion Sort
# Difficulty: EasyAccuracy: 66.61%Submissions: 168K+Points: 2
# The task is to complete the insert() function which is used to implement Insertion Sort.


# Examples:

# Input: n = 5, arr[] = { 4, 1, 3, 9, 7}
# Output: 1 3 4 7 9
# Input: n = 10, arr[] = {10, 9, 8, 7, 6, 5, 4, 3, 2, 1}
# Output: 1 2 3 4 5 6 7 8 9 10

# Your Task: 
# You don't have to read input or print anything. Your task is to complete the function insert() and insertionSort() where insert() takes the array, it's size and an index i and insertionSort() uses insert function to sort the array in ascending order using insertion sort algorithm. 

# Expected Time Complexity: O(n*n).
# Expected Auxiliary Space: O(1).P


# Constraints:
# 1 <= n <= 1000
# 1 <= arr[i] <= 1000O

# proble link: https://www.geeksforgeeks.org/problems/insertion-sort/0?category%5B%5D=Algorithms&page=1&query=category%5B%5DAlgorithmspage1

def insertion(arr):
    for i in range(len(arr)):
        j = i
        
        while j > 0 and arr[j-1] > arr[j]:
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j-=1

arr = [4, 1, 3, 9, 7]
insertion(arr)
print(arr)