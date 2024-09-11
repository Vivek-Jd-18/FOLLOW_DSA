# Print N to 1 without loop
# Difficulty: EasyAccuracy: 77.72%Submissions: 65K+Points: 2
# Print numbers from N to 1 (space separated) without the help of loops.

# Example 1:

# Input:
# N = 10
# Output: 10 9 8 7 6 5 4 3 2 1
# Your Task:
# This is a function problem. You only need to complete the function printNos() that takes N as parameter and prints number from N to 1 recursively. Don't print newline, it will be added by the driver code.


# Expected Time Complexity: O(N).
# Expected Auxiliary Space: O(N) (Recursive).

# Constraint
# 1<=n<=1000

# link to problem: https://www.geeksforgeeks.org/problems/print-n-to-1-without-loop/1


def rec_name(i):
    if(i==0):
        return
    print(i," ",end="")
    i-=1
    rec_name(i)
    
rec_name(10)