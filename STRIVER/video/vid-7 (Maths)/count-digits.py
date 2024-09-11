#  time complexity  = log10(n)

def evenlyDivides(N):
    # code here
    n = N
    divs = 0
    
    while n!=0 :
        temp = n%10
        if(temp != 0 and N%temp == 0):
            divs+=1
        n = n//10
    return divs

print(evenlyDivides(232))