# 1 - - - - - - 1
# 1 2 - - - - 2 1
# 1 2 3 - - 3 2 1 
# 1 2 3 4 4 3 2 1


def p12(row:int)->None:
    for i in range(1,row+1):
    # layer 1
        for j in range(1,i+1):
            print(j,end="")
    # layer 2
        for j in range(1,2 *(row - i)+1):
            print(" ",end="")
    # layer 3
        for j in range(i, 0,-1):
            print(j,end="")
        print("")

row = 4
p12(row)