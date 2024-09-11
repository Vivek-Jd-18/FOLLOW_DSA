def is_palindrome(N):
    n = N
    pal = 0

    if(N<0):
        n = -n

    while(n!=0):
        temp = n%10
        pal = pal*10 + temp
        n = n//10
    return (pal == N)

print(is_palindrome(1234321))