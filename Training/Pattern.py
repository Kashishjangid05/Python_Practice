#       *       
#     * * *
#   * * * * *
# * * * * * * *
# i =1
# while i <= 4:
#     j = 1
#     while j <= 7:
#         if j >= 5-i and j <= i+3:
#             print("*",end= " ")
#         else:
#             print(" ",end = " ")
#         j += 1
#     print()
#     i += 1


#     *
#   * * *
# * * * * *
#   * * *
#     *
# i =1
# while i <= 5:
#     j = 1
#     while j <= 5:
#         if j >= 4-i and j <= i+2:
#             print("*",end= " ")
#         else:
#             print(" ",end = " ")
#         j += 1
#     print()
#     i += 1



# *       *
# *     *
# *   *
# * *
# *
# * *
# *   *
# *     *
# *       *

# i = 1
# while i <= 5:
#     j = 1
#     while j <= 5:
#         if j == 1 or j == 6 - i:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#         j += 1
#     print()
#     i += 1

# i = 2
# while i <= 5:
#     j = 1
#     while j <= 5:
#         if j == 1 or j == i:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#         j += 1
#     print()
#     i += 1


i = 1
while i <= 5:
    j = 1
    while j <= 5:
        if i == 1 or j == 3  :
            print("*", end=" ")
        else:
            print(" ", end=" ")
        j += 1
    print()
    i += 1