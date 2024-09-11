# 1
# 0 1
# 1 0 1
# 0 1 0 1
# 1 0 1 0 1


# approach 1
# def p11(row:int)->None:

#     for i in range(row+1):
#         for j in range(i):
#             if(i%2 == 0 and j%2 == 0):
#                 print("0 ",end="")  
#             else:
#                 print("1 ",end="")
#         print("")

# row = 5
# p11(row)


# approach 2
def p11_2(row:int)->None:
    flag = 1
    for i in range(row+1):
        if i%2 != 0:flag = 1 
        else: flag = 0
        for j in range(i):
            print(flag,end=" ")
            flag = 1- flag
        print("")

row = 5
p11_2(row)