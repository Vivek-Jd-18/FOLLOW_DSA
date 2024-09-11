# Hashing: prestore and fetch

def base(arr):
    art = [0] * len(arr)

    for i in range(len(arr)):
        art[arr[i]] += 1 
    
    return art

arr = [1,2,3,2,1,6,8,6,2]
print(base(arr))