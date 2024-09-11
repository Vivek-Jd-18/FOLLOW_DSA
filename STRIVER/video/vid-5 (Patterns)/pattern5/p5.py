#  * * * *
#  * * * 
#  * *
#  *

def p3(row:int)->None:
    for i in range(row, 0,-1):
        for j in range(i, 0, -1):
            print("*",end=" ")
        print("")

row = 5
p3(row)