# *
# * *
# * * *
# * * * * 
# * * * * *
# * * * * 
# * * *
# * *
# *


def p10(row:int)->None:
    # upper
    for i in range(row):
        for j in range(i):
            print("* ",end="")
        print("")

    # #lower 
    for i in range(row, -1, -1):
        for j in range(i):
            print("* ",end="")
        print("")

row = 4
p10(row)