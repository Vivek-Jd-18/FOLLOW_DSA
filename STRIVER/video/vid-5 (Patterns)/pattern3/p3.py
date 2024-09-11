#  1
#  1 2
#  1 2 3
#  1 2 3 4


def p3(row:int)->None:
    for i in range(1,row+1):
        for j in range(1, i+1):
            print(j, end=" ")
        print("")

row = 5
p3(row)