# String Operations

# Define a string
a = "   aayush!!!!!!! Tiruwa John  " 

# Print the length of the string
print(len(a))

# Print the string in uppercase
print(a.upper())

# Print the string in lowercase
print(a.lower())

# Print the string with leading and trailing whitespaces removed
print(a.strip())

# Print the string with trailing exclamation marks removed
print(a.rstrip("!!!!!!"))

# Print the string with a replacement
print(a.replace("Aayush!!!!!!!", "John"))

# Split the string into a list of substrings based on the given delimiter
print(a.split(" "))


# Capitalization and Formatting

# Define a string
blogHeading = "python is a great language"

# Print the string with the first character capitalized
print(blogHeading.capitalize())

# Define a string
str1 = "Welcome to the world of Python"

# Print the string centered in a field of width 50
print(str1.center(50))


# String Searching and Counting

# Print the length of the string
print(len(str1))

# Define a string
str2 = "Abcdefgha"

# Count the occurrences of a specific substring in the string
countStr = str2.count("a")
print(countStr)

# Define a string
str3 = "Python is a great language"

# Check if the string ends with a specific substring
print(str3.endswith(" "))

# Define a string
str4 = "He's name is Dan. He is an honest man."

# Find the first occurrence of a specific substring in the string
print(str4.find("h"))


# String Validation

# Define a string
str5 = "He's name is Dan. Dan is an honest man."

# Check if the string is alphanumeric
print(str5.isalnum())

# Define a string
str6 = "Python is a great language"

# Check if the string is printable
print(str6.isprintable())

# Define a string
str7 = "We wish you a Merry Christmas"

# Check if the string is printable
print(str7.isprintable())

# Define a string
str8 = "      "

# Check if the string contains only whitespace characters
print(str8.isspace())

# Define a string
str9 = "        "

# Check if the string contains only whitespace characters
print(str9.isspace())

# Define a string
str9 = "World Health Organization"

# Check if the string is in titlecase
print(str9.istitle())


# String Manipulation

# Define a string
str10 = "Python is a interpreted language"

# Check if the string starts with a specific substring
print(str10.startswith("Python"))

# Define a string
str11 = "Python is a interpreted language"

# Print the string with uppercase characters converted to lowercase and vice versa
print(str11.swapcase())

# Define a string
str12 = "Python is a interpreted language"

# Print the string with each word capitalized
print(str12.title())
