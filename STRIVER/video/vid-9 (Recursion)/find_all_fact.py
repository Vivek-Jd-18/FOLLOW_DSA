# Find all factorial numbers less than or equal to n
# Difficulty: EasyAccuracy: 48.96%Submissions: 77K+Points: 2
# A number n is called a factorial number if it is the factorial of a positive integer. For example, the first few factorial numbers are 1, 2, 6, 24, 120,
# Given a number n, the task is to return the list/vector of the factorial numbers smaller than or equal to n.

# Examples:

# Input: n = 3
# Output: 1 2
# Explanation: The first factorial number is 1 which is less than equal to n. The second number is 2 which is less than equal to n,but the third factorial number is 6 which is greater than n. So we print only 1 and 2.
# Input: n = 6
# Output: 1 2 6
# Explanation: The first three factorial numbers are less than equal to n but the fourth factorial number 24 is greater than n. So we print only first three factorial numbers.
# Expected Time Complexity: O(k), Where k is the number of factorial numbers.
# Expected Auxiliary Space: O(1)

# Constraints:
# 1<=n<=1018

# problem link: https://www.geeksforgeeks.org/problems/find-all-factorial-numbers-less-than-or-equal-to-n3548/0?problemType=functional&difficulty%255B%255D=-1&page=1&query=problemTypefunctionaldifficulty%255B%255D-1page1



# def find_all_fact(i, N):
#     if(i>N):
#         return 0
#     print(i)
#     i = i * (i+1)
#     return find_all_fact(i, N)

# n = 3
# find_all_fact(1, n)


def find_all_fact(start, iter, N):
    if(start>N):
        return []
    next = start * iter
    return [start] + find_all_fact(next, iter+1, N)        

n = 54
li = []

# series: 1*1=1, 1*2= 2, 2*3 = 6

print(find_all_fact(1, 2, n))