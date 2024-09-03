# ****
# ****
# ****
# ****

def p1(row: int, col:int)-> None:
    for i in range(4):
        for j in range(4):
            print("*",end="")
        print("")

row = 4
col = 4
p1(row,col)