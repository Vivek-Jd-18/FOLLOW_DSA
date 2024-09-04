#    A
#   ABA
#  ABCBA
# ABCDCBA

def p17(row:int)->None:

    for i in range(row):

        # space
        for j in range(row-i-1):
            print("-",end="")

        # stuff
        ch = ord('A')
        brk = ((2*i)+1) / 2
        for j in range(1, (2*i)+2):
            print(chr(ch),end="")
            if j <= brk:
                ch+=1
            else:
                ch-=1

        # space
        for j in range(row-i-1):
            print("-",end="")
        print(" ")

row = 4
p17(row)



# --------------------------------another type ---------------------------------------

# #    A   
# #   B B  
# #  C C C 
# # D D D D

# def p17(row:int)->None:

#     for i in range(row):

#         # space
#         for j in range(row-i-1):
#             print("-",end="")

#         # stuff
#         for j in range((2*i)+1):
#             ch = ord('A')+i
#             print(chr(ch),end="")

#         # space
#         for j in range(row-i-1):
#             print("-",end="")
#         print(" ")

# row = 4
# p17(row)
