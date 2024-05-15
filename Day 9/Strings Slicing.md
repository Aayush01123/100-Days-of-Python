# String Slicing & Operations on String

<br>

# Length of a String

<br>
We can find the length of a string using len() function.

# Example:
<br>

```
fruit = "Mango"
len1 = len(fruit)
print("Mango is a", len1, "Letter word.")
```

# Output:
<br>
```
Mango is a 5 letter word.
```

# Example
<br>
```
# Define a sample string
my_string = "Hello, World!"

# Extracting characters:
print(my_string[0])     # Output: H
print(my_string[7])     # Output: W

# Slicing to get a substring:
print(my_string[0:5])   # Output: Hello (from index 0 to 4)
print(my_string[7:12])  # Output: World (from index 7 to 11)

# Using negative indices (counting from the end of the string):
print(my_string[-6:])   # Output: World! (last 6 characters)
print(my_string[:-7])   # Output: Hello, (exclude last 7 characters)

# Using step size:
print(my_string[::2])   # Output: Hlo ol! (every second character)
```

# String as an array

A string is essentially a sequence of characters also called a array. Thus we can access the elements of this array.

# Example:

pie = "ApplePie"
print(pie[:5])
print(pie[6]) #returns chracter at specified index

# Output:

Apple
i
