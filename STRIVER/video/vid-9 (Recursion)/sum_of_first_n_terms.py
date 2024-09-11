# Sum of first n terms
# Difficulty: BasicAccuracy: 23.17%Submissions: 125K+Points: 1
# Given an integer n, calculate the sum of series 13 + 23 + 33 + 43 + … till n-th term.

# Example 1:

# Input:
# n=5
# Output:
# 225
# Explanation:
# 13+23+33+43+53=225
# Example 2:

# Input:
# n=7
# Output:
# 784
# Explanation:
# 13+23+33+43+53+63+73=784

# Your Task:
# You don't need to read input or print anything. Your task is to complete the function sumOfSeries() which takes the integer n as a parameter and returns the sum of the cubes of the first n natural numbers.


# Expected Time Complexity: O(1)
# Expected Auxillary Space: O(1)


# Constraints:
# 1<=n<=50000

# link to problem: https://www.geeksforgeeks.org/problems/sum-of-first-n-terms5843/1


def sum_of_first_n_terms(N):
    if(N == 0):
        return 0
    
    return N**3 + sum_of_first_n_terms(N-1)

N = 3

print(sum_of_first_n_terms(N))



# n = 3
# 1 = 1, 2 = 8, 3 = 27   => 36