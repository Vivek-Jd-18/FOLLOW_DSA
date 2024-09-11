# *
# * *
# * * *
# * * * * 

def p2(row:int)->None:
    for i in range(row):
        for j in range(i):
            print("* ",end="")
        print("")

row = 5
p2(row)