# 1 2 3 4 
# 1 2 3
# 1 2 
# 1

def p6(row:int)->None:
    for i in range(row):
        for j in range(1, row-i):
            print(j, end=" ")
        print("")

row = 5
p6(row)