fruit = "Mango"
mangolean = len(fruit)
print(mangolean)
print(fruit[0:4]) #including 0th index but not 4th index
print(fruit[1:4]) #including 1st index but not 4th index
print(fruit[:]) # including all indexes
print(fruit[:5]) # including all indexes

# # This Both are Same
print(fruit[0:-3]) # including 0th index but not -3rd index
print(fruit[0:len(fruit)-3]) # including 0th index but not -3rd index
print(fruit[-3:-1]) # including -3rd index but not -1st index

my_string = "Hello, World!"
print(len(my_string))
print(my_string[0:len(my_string)-7])
