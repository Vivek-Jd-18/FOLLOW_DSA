# Print 1 To N Without Loop
# Difficulty: BasicAccuracy: 61.33%Submissions: 228K+Points: 1
# Print numbers from 1 to n without the help of loops. You only need to complete the function printNos() that takes N as parameter and prints number from 1 to N recursively.

# Don't print newline, it will be added by the driver code.

# Examples

# Input: n = 10
# Output: 1 2 3 4 5 6 7 8 9 10
# Input: n = 5
# Output: 1 2 3 4 5
# Expected Time Complexity: O(n).
# Expected Auxiliary Space: O(n) (Recursive).

# Constraints:
# 1 <= n <= 1000

# problem link: https://www.geeksforgeeks.org/problems/print-1-to-n-without-using-loops-1587115620/1


def rec1(i, n):
    if(i>n):
        return
    print(i)
    i+=1
    rec1(i,n)

n = 10

rec1(1,n)
