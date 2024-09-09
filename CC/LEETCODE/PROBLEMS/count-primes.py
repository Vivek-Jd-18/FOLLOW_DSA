# 204. Count Primes
# Medium
# Topics
# Companies
# Hint
# Given an integer n, return the number of prime numbers that are strictly less than n.

 

# Example 1:

# Input: n = 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
# Example 2:

# Input: n = 0
# Output: 0
# Example 3:

# Input: n = 1
# Output: 0
 

# Constraints:

# 0 <= n <= 5 * 106

# link to problem:https://leetcode.com/problems/count-primes/description/

# normal approcah
# def count_primes(N):
#     if(N == 0 or N ==1):
#         return 0
#     primes = 0
#     for i in range(N):
#         j = 1
#         counts = 0
#         while(j*j <= i):
#             if(i%j == 0):
#                 counts+=1
#                 if((i//j) != j):
#                     counts +=1
#             j+=1
#         if(counts == 2):
#             primes+=1
#     return primes

# print(count_primes(10))


# Sieve of Eratosthenes approach

def count_primes(n):        
    if(n<=2):
        return 0
    
    mp = [True for i in range (n)]
    counts = 0
    i = 2

    while(i*i <= n):
        if(mp[i]):
            for j in range(i*i, n,i):
                mp[j] = False
        i+=1
    for i in range(2,len(mp)):
        if(mp[i]):
            counts+=1
    return counts

print(count_primes(10))