# Print GFG n times without the loop.

# Example:

# Input:
# 5
# Output:
# GFG GFG GFG GFG GFG
# Your Task:
# This is a function problem. You only need to complete the function printGfg() that takes N as parameter and prints N times GFG recursively. Don't print newline, it will be added by the driver code.


# Expected Time Complexity: O(N).
# Expected Auxiliary Space: O(N) (Recursive).

# link to problem: https://www.geeksforgeeks.org/problems/print-gfg-n-times/1

def rec_name(i, N):
    if(i>N):
        return
    print("GFG ",end="")
    i+=1
    rec_name(i, N)

rec_name(1, 10)