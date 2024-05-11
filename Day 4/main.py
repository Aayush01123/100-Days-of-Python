a = 11212221212
b = True
c = "Aayush"
d = None
e = 12.3
f = complex(1, 2)

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)


print("The type of a is ", type(a))
print("The type of b is", type(b))
print("The type of c is", type(c))
print("The type of d is", type(d))
print("The type of e is", type(e))
print("The type of f is", type(f))

# List is mutable which can be changed after creation.
list1 = [1, 2, 3, 4, 5, [-4, 5], ["apple", "banana", "cherry"]]
print(list1)

# Tuple is immutable which can't be changed after creation.
tuple1 = ("Parrot", "Peacock", "Pigeon"), (1, 2, 3, 4, 5), (1.2, 3.4, 5.6)
print(tuple1)

# Dictionary is a collection of key-value pairs.
dict1 = {"name": "Aayush", "age": 20, ", can_vote": True}
print(dict1)