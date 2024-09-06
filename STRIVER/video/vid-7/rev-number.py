import sys
#  time complexity  = O(Log(X))

MIN_SIZE = -2**31 
MAX_SIZE = 2**31 - 1

def evenlyDivides(N):
    # code here
    n = N
    rev_num = 0
    
    
    if(str(N)[0] == '-'):
        n = int(str(N)[1:])
    while n!=0 :
        temp = n%10
        rev_num = (rev_num * 10) + temp
        n = n // 10

    if(rev_num > MAX_SIZE or rev_num < MIN_SIZE):
            return 0
    
    if(str(N)[0] == '-'):
        return int('-'+str(rev_num))
    else:
        return rev_num

print(evenlyDivides(1534236469))