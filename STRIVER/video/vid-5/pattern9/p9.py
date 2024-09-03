    #      *
    #     * *     
    #    * * *   
    #   * * * *  
    #  * * * * *  
    #   * * * *  
    #    * * *   
    #     * *     
    #      *


def p9(row:int)->None:
    # upper
    for i in range(row):
        # space
        for j in range(row-i-1):
            print("  ",end="")

        # stars
        for j in range((2*i+1)):
            print("* ",end="")

        # space
        for j in range(row-i-1):
            print("  ",end="")

        print("")

    #lower 
    for i in range(row+1):
        # space
        for j in range(i):
            print("  ",end="")

        # stars
        for j in range(2*row - (2*i+1)):
            print("* ",end="")

        # space
        for j in range(i):
            print("  ",end="")

        print("")

row = 3
p9(row)