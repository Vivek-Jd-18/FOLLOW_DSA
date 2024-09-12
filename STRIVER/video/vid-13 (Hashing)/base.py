# Hashing: prestore and fetch


# time complexity of map:
# 1) Storing and 2) Fetching takes log(n) in all cases : Best, Average and Worst Cases

# time complexity of unordered_map:
# 1) Storing 
# Best and Average Case = O(1)
# Worst Case = O(N)

# and 2) Fetching takes log(n) in all cases : Best, Average and Worst Cases

# It's recommended to use unordered_maps before regular maps

# Hashing methods:
# 1)  Division Method
# 2)Folding Method
# 3) MidSquare Method

def base(arr):
    art = [0] * len(arr)

    for i in range(len(arr)):
        art[arr[i]] += 1 
    
    return art

arr = [1,2,3,2,1,6,8,6,2]
print(base(arr))