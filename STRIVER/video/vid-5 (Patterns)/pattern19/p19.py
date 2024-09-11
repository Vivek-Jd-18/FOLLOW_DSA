# ********
# ***  ***
# **    **
# *      *
# *      *
# **    **
# ***  ***
# ********

# formula: 
# space (row-i)
# stuff (2*i)
# space (row-i)

def p19(row:int)->None:

    # upper part 
    for i in range(row):
        # space
        for j in range(row-i):
            print("*",end="")

        # stuff
        for j in range((2*i)):
            print(" ",end="")

        # space
        for j in range(row-i):
            print("*",end="")

        print(" ")

    # lower part 
    for i in range(row-1,-1,-1):
        # space
        for j in range(row-i):
            print("*",end="")

        # stuff
        for j in range((2*i)):
            print(" ",end="")

        # space
        for j in range(row-i):
            print("*",end="")

        print(" ")

row = 5
p19(row)
