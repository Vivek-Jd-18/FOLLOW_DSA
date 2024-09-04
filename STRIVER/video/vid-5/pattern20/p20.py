#0 *        * -> (4-0)*2 = 8
#1 **      ** -> (4-1)*2 = 6
#2 ***    *** -> (4-2)*2 = 4
#3 ****  **** -> (4-3)*2 = 2
#4 ********** -> (4-4)*2 = 0
#5 ****  **** -> (4-3)*2 = 2
#6 ***    *** -> (4-3)*2 = 2
#7 **      ** -> (4-3)*2 = 2
#8 *        * -> (4-3)*2 = 2

# formula: 
# stuff (i+1)
# space (row-i)*2
# stuff (i+1)


def p20(row:int)->None:

    # upper part 
    for i in range(row):
        # space
        for j in range(i+1):
            print("*",end="")

        # stuff
        for j in range((row-i)*2):
            print("-",end="")

        # space
        for j in range(i+1):
            print("*",end="")

        print(" ")

    # lower part 
    for i in range(row,-1,-1):
        # space
        for j in range(i+1):
            print("*",end="")

        # stuff
        for j in range((row-i)*2):
            print("-",end="")

        # space
        for j in range(i+1):
            print("*",end="")

        print(" ")

row = 5
p20(row)
