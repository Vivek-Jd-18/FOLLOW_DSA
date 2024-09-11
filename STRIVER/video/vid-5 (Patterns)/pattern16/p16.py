# A
# BB
# CCC
# DDDD
# EEEEE

def p16(row:int)->None:

    for i in range(ord('A'),row+ord('A')+1):
        for j in range(ord('A'), i+1):
            print(chr(i),end="")
        print("")

row = 4
p16(row)