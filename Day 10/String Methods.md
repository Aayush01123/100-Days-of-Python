# String methods

<br>
Python provides a set of built-in methods that we can use to alter and modify the strings.

# upper():

<br>
The upper() method converts a strings to upper case.

# Example:

<br>
```
str1 = "abcde"
print(str1.upper())
```

# Output:

<br>
```
ABCDE
```

# lower()

<br>
The lower() method converts a string to lower case.

# Example:

```
str1 = "AbcDe"
print(str1.lower())
```

# Output
<br>
```
abcde
```

# strip():

<br>
The strip() method removes any white spaces before and after the string.

# Example:

```
str2 = "Silver Spoon"
print(str2.strip())
```

# Output:

```
Silver Spoon
```

# rstrip():

<br>
The rstrip() removes any tralling characters. Example:

# Example
```
str3 = "Hello !!!"
print(str3.rstrip("!"))
```

# Output:

```
Hello # it will remove !!
```

# replace():

The replace() method replaces all occurences of a string with another string. Example:

# Example :
```
str2 = "Silver Spoon"
print(str2.replace("Sp", "M"))
```

# Output:

```
Silver Moon
```

# split():

The split() method splits the given string at the specified instance and returns the seperated strings as list items

# Example:

```
str2 = "Silver Spoon"
print(str2.split(" ")) # Splits the string at the whitespace " ".
```

# Output:

```
['Silver', 'Spoon']
There are various other string methods that we can use to modify our strings.
```

# capitalize():

<br>
The capitalize() method turns only the first character of the string to uppercase and the rest other characters of the string are turned to lowercase. The string has no effect if the first character is already uppercase.

# Example:

```
str1 = "hello"
capStr1 = str1.capitalize()
print(capStr1)

str2 = "hello World"
capStr2 = str2.capitalize()
print(capStr2)
```

# Center():

The center() method aligns the string to the center as per the parameters given by the user.

# Example:

```
str1 = "Welcome to the Console!!!"
print(str1.center(50))
```

# Output:

```
            Welcome to the Console!!!
```

# count():

The count method returns the number of times the given value has occured within the given string.

# Example:

```
str2 = "Abcdefgha"
countStr = str2.count("a")
print(countStr)
```

# endswitch():

The endswitch() method checks if the string ends with a given value. If yes then return True, else, return False.

# Example :

```
str1 = "Welcome to the Console !!!"
print(str1.endswitch("!!!))
```

# Output:

```
True
```

We can even also check if a value in-between the string by providing start and end index position

# Example:

```
str1 = "Welcome to the Console !!!"
print(str1.endswitch("to", 4, 10))
```

# find():

The find() method searchs for the first occurrence of the given value and returns the index where it is present. if given value is absent from the string then return -1.

# Example:

```
str1 = "He's name is Dan. He is an honest man."
print(str1.find("is"))
```

# Output

```
-1
```

# index()

The index() method searches for the first occurence of the given value and returns the index where it is present. If given value is absent from the string then raise an exception.

# Example:

str1 = "He's name is Dan. Dan is an honest man."
print(str1.index("Dan"))

# isalpha():

The isalnum() method return True only if the entire string only consists of A-Z, a-z. if any other characters or punctuations or number(0-9) are present, then it reurns False.

# Example :

```
str1 = "Welcome"
print(str1.isalpha())
```

# Ouput:

```
True
```

# islower():

<br>
The islower() method returns True if all the chracters in the string are lower case, else it returns False.

# Example:

```
str1 = "hello world"
print(str1.islower())
```

# Output:

```
True
```

# isprintable():

<br>
The isprintable() method returns True if all the values within the given string are printable, if not, then return False.

# Example:

str 1 = "We wish you a Merry Christmas"
print(str.isprintable())

# isspace():

<br>
The isspace() method returns true only and only if the string contains white spaces, else return False.

Example:

```
str1 = "    " #using Spacebar
print(str1.isspace())

str2= "     " # using Tab
print(str2.isspace())
```

# is title():

The istitle() returns True only if the first letter of each word of the string is capitalized, else it returns False.

# Example:

```
str1 = "World Heath Organization"
print(str1.istitle())
```

# Output:

```
True
```

# Example:

```
str2 = "To kill a Mocking bird"
print(str2.istitle())
```

# Output :

```
False
```

# startswith():

<br>
The endswith() method checks if the string starts with a given value. If yes then return True, else return False.

# Example :

```
str1 = "Python is a Interpreted Language"
print(str1.startswith("Python))
```

# Output:

```
True
```

# swapcase():

<br>
The swapcase() method changes the character casing of the string. Upper case are converted to lower case to upper case.

# Example :

```
str1 = "Python is a Interpreted Language"
print(str1.swapcase())
```

# Output:

```
pYTHON IS A iNTERPRETED lANGUAGE
```

# title():

<br>
The title() method capitalizes each letter of the word with the string.

# Example:

```
str1 = "He's name is Dan. Dan is an honest man."
print(str1.title())
```

# Output:

```
He's Name Is Dan. Dan Is An Honest man.
```
