# Break statement in Python
# for i in range(12):
#     if (i == 10):
#         break  # This will break the loop when i is 10
#     print("5" "x ", i+1, " = ", 5 * (i + 1))
# print("Loop ended")

# Continue statement in Python
# for i in range(12):
#     if (i == 10):
#         print("Skip the iteration when i is 10")
#         continue
#     print("5" "x ", i+1, " = ", 5 * (i + 1))

# for i in [2,3,4,8,0]:
#     if (i%2!=0):
#         continue
#     print(i)


i = 0
while True:
    print(i)
    i = i + 1
    if(i%100 == 0):
        break