# x = int(input("Enter a number: "))
# # x is the variable to match

# match x:
#     #if x is 0
#     case 0:
#         print("x is 0")
#     #if x is 1
#     case 1:
#         print("x is 1")
#     case 2:
#         print("x is 2")
#     case 3:
#         print("x is 3")
#     case _:
#         print("x is not 0, 1, 2, or 3")

# x = int(input("Enter a number: "))
# # x is the variable to match
# match x:
#     # if x is 0
#     case 0:
#         print("x is 0")
#     # case with if-condition
#     case 1 if x > 0:
#         print("x is 1")
#     case _ if x != 90:
#         print("x is not 90")
#     case _ if x!=80:
#         print(x, "is not 80")


x = 4
# x is the variable to match
match x:
    # if x is 0
    case 0:
        print("x is zero")
    # case with if-condition
    case 4 if x % 2 == 0:
        print("x % 2 == 0 and case is 4")
    # Empty case with if-condition
    case _ if x < 10:
        print("x is < 10")
    # default case will only be matched if the above cases were not matched
    # so it is basically just an else:
    case _:
        print(x)
        