# You are given a 3-digit number n, Find whether it is an Armstrong number or not.

# An Armstrong number of three digits is a number such that the sum of the cubes of 
# its digits is equal to the number itself. 371 is an Armstrong number since 33 + 73 + 13 = 371. 

# Examples

# Input: n = 153
# Output: true
# Explanation: 153 is an Armstrong number since 13 + 53 + 33 = 153. Hence answer is "true".

# Input: n = 372
# Output: false
# Explanation: 372 is not an Armstrong number since 33 + 73 + 23 = 378. Hence answer is "false".




def if_armstring(N):
    n = N 
    arm = 0

    while(n!=0):
        temp = n%10
        arm = (temp**3)+arm
        n = n//10
    
    return (arm == N), arm

print(if_armstring(153))