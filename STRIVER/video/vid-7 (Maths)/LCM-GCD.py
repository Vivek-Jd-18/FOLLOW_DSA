# LCM And GCD

# Given two integers a and b, write a function lcmAndGcd() to compute their LCM and GCD. The function takes two integers a and b as input and returns a list containing their LCM and GCD.

# Example 1:

# Input: a = 5 , b = 10
# Output: 10 5
# Explanation: LCM of 5 and 10 is 10, while their GCD is 5.
# Input: a = 14 , b = 8
# Output: 56 2
# Explanation: LCM of 14 and 8 is 56, while their GCD is 2.
# Expected Time Complexity: O(log(min(a, b))
# Expected Auxiliary Space: O(1)

# Constraints:
# 1 <= a, b <= 109

# link to problem: https://www.geeksforgeeks.org/problems/lcm-and-gcd4516/1

# A = 10, B = 20

# GCD(A, B): 10
#
#  A = 1, 2, 5, '10' 
#  B = 1, 2, 4, 5, '10', 20

# LCM(A, B) = 20 
# 
# 10 = 10, '20', 30, 40, 50,...
# 20 = '20', 40, 60, 80, 100,...


def gcd_n_lcm(a, b):
    A, B = a, b

    gcd, lcm = 0, 0

    # find GCD 
    while(A > 0 and B > 0):
        if(A>B):
            A = A % B
        else:
            B = B % A

        if(A==0):
            gcd = B
        else:
            gcd = A

    # find LCM
    greater, smaller = 0, 0
    if(a>b):
        greater = a
        smaller = b
    else:
        greater = b
        smaller = a
    
    print("-- ",greater, smaller," --")
    for i in range(greater, a*b+1, greater):
        if i % smaller == 0:
            lcm = i
            break
    return gcd, lcm

print(gcd_n_lcm(20,10))



# def gcd_n_lcm(a, b):
#     original_a, original_b = a, b  # Save original values for LCM calculation
#     gcd, lcm = 0, 0

#     # Find GCD using Euclidean algorithm
#     while a > 0 and b > 0:
#         if a > b:
#             a = a % b  # Use modulus instead of division
#         else:
#             b = b % a

#     gcd = b if a == 0 else a  # Assign GCD after the loop

#     # Find LCM using the formula: LCM = (a * b) / GCD
#     lcm = (original_a * original_b) // gcd  # Use original values for LCM

#     print(gcd, lcm)  # Print GCD and LCM
#     return gcd

# print(gcd_n_lcm(10, 5))
