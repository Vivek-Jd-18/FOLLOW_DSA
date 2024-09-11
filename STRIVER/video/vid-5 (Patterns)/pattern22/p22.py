# 4 4 4 4 4 4 4
# 4 3 3 3 3 3 4
# 4 3 2 2 2 3 4
# 4 3 2 1 2 3 4
# 4 3 2 2 2 3 4
# 4 3 3 3 3 3 4
# 4 4 4 4 4 4 4

# COPIED solutiosn, i haven't found a solution by my self yet

# formula:
# start from reverese
# (n-i)

def p22(row:int)->None:

    for i in range((2*row)-1):
        for j in range((2*row)-1):

            top = i
            bottom = j
            left = (2*row- 2) - i
            right = (2*row- 2) - j

            print(row-min(min(top,bottom),min(left,right)),end=" ")

        print(" ")

row = 4
p22(row)


# def p22(row:int)->None:

#     for i in range(row):

#         # first phase
#         itr = row
#         for j in range(row,0,-1):
#             print(itr,end="")
#             if(j >= (row-i+1)):
#                 itr-=1
        
#         # second phase
#         itr = (row-i)
#         for j in range(1, row+1):
#             print(itr,end="")
#             if(j > (row-i)):
#                 itr+=1

#         print(" ")

# row = 4
# p22(row)
