# ****
# *  *
# *  *
# ****

# formula: 
# printstars: only when (i==0 or i==row-1 or j==0 or j==row-1)

def p21(row:int)->None:

    for i in range(row):
        for j in range(row):
            if(i==0 or i==row-1 or j==0 or j==row-1):
                print("*",end="")
            else:
                print(" ",end="")
        print(" ")

row = 6
p21(row)
