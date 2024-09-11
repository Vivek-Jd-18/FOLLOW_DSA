    #      *
    #     * *     
    #    * * *   
    #   * * * *  
    #  * * * * *  


def p7(row:int)->None:
    for i in range(row):
        # space
        for j in range(row-i-1):
            print(" ",end="")

        # stars
        for j in range(2*i+1):
            print("*",end="")

        # space
        for j in range(row-i-1):
            print(" ",end="")
        print("")

row = 5
p7(row)