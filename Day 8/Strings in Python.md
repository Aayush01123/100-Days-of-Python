# What are strings?

<br>
In python, anything that you enclose between single or double quotation marks considered a string. A string is essentially a sequence or array of textual data. Strings are used when working with Unicode.

# Example

```
name = "Harry"
print("Hello, " + name)
```

# Output

```
Hello, Aayush
```

**Note**: It does not matter whether you enclose your strings in single or double quotes, the output remains the same.

Sometimes, the user might need to put quotation marks in between the strings. Example, consider the sentence: He said, "I want to eat an apple"

# Multiline Strings

<br>
If our strings has multiple lines, we can create them like this:
```
a = '''Hello How Areajasjdadjsadad
sdadaisjdjasjdjaosdj jdoijasjdojaosjd ndsndks
dsa'''
print(a)
```

# Accessing Characters of a String

<br>
In Python, string is like an array of characters, We can access parts of string by using its index which start from 0.
Squre bracket can be used to access elements of the string.

```
print(name[0])
print[name[1]]
```

# Lopping through the string

<br>
We can loop through strings using a for loop like this:

```
for character in name:
    print(character)
```

Above code prints all the characters in the string name one by one!
