# A
# AB
# ABC
# ABCD
# ABCDE

def p13(row:int)->None:

    for i in range(row+1):
        for j in range(ord('A'), ord('A') + i + 1):
            print(chr(j),end="")
        print("")

row = 4
p13(row)