# E
# D E
# C D E
# B C D E
# A B C D E 

def p18(row:int)->None:

    for i in range(row+1):
        ch = (row-i-1)+ord('A')+1
        for j in range(i):
            print(f"{chr(ch)} ",end="")
            ch+=1
        print(" ")

row = 5
p18(row)
