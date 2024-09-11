    #  * * * * *  
    #   * * * *  
    #    * * *   
    #     * *     
    #      *


def p8(row:int)->None:
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
p8(row)