# Given a positive integer N., The task is to find the value of Σi from 1 to N F(i) where function F(i) for the number i is defined
#  as the sum of all divisors of i.


# Example 1:

# Input:
# N = 4
# Output:
# 15
# Explanation:
# F(1) = 1
# F(2) = 1 + 2 = 3
# F(3) = 1 + 3 = 4
# F(4) = 1 + 2 + 4 = 7
# ans = F(1) + F(2) + F(3) + F(4)
#     = 1 + 3 + 4 + 7
#     = 15

# --------------------------

# Example 2:

# Input:
# N = 5
# Output:
# 21
# Explanation:
# F(1) = 1
# F(2) = 1 + 2 = 3
# F(3) = 1 + 3 = 4
# F(4) = 1 + 2 + 4 = 7
# F(5) = 1 + 5 = 6
# ans = F(1) + F(2) + F(3) + F(4) + F(5)
#     = 1 + 3 + 4 + 7 + 6
#     = 21

def print_all_divisors(N):

    # sum = 0
    # i = 1
    # while (i*i) <= N:
    #     j = 1
    #     while (j*j) <= i:
    #         if(i % j == 0):
    #             sum = sum + j
    #             if (N // j != j):
    #                 sum = sum + j
    #         j+=1
    #     i+=1
    # return  sum


    sum = 0
    i = 1
    li = []
    while (i*i) <= N:
        if(N % i == 0):
            li.append(i)
            if(N/i != i):
                li.append(N//i)
        i+=1
    return  li

print(print_all_divisors(12))
