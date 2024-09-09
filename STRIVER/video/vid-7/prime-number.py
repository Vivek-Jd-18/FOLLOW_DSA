def primt_number_or_not(N):
    if(N == 0 or N ==1):
        return 0
    count = 0
    i = 1
    while (i*i<= N):
        print("nums: ",i)
        if(N%i == 0):
            count+=1
            print("fact: ",i)
            if((N//i) != i):
                print("fact: ",N//i)
                count+=1
        i+=1
    if(count>=2):
        return 1
    return 0

print(primt_number_or_not(15))