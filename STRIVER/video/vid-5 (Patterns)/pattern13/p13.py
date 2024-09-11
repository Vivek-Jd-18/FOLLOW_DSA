#  1
#  2 3 
#  4 5 6
#  7 8 9 10


def p13(row:int)->None:
    iter = 1
    for i in range(row+1):
        for j in range(i):
            print(iter,end=" ")
            iter+=1
        print("")

row = 4
p13(row)