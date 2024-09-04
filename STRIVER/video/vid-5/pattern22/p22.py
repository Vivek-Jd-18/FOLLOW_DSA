# 4 4 4 4   4 4 4
# 4 3 3 3   3 3 4
# 4 3 2 2   2 3 4
# 4 3 2 1   2 3 4

# 4 3 2 2 2 3 4
# 4 3 3 3 3 3 4
# 4 4 4 4 4 4 4

# formula:
# start from reverese
# (n-i)


def p21(row:int)->None:

    for i in range(row,0,-1):
        itr = row
        for j in range(row,0,-1):
            print(itr,end="")
            if(j > (row-i)):
                itr-=1

        print(" ")

row = 4
p21(row)